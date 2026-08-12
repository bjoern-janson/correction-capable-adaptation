#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re
from pathlib import Path
import numpy as np,pandas as pd,yaml

def token_re(cfg): return re.compile(cfg['semantic_tokenization']['token_pattern'],flags=re.UNICODE)
def sha(p):
 h=hashlib.sha256();
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def paths(root): return {p.stem:p for p in Path(root).rglob('*.csv')}
def l2(v):
 n=float(np.linalg.norm(v)); return v/n if n>0 else np.zeros_like(v)
def emb(text,r,words,V,dim):
 a=[V[words[t]] for t in r.findall((text or '').lower()) if t in words]
 if not a:return np.zeros(dim,np.float32)
 return l2(np.mean(np.stack(a),axis=0,dtype=np.float64).astype(np.float32))

def collect(a,cfg):
 r=token_re(cfg); toks=set()
 if a.index:
  df=pd.read_csv(a.index,usecols=['learning_objective']);
  for s in df.learning_objective.astype(str).unique(): toks.update(r.findall(s.lower()))
 pm=paths(a.root)
 for n,(sid,p) in enumerate(sorted(pm.items()),1):
  with p.open('r',encoding='utf-8-sig',newline='') as f:
   rd=csv.DictReader(f)
   for row in rd:toks.update(r.findall((row['content'] or '').lower()))
  if n%2000==0: print(json.dumps({'sessions':n,'tokens':len(toks)}),flush=True)
 Path(a.output).write_text('\n'.join(sorted(toks))+'\n')
 print(json.dumps({'tokens':len(toks),'sha256':sha(a.output)}))

def filter_glove(a,cfg):
 wanted=set()
 for p in a.vocab: wanted.update(Path(p).read_text().splitlines())
 res=cfg['external_semantic_resource'];dim=int(res['vector_dimension']); assert sha(a.vector)==res['extracted_vector_sha256_required']
 words=[];vals=[];rows=0
 with open(a.vector,encoding='utf-8') as f:
  for line in f:
   if not line.strip():continue
   rows+=1;w,_,tail=line.rstrip('\n').partition(' ')
   if w in wanted:
    v=np.fromstring(tail,sep=' ',dtype=np.float32); assert v.size==dim and np.isfinite(v).all();words.append(w);vals.append(v)
 assert rows==int(res['vocabulary_rows_validated'])
 A=np.stack(vals) if vals else np.zeros((0,dim),np.float32)
 np.savez_compressed(a.output,words=np.asarray(words,dtype=object),vectors=A)
 print(json.dumps({'wanted':len(wanted),'matched':len(words),'sha256':sha(a.output)}))

def shard(a,cfg):
 z=np.load(a.filtered,allow_pickle=True); wl=z['words'].tolist(); V=z['vectors']; words={w:i for i,w in enumerate(wl)};dim=V.shape[1];r=token_re(cfg); beta=float(cfg['semantic_conditioning']['beta'])
 idx=pd.read_csv(a.index,usecols=['response_id','session_id','learning_objective_id','learning_objective']); pm={}
 for root in a.root:pm.update(paths(root))
 sessions=sorted(idx.session_id.astype(str).unique())[a.start:a.end]
 objtxt=idx[['learning_objective_id','learning_objective']].drop_duplicates('learning_objective_id'); OE={str(x.learning_objective_id):emb(str(x.learning_objective),r,words,V,dim) for x in objtxt.itertuples(index=False)}
 assert all(np.any(v) for v in OE.values())
 obj_by=idx.groupby('session_id')['learning_objective_id'].apply(lambda s:sorted(set(map(str,s))))
 srows=[];rrows=[]
 for n,sid in enumerate(sessions,1):
  qs=[]
  with pm[sid].open('r',encoding='utf-8-sig',newline='') as f:
   rd=csv.DictReader(f)
   for row in rd:
    e=emb(row['content'] or '',r,words,V,dim)
    if np.any(e):qs.append(e)
  if not qs:raise AssertionError(f'zero session {sid}')
  Q=np.stack(qs).astype(np.float32);zs=Q.mean(0,dtype=np.float64).astype(np.float32);sr={'session_id':sid,'nonzero_semantic_utterances':len(qs)};sr.update({f'z_s_{j:02d}':float(zs[j]) for j in range(dim)});srows.append(sr)
  sub=idx[idx.session_id.astype(str)==sid][['response_id','learning_objective_id']]
  residual={}
  for oid in obj_by.loc[sid]:
   qo=OE[oid];lg=beta*(Q@qo);lg-=float(lg.max());w=np.exp(lg,dtype=np.float64);w/=w.sum();zc=(w[:,None]*Q).sum(0,dtype=np.float64).astype(np.float32);residual[oid]=zc-zs
  for x in sub.itertuples(index=False):
   rr={'response_id':x.response_id,'session_id':sid,'learning_objective_id':x.learning_objective_id};rv=residual[str(x.learning_objective_id)];rr.update({f'r_to_{j:02d}':float(rv[j]) for j in range(dim)});rrows.append(rr)
  if n%1000==0:print(json.dumps({'shard_sessions_done':n}),flush=True)
 out=Path(a.output);out.mkdir(parents=True,exist_ok=True);pd.DataFrame(srows).to_csv(out/f'sessions_{a.start}_{a.end}.csv',index=False,lineterminator='\n');pd.DataFrame(rrows).to_csv(out/f'responses_{a.start}_{a.end}.csv',index=False,lineterminator='\n');print(json.dumps({'sessions':len(srows),'responses':len(rrows)}))

def merge(a,cfg):
 ss=pd.concat([pd.read_csv(p) for p in sorted(Path(a.shards).glob('sessions_*.csv'))],ignore_index=True);rr=pd.concat([pd.read_csv(p) for p in sorted(Path(a.shards).glob('responses_*.csv'))],ignore_index=True);idx=pd.read_csv(a.index,usecols=['response_id','session_id','learning_objective_id']); assert ss.session_id.nunique()==idx.session_id.nunique()==len(ss); assert rr.response_id.nunique()==idx.response_id.nunique()==len(rr)
 rcols=[c for c in rr if c.startswith('r_to_')]; assert (rr[rcols].abs().sum(1)>0).any(); multi=idx.groupby('session_id').learning_objective_id.nunique();vary=False
 for sid in multi[multi>1].index:
  a0=rr[rr.session_id==sid].groupby('learning_objective_id')[rcols].first().to_numpy()
  if len(a0)>1 and any(not np.array_equal(a0[0],x) for x in a0[1:]):vary=True;break
 assert vary
 out=Path(a.output);out.mkdir(parents=True,exist_ok=True);sp=out/'session_semantic_features.csv';rp=out/'response_conditioning_features.csv';ss.sort_values('session_id').to_csv(sp,index=False,lineterminator='\n');rr.sort_values('response_id').to_csv(rp,index=False,lineterminator='\n');rec={'stage':'SEMANTIC_FEATURES_BUILT_NO_OUTCOMES','result_observed':False,'sessions':len(ss),'responses':len(rr),'R_TO_nonzero':True,'R_TO_multiobjective_variation':True,'session_features_sha256':sha(sp),'response_features_sha256':sha(rp)};(out/'semantic_feature_record.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n');print(json.dumps(rec,indent=2))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['collect','filter','shard','merge']);ap.add_argument('--config',required=True);ap.add_argument('--index');ap.add_argument('--root',action='append');ap.add_argument('--output',required=True);ap.add_argument('--vocab',action='append');ap.add_argument('--vector');ap.add_argument('--filtered');ap.add_argument('--start',type=int,default=0);ap.add_argument('--end',type=int,default=999999);ap.add_argument('--shards');a=ap.parse_args();cfg=yaml.safe_load(open(a.config));
 if a.stage=='collect':a.root=a.root[0];collect(a,cfg)
 elif a.stage=='filter':filter_glove(a,cfg)
 elif a.stage=='shard':shard(a,cfg)
 else:merge(a,cfg)
if __name__=='__main__':main()
