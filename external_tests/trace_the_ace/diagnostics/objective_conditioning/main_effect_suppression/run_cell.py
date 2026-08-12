#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path
import numpy as np, pandas as pd, yaml
from scipy import sparse
from sklearn.preprocessing import StandardScaler

def loadmod(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def sigmoid(x):
 x=np.asarray(x,float);o=np.empty_like(x);p=x>=0;o[p]=1/(1+np.exp(-x[p]));e=np.exp(x[~p]);o[~p]=e/(1+e);return o
def struct(a,b):
 a=a.copy();b=b.copy();m=np.nanmedian(a,axis=0);ia=np.where(np.isnan(a));ib=np.where(np.isnan(b));a[ia]=m[ia[1]];b[ib]=m[ib[1]];s=StandardScaler();return s.fit_transform(a).astype(np.float32),s.transform(b).astype(np.float32)
def center(R,obj,tr,va):
 means={o:R[tr][obj[tr]==o].mean(0,dtype=np.float64).astype(np.float32) for o in np.unique(obj[tr])};missing=set(obj[va])-set(means)
 if missing:raise AssertionError(f'missing objective support {len(missing)}')
 a=np.vstack([R[i]-means[obj[i]] for i in tr]).astype(np.float32);b=np.vstack([R[i]-means[obj[i]] for i in va]).astype(np.float32)
 for o in np.unique(obj[tr]):
  m=obj[tr]==o
  if np.max(np.abs(a[m].mean(0,dtype=np.float64)))>2e-6:raise AssertionError('centering failure')
 return a,b
def main():
 p=argparse.ArgumentParser();p.add_argument('--outer-fold',type=int,required=True);p.add_argument('--arm',choices=['B0','C0','B1','C1'],required=True);p.add_argument('--config',type=Path,required=True);p.add_argument('--index',type=Path,required=True);p.add_argument('--folds',type=Path,required=True);p.add_argument('--m0-session-features',type=Path,required=True);p.add_argument('--zt-cache',type=Path,required=True);p.add_argument('--session-semantic',type=Path,required=True);p.add_argument('--response-conditioning',type=Path,required=True);p.add_argument('--eligible-objectives',type=Path,required=True);p.add_argument('--parent-runner',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();cfg=yaml.safe_load(a.config.read_text());parent=loadmod('parent',a.parent_runner)
 for q,h in [(a.index,cfg['index_sha256_required']),(a.folds,cfg['fold_sha256_required']),(a.zt_cache,cfg['zt_cache_sha256_required']),(a.session_semantic,cfg['session_semantic_sha256_required']),(a.response_conditioning,cfg['response_conditioning_sha256_required']),(a.eligible_objectives,cfg['eligible_objectives_sha256_required'])]:
  if sha(q)!=h:raise AssertionError(f'identity mismatch {q}')
 idx=pd.read_csv(a.index,usecols=['response_id','session_id','learning_objective_id','learning_objective','is_correct']);fd=pd.read_csv(a.folds);m0=pd.read_csv(a.m0_session_features);ss=pd.read_csv(a.session_semantic);rc=pd.read_csv(a.response_conditioning);oc=list(cfg['ordinary_covariates']);df=idx.merge(fd,on='session_id',validate='many_to_one').merge(m0[['session_id',*oc]],on='session_id',validate='many_to_one').merge(ss,on='session_id',validate='many_to_one').merge(rc,on=['response_id','session_id','learning_objective_id'],validate='one_to_one');elig=set(a.eligible_objectives.read_text().splitlines());df=df[df.learning_objective_id.astype(str).isin(elig)].reset_index(drop=True)
 sessions=sorted(idx.session_id.astype(str).unique());Z=sparse.load_npz(a.zt_cache).tocsr().astype(np.float32,copy=False);sm={s:i for i,s in enumerate(sessions)};ri=np.fromiter((sm[str(x)] for x in df.session_id),dtype=np.int32);Xt=Z[ri].tocsr();del Z
 vec=parent.make_vectorizer(cfg['hashed_representation']);ot=df[['learning_objective_id','learning_objective']].drop_duplicates('learning_objective_id').sort_values('learning_objective_id');U=vec.transform(ot.learning_objective.astype(str).tolist()).tocsr().astype(np.float32);om={str(o):i for i,o in enumerate(ot.learning_objective_id)};oi=np.fromiter((om[str(o)] for o in df.learning_objective_id),dtype=np.int32);Xo=U[oi].tocsr();Xs=df[[c for c in df if c.startswith('z_s_')]].to_numpy(np.float32);R=df[[c for c in df if c.startswith('r_to_')]].to_numpy(np.float32);Xq=df[oc].to_numpy(float);y=df.is_correct.to_numpy(np.int8);g=df.session_id.astype(str).to_numpy();obj=df.learning_objective_id.astype(str).to_numpy();fa=df.fold.to_numpy(int)
 o=a.outer_fold;tr=np.flatnonzero(fa!=o);va=np.flatnonzero(fa==o);assert not(set(g[tr])&set(g[va]));qs,qv=struct(Xq[tr],Xq[va]);cr,cv=center(R,obj,tr,va);base0tr=[Xt[tr],sparse.csr_matrix(qs),sparse.csr_matrix(Xs[tr])];base0va=[Xt[va],sparse.csr_matrix(qv),sparse.csr_matrix(Xs[va])];base1tr=[Xt[tr],Xo[tr],sparse.csr_matrix(qs),sparse.csr_matrix(Xs[tr])];base1va=[Xt[va],Xo[va],sparse.csr_matrix(qv),sparse.csr_matrix(Xs[va])];spec={'B0':(base0tr,base0va),'C0':(base0tr+[sparse.csr_matrix(cr)],base0va+[sparse.csr_matrix(cv)]),'B1':(base1tr,base1va),'C1':(base1tr+[sparse.csr_matrix(cr)],base1va+[sparse.csr_matrix(cv)])};tb,vb=spec[a.arm];X=sparse.hstack(tb,format='csr',dtype=np.float32);V=sparse.hstack(vb,format='csr',dtype=np.float32);m=parent.make_classifier(cfg['base_classifier']);m.fit(X,y[tr]);score=np.asarray(m.decision_function(V),float);prob=sigmoid(score);ni=int(np.asarray(m.n_iter_).max());a.output.parent.mkdir(parents=True,exist_ok=True);np.savez_compressed(a.output,row_index=va.astype(np.int32),probability=prob.astype(np.float64),n_iter=np.asarray([ni],np.int32));print(json.dumps({'fold':o,'arm':a.arm,'n_iter':ni,'rows':len(va),'output':str(a.output)}))
if __name__=='__main__':main()
