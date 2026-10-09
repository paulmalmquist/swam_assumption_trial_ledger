import json, tempfile, threading, unittest
from datetime import datetime,timezone,timedelta
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from http.server import ThreadingHTTPServer
from domain import new_claim,simulate,claim_state,readiness,mutate
from server import Store,Conflict,Handler

def claim(**kw):
    d=dict(statement='Success rate meets criterion',scope='Fixture v1',owner='Tester',evidence_ref='fixture://v1',expires_at=(datetime.now(timezone.utc)+timedelta(days=1)).isoformat(),threshold=.95,sample_size=200,min_samples=100,synthetic_rate=1.,seed=123,required=True,empirical_required=False,control_pass=True,missing=False)
    return new_claim(dict(d,**kw))
def supported(**kw):
    c=claim(**kw);c['approved']={'actor':'tester'};t=simulate(c);t['review']={'decision':'accept'};c['trials']=[t];return c
class PolicyTests(unittest.TestCase):
    def test_determinism(self):
        c=claim(synthetic_rate=.7);a=simulate(c);b=simulate(c);self.assertEqual(a['observations'],b['observations']);self.assertEqual(a['config_hash'],b['config_hash'])
    def test_support_and_refutation(self):
        self.assertEqual(claim_state(supported()),'supported');self.assertEqual(claim_state(supported(synthetic_rate=.4)),'refuted')
    def test_missing_controls_and_low_sample(self):
        for kw in ({'missing':True},{'control_pass':False},{'sample_size':5}):self.assertEqual(claim_state(supported(**kw)),'inconclusive')
    def test_borderline(self):self.assertEqual(claim_state(supported(synthetic_rate=.95)),'inconclusive')
    def test_empirical_and_expiry(self):
        self.assertEqual(claim_state(supported(empirical_required=True)),'empirical_required');c=supported();c['expires_at']='2020-01-01T00:00:00+00:00';self.assertEqual(claim_state(c),'expired')
    def test_gate(self):
        r=dict(owner='Tester',risk='low',claims=[supported()]);self.assertEqual(readiness(r)['state'],'ready_for_demo_review')
        for claims in ([],[supported(synthetic_rate=.4)],[supported(empirical_required=True)]):
            r['claims']=claims;self.assertEqual(readiness(r)['state'],'blocked')
        r.update(claims=[supported()],risk='high');self.assertEqual(readiness(r)['state'],'blocked')
    def test_review_required(self):
        c=supported();c['trials'][-1]['review']=None;self.assertEqual(claim_state(c),'pending_review');c['trials'][-1]['review']={'decision':'reject'};self.assertEqual(claim_state(c),'rejected')
    def test_validation(self):
        for kw in ({'threshold':float('nan')},{'sample_size':True},{'threshold':2},{'required':'true'},{'evidence_ref':'https://real-system'}):
            with self.assertRaises(ValueError):claim(**kw)
    def test_revision(self):
        c=supported();s={'recommendations':[dict(id='r',version=1,owner='Tester',risk='low',claims=[c])]};d=dict(c,recommendation_id='r',claim_id=c['id'],statement='Changed')
        n=mutate(s,'revise',d,'Tester')['recommendations'][0]['claims'][0];self.assertEqual(n['version'],2);self.assertEqual(len(n['trials']),1);self.assertEqual(claim_state(n),'pending_approval');self.assertEqual(c['version'],1)
    def test_approval_and_duplicate(self):
        c=claim();s={'recommendations':[dict(id='r',version=1,owner='Tester',risk='low',claims=[c])]};d=dict(recommendation_id='r',claim_id=c['id'])
        with self.assertRaises(ValueError):mutate(s,'run',d,'Tester')
        s=mutate(s,'approve',dict(d,reason='Test'),'Tester');s=mutate(s,'run',d,'Tester')
        with self.assertRaises(ValueError):mutate(s,'run',d,'Tester')
class PersistenceTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.path=Path(self.tmp.name)/'db.sqlite';self.store=Store(self.path)
    def tearDown(self):self.tmp.cleanup()
    def req(self):return dict(key='key1',expected_version=self.store.read()[0],actor='Tester',action='create',data=dict(title='Test',owner='Tester',node_ref='fixture://node',rationale='Test',risk='low'))
    def test_restart_replay(self):
        self.store.change(self.req());self.assertEqual(self.store.read(),Store(self.path).read());self.assertTrue(self.store.replay()['verified'])
    def test_idempotency(self):
        r=self.req();self.store.change(r);v=self.store.read()[0];self.store.change(r);self.assertEqual(v,self.store.read()[0]);r['data']['title']='Other'
        with self.assertRaises(Conflict):self.store.change(r)
    def test_stale_write(self):
        r=self.req();self.store.change(r);r['key']='key2'
        with self.assertRaises(Conflict):self.store.change(r)
    def test_atomic_validation(self):
        before=self.store.read();r=self.req();r['data']['risk']='prohibited'
        with self.assertRaises(ValueError):self.store.change(r)
        self.assertEqual(before,self.store.read())
    def test_tamper(self):
        with self.store.connect() as db:db.execute("UPDATE events SET hash='bad' WHERE seq=1")
        with self.assertRaises(ValueError):self.store.replay()
class HTTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();Handler.store=Store(Path(self.tmp.name)/'http.sqlite');Handler.token='test-token';self.http=ThreadingHTTPServer(('127.0.0.1',0),Handler);self.thread=threading.Thread(target=self.http.serve_forever,daemon=True);self.thread.start();self.base='http://127.0.0.1:'+str(self.http.server_port)
    def tearDown(self):self.http.shutdown();self.http.server_close();self.thread.join();self.tmp.cleanup()
    def test_assets_and_export(self):
        for p in ('/','/style.css','/app.js','/api/state','/api/events','/api/export','/api/replay'):
            with urlopen(self.base+p) as r:self.assertEqual(r.status,200)
    def test_request_protection(self):
        for h in ({},{'Host':'attacker.example'},{'Origin':'https://attacker.example','X-Ledger-Token':'test-token'}):
            with self.assertRaises(HTTPError) as ctx:urlopen(Request(self.base+'/api/command',data=b'{}',headers=h))
            self.assertEqual(ctx.exception.code,403)
    def test_command(self):
        v=Handler.store.read()[0];req=dict(key='http1',expected_version=v,actor='Tester',action='create',data=dict(title='HTTP',owner='Tester',node_ref='fixture://test',rationale='Test',risk='low'))
        with urlopen(Request(self.base+'/api/command',data=json.dumps(req).encode(),headers={'Content-Type':'application/json','X-Ledger-Token':'test-token'})) as r:self.assertEqual(r.status,200)
        self.assertEqual(Handler.store.read()[0],v+1)
if __name__=='__main__':unittest.main()
