"""Deterministic, synthetic-only trial policy. No external calls."""
import copy
import hashlib
import json
import math
import random
import uuid
from datetime import datetime, timezone, timedelta

POLICY = 'synthetic-review-v1'
def now(): return datetime.now(timezone.utc).isoformat()
def uid(prefix): return prefix + '_' + uuid.uuid4().hex[:12]
def digest(value): return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
def require(condition, message):
    if not condition: raise ValueError(message)
def text(data, key, limit=4000):
    v = data.get(key)
    require(isinstance(v, str) and 0 < len(v.strip()) <= limit, 'invalid_' + key)
    return v.strip()
def expiry(value):
    try:
        d = datetime.fromisoformat(value.replace('Z', '+00:00'))
        require(d.tzinfo is not None, 'expiry_requires_timezone')
        return d
    except (TypeError, AttributeError, ValueError): raise ValueError('invalid_expiry')
def number(data, key, low, high, integer=False):
    v = data.get(key)
    require(type(v) in (int, float) and math.isfinite(v) and low <= v <= high, 'invalid_' + key)
    require(not integer or type(v) is int, 'invalid_' + key)
    return v

def new_claim(data):
    c = {k:text(data,k) for k in ('statement','scope','owner','evidence_ref')}
    require(c['evidence_ref'].startswith('fixture://'), 'synthetic_evidence_only')
    c['expires_at'] = text(data,'expires_at'); expiry(c['expires_at'])
    c['threshold'] = number(data,'threshold',0,1)
    c['sample_size'] = number(data,'sample_size',5,10000,True)
    c['min_samples'] = number(data,'min_samples',5,10000,True)
    c['synthetic_rate'] = number(data,'synthetic_rate',0,1)
    c['seed'] = number(data,'seed',0,2147483647,True)
    for k in ('required','empirical_required','missing','control_pass'):
        require(type(data.get(k)) is bool,'invalid_'+k); c[k]=data[k]
    c.update(id=uid('claim'), version=1, approved=None, trials=[],
             fingerprint=digest({'statement':c['statement'],'scope':c['scope']}))
    return c

def interval(successes, n):
    if not n:return [0,1]
    z=1.959963984540054; p=successes/n; den=1+z*z/n
    mid=(p+z*z/(2*n))/den
    delta=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return [max(0,mid-delta), min(1,mid+delta)]

def simulate(c):
    rng=random.Random(c['seed'])
    obs=[int(rng.random()<c['synthetic_rate']) for _ in range(c['sample_size'])] if not c['missing'] else []
    bounds=interval(sum(obs),len(obs)); outcome='inconclusive'
    if len(obs)>=c['min_samples'] and c['control_pass']:
        if bounds[0]>=c['threshold']:outcome='supported'
        elif bounds[1]<c['threshold']:outcome='refuted'
    return {'id':uid('trial'),'claim_version':c['version'],'claim_statement':c['statement'],'scope':c['scope'],'threshold':c['threshold'],'seed':c['seed'],'sample_size':c['sample_size'],'min_samples':c['min_samples'],'synthetic_rate':c['synthetic_rate'],'at':now(),'mode':'synthetic',
            'outcome':outcome,'observations':obs,'successes':sum(obs),'n':len(obs),'interval':bounds,
            'control_pass':c['control_pass'],'review':None,'evidence_ref':c['evidence_ref'],
            'config_hash':digest({k:c[k] for k in ('threshold','seed','sample_size','min_samples','synthetic_rate','missing','control_pass','scope')}),
            'evaluator':'binomial-wilson-v1','limitations':'IID Bernoulli synthetic fixture; no causal or empirical validation.'}

def claim_state(c, asof=None):
    if expiry(c['expires_at']) <= (asof or datetime.now(timezone.utc)):return 'expired'
    if not c['approved']:return 'pending_approval'
    current=[t for t in c['trials'] if t['claim_version']==c['version']]
    if not current:return 'untested'
    t=current[-1]
    if not t['review']:return 'pending_review'
    if t['review']['decision']=='reject':return 'rejected'
    if c['empirical_required'] and t['mode']!='empirical':return 'empirical_required'
    return t['outcome']

def readiness(rec):
    required=[c for c in rec['claims'] if c['required']]
    reasons=[{'claim_id':c['id'],'reason':claim_state(c),'owner':c['owner']} for c in required if claim_state(c)!='supported']
    if not required:reasons.append({'claim_id':None,'reason':'no_required_claims','owner':rec['owner']})
    if rec['risk']=='high':reasons.append({'claim_id':None,'reason':'work_authority_required','owner':rec['owner']})
    return {'state':'blocked' if reasons else 'ready_for_demo_review','reasons':reasons,
            'policy':POLICY,'production_authorized':False,'as_of':now()}

def mutate(state, action, data, actor):
    s=copy.deepcopy(state)
    if action=='create':
        rec={k:text(data,k) for k in ('title','owner','node_ref','rationale')}
        require(data.get('risk') in ('low','medium','high'),'invalid_risk')
        rec.update(id=uid('rec'),risk=data['risk'],version=1,claims=[],created_at=now())
        s['recommendations'].append(rec); return s
    rec=next((r for r in s['recommendations'] if r['id']==data.get('recommendation_id')),None)
    require(rec is not None,'recommendation_not_found')
    if action=='add_claim':
        require(len(rec['claims'])<8,'maximum_8_claims'); rec['claims'].append(new_claim(data))
    else:
        c=next((x for x in rec['claims'] if x['id']==data.get('claim_id')),None)
        require(c is not None,'claim_not_found')
        if action=='revise':
            replacement=new_claim(data)
            replacement.update(id=c['id'],version=c['version']+1,trials=c['trials'])
            rec['claims'][rec['claims'].index(c)]=replacement
        elif action=='approve':
            require(not c['approved'],'already_approved')
            require(expiry(c['expires_at'])>datetime.now(timezone.utc),'claim_expired')
            c['approved']={'actor':actor,'reason':text(data,'reason'),'at':now(),'version':c['version']}
        elif action=='run':
            require(c['approved'] is not None,'approval_required')
            require(expiry(c['expires_at'])>datetime.now(timezone.utc),'claim_expired')
            require(not any(t['claim_version']==c['version'] for t in c['trials']),'duplicate_trial_revise_first')
            c['trials'].append(simulate(c))
        elif action=='review':
            t=next((t for t in c['trials'] if t['id']==data.get('trial_id')),None)
            require(t is not None,'trial_not_found')
            require(t['claim_version']==c['version'],'stale_trial')
            require(t['review'] is None,'already_reviewed')
            require(data.get('decision') in ('accept','reject'),'invalid_decision')
            t['review']={'actor':actor,'decision':data['decision'],'reason':text(data,'reason'),'at':now()}
        else:raise ValueError('unknown_action')
    rec['version']+=1
    return s

def seed_state():
    state={'recommendations':[]}
    examples=[('Telemetry join alignment','Verify batch-to-operation alignment before interpreting excursion signals.','Data engineering','medium',[
        ('Signal rows map to the correct operation',.95,1.,False,False,True),
        ('Association survives a matched comparison',.80,.80,True,False,True),
        ('Inspection detects the relevant failure mode',.90,.98,True,False,True)]),
        ('Metric definition reconciliation','Compare first-pass yield across reports at the same grain.','Analytics owner','low',[
        ('Both reports count distinct serialized units',.95,1.,False,False,True),
        ('Denominator excludes incomplete inspections',.95,.55,False,False,True)]),
        ('Retrieval evidence freshness','Test whether cached summaries reflect the current evidence version.','Swarm owner','low',[
        ('Summaries link to the latest definition',.95,1.,False,False,True),
        ('Invalidated evidence is excluded from retrieval',.95,1.,False,True,True)])]
    for title, rationale, owner,risk,claims in examples:
        state=mutate(state,'create',dict(title=title,rationale=rationale,owner=owner,risk=risk,node_ref='fixture://swarm/'+title.lower().replace(' ','-')),'Demo curator')
        r=state['recommendations'][-1]
        for title,threshold,rate,empirical,missing,control in claims:
            data=dict(recommendation_id=r['id'],statement=title,scope='Synthetic fixture population v1; local replay only',owner=owner,evidence_ref='fixture://demo-v1',expires_at=(datetime.now(timezone.utc)+timedelta(days=30)).isoformat(),threshold=threshold,synthetic_rate=rate,sample_size=200,min_samples=100,seed=42,required=True,empirical_required=empirical,missing=missing,control_pass=control)
            state=mutate(state,'add_claim',data,'Demo curator'); r=state['recommendations'][-1]; c=r['claims'][-1]
            base=dict(recommendation_id=r['id'],claim_id=c['id'],reason='Seeded synthetic demonstration')
            state=mutate(state,'approve',base,'Demo curator')
            state=mutate(state,'run',base,'Demo curator');t=state['recommendations'][-1]['claims'][-1]['trials'][-1]
            state=mutate(state,'review',dict(base,trial_id=t['id'],decision='accept'),'Demo reviewer')
    return state
