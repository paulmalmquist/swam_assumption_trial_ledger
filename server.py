#!/usr/bin/env python3
"""Local-only web application; Python 3.10+, standard library."""
import argparse
import json
import secrets
import sqlite3
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
from domain import digest, now, seed_state, mutate, readiness, claim_state, require

ROOT=Path(__file__).resolve().parent
class Conflict(Exception):pass
class Store:
    def __init__(self,path):
        Path(path).parent.mkdir(parents=True,exist_ok=True)
        self.path=str(path); self.lock=threading.RLock()
        with self.connect() as db:
            db.execute('CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT UNIQUE NOT NULL, request_hash TEXT NOT NULL, body TEXT NOT NULL, hash TEXT NOT NULL)')
            if not db.execute('SELECT 1 FROM events LIMIT 1').fetchone():
                self.append(db,'initial-seed','seed',{},'Demo curator',seed_state())
    def connect(self):
        db=sqlite3.connect(self.path,timeout=10); db.execute('PRAGMA foreign_keys=ON'); return db
    def append(self,db,key,action,data,actor,state):
        row=db.execute('SELECT hash FROM events ORDER BY seq DESC LIMIT 1').fetchone()
        body=dict(at=now(),actor=actor,action=action,data=data,state=state,previous_hash=row[0] if row else None,schema_version=1)
        db.execute('INSERT INTO events(key,request_hash,body,hash) VALUES(?,?,?,?)',(key,digest(dict(action=action,data=data,actor=actor)),json.dumps(body,allow_nan=False),digest(body)))
    def read(self):
        with self.connect() as db:
            seq,body=db.execute('SELECT seq,body FROM events ORDER BY seq DESC LIMIT 1').fetchone()
        return seq,json.loads(body)['state']
    def change(self,req):
        require(isinstance(req,dict),'object_required')
        require(set(req)=={'action','data','actor','key','expected_version'},'invalid_request_fields')
        require(type(req['expected_version']) is int,'invalid_expected_version')
        require(isinstance(req['data'],dict),'invalid_data')
        for k in ('key','actor','action'): require(isinstance(req[k],str) and 0<len(req[k].strip())<=200,'invalid_'+k)
        with self.lock, self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            existing=db.execute('SELECT request_hash FROM events WHERE key=?',(req['key'],)).fetchone()
            fingerprint=digest({k:req[k] for k in ('action','data','actor')})
            if existing:
                if existing[0]!=fingerprint:raise Conflict('idempotency_key_reused')
                return {'replayed':True}
            seq,raw=db.execute('SELECT seq,body FROM events ORDER BY seq DESC LIMIT 1').fetchone()
            if seq!=req['expected_version']:raise Conflict('stale_version_refresh_and_retry')
            state=mutate(json.loads(raw)['state'],req['action'],req['data'],req['actor'])
            self.append(db,req['key'],req['action'],req['data'],req['actor'],state)
        return {'saved':True}
    def events(self):
        with self.connect() as db:rows=db.execute('SELECT seq,body,hash FROM events ORDER BY seq').fetchall()
        return [{'seq':seq,'hash':h,**json.loads(raw)} for seq,raw,h in rows]
    def replay(self):
        previous=None;state=None;events=self.events()
        for e in events:
            body={k:v for k,v in e.items() if k not in ('seq','hash')}
            require(body['previous_hash']==previous and digest(body)==e['hash'],'audit_hash_mismatch')
            require(body['schema_version']==1,'unknown_schema')
            state=body['state'];previous=e['hash']
        return dict(verified=True,events=len(events),state_hash=digest(state),method='Hash-verified snapshot replay',tamper_proof=False)

class Handler(BaseHTTPRequestHandler):
    store=None;token=None
    def log_message(self,fmt,*args): pass
    def send(self,status,value,ctype='application/json'):
        raw=json.dumps(value,allow_nan=False).encode() if ctype=='application/json' else value
        self.send_response(status);self.send_header('Content-Type',ctype);self.send_header('Content-Length',str(len(raw)))
        self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
        self.end_headers();self.wfile.write(raw)
    def trusted(self):
        return self.headers.get('Host') in ('localhost:'+str(self.server.server_port),'127.0.0.1:'+str(self.server.server_port))
    def do_GET(self):
        if not self.trusted():return self.send(403,{'error':'invalid_host'})
        path=urlsplit(self.path).path
        if path in ('/','/app.js','/style.css'):
            file=ROOT/'web'/({'/':'index.html','/app.js':'app.js','/style.css':'style.css'}[path]);mime={'/':'text/html; charset=utf-8','/app.js':'text/javascript','/style.css':'text/css'}[path]
            return self.send(200,file.read_bytes(),mime)
        if path=='/api/state':
            v,s=self.store.read()
            for r in s['recommendations']:
                r['readiness']=readiness(r)
                for c in r['claims']:c['state']=claim_state(c)
            return self.send(200,dict(version=v,state=s,token=self.token))
        if path=='/api/events':
            return self.send(200,[{k:v for k,v in e.items() if k not in ('state','data')} for e in self.store.events()])
        if path=='/api/export':
            v,s=self.store.read()
            return self.send(200,dict(schema_version=1,exported_at=now(),mode='synthetic',version=v,state=s,receipts=[dict(recommendation_id=r['id'],**readiness(r)) for r in s['recommendations']],events=self.store.events(),replay=self.store.replay()))
        if path=='/api/replay':
            try:return self.send(200,self.store.replay())
            except ValueError as e:return self.send(409,{'error':str(e)})
        self.send(404,{'error':'not_found'})
    def do_POST(self):
        if not self.trusted() or not secrets.compare_digest(self.headers.get('X-Ledger-Token',''),self.token):return self.send(403,{'error':'invalid_session'})
        origin=self.headers.get('Origin')
        if origin and origin not in ('http://localhost:'+str(self.server.server_port),'http://127.0.0.1:'+str(self.server.server_port)):return self.send(403,{'error':'invalid_origin'})
        if self.path!='/api/command':return self.send(404,{'error':'not_found'})
        try:
            size=int(self.headers.get('Content-Length','0'));require(0<size<=262144,'request_size_limit')
            req=json.loads(self.rfile.read(size));result=self.store.change(req);self.send(200,result)
        except Conflict as e:self.send(409,{'error':str(e)})
        except (ValueError,KeyError,TypeError) as e:self.send(400,{'error':str(e)})
        except Exception:self.send(500,{'error':'internal_error'})

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--port',type=int,default=8765);p.add_argument('--db',default=str(ROOT/'data/ledger.sqlite'));p.add_argument('--replay',action='store_true');a=p.parse_args()
    store=Store(a.db)
    if a.replay:print(json.dumps(store.replay(),indent=2));return
    Handler.store=store;Handler.token=secrets.token_urlsafe(32)
    server=ThreadingHTTPServer(('127.0.0.1',a.port),Handler)
    print(f'Swarm Assumption Trial Ledger: http://127.0.0.1:{server.server_port}',flush=True)
    print('Synthetic-only local demo. Ctrl+C to stop.',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:server.server_close()
if __name__=='__main__':main()
