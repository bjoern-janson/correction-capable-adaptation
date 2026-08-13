#!/usr/bin/env python3
"""Checkpoint exact frozen M2-SEM base fits one at a time; finalize an arm only after all six fits exist."""
from __future__ import annotations
import argparse,importlib.util,json,time
from pathlib import Path
import numpy as np,pandas as pd,yaml
from scipy import sparse
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import log_loss
from sklearn.linear_model import LogisticRegression

def loadmod(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sigmoid(x):
 x=np.asarray(x,float);o=np.empty_like(x);p=x>=0;o[p]=1/(1+np.exp(-x[p]));e=np.exp(x[~p]);o[~p]=e/(1+e);return o
def struct(X,tr,va):
 a=X[tr].copy();b=X[va].copy();m=np.nanmedian(a,axis=0);ia=np.where(np.isnan(a));ib=np.where(np.isnan(b));a[ia]=m[ia[1]];b[ib]=m[ib[1]];s=StandardScaler();return s.fit_transform(a).astype(np.float32),s.transform(b).astype(np.float32)
def fit(parent,arm,Xt,Xo,Xs,Xr,Xq,y,tr,va,cfg):
 a,b=struct(Xq,tr,va);tb=[Xt[tr],Xo[tr],sparse.csr_matrix(a),sparse.csr_matrix(Xs[tr])];vb=[Xt[va],Xo[va],sparse.csr_matrix(b),sparse.csr_matrix(Xs[va])]
 if arm=='M2_SC':tb.append(sparse.csr_matrix(Xr[tr]));vb.append(sparse.csr_matrix(Xr[va]))
 Xtr=sparse.hstack(tb,format='csr',dtype=np.float32);Xva=sparse.hstack(vb,format='csr',dtype=np.float32);model=parent.make_classifier(cfg);model.fit(Xtr,y[tr]);return np.asarray(model.decision_function(Xva),float),int(np.asarray(model.n_iter_).max())
def main():
 p=argparse.ArgumentParser();p.add_argument('--arm',choices=['M2_S','M2_SC'],required=True);p.add_argument('--outer-fold',type=int,required=True);p.add_argument('--index',type=Path,required=True);p.add_argument('--folds',type=Path,required=True);p.add_argument('--m0-session-features',type=Path,required=True);p.add_argument('--historical-m2-oof',type=Path,required=True);p.add_argument('--zt-cache',type=Path,required=True);p.add_argument('--session-semantic',type=Path,required=True);p.add_argument('--response-conditioning',type=Path,required=True);p.add_argument('--config',type=Path,required=True);p.add_argument('--parent-runner',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args()
 cfg=yaml.safe_load(a.config.read_text());parent=loadmod('parent',a.parent_runner);assert parent.sha256_file(a.folds)==cfg['fold_sha256_required'];assert parent.sha256_file(a.historical_m2_oof)==cfg['historical_m2_oof_sha256_required']
 idx=pd.read_csv(a.index,usecols=['response_id','session_id','learning_objective_id','learning_objective','is_correct']);fd=pd.read_csv(a.folds);m0=pd.read_csv(a.m0_session_features);hist=pd.read_csv(a.historical_m2_oof);ss=pd.read_csv(a.session_semantic);rc=pd.read_csv(a.response_conditioning);ord=list(cfg['ordinary_covariates']);dim=int(cfg['external_semantic_resource']['vector_dimension'])
 df=idx.merge(fd,on='session_id',validate='many_to_one').merge(m0[['session_id',*ord]],on='session_id',validate='many_to_one').merge(hist[['response_id','m2_o_probability']],on='response_id',validate='one_to_one').merge(ss,on='session_id',validate='many_to_one').merge(rc,on=['response_id','session_id','learning_objective_id'],validate='one_to_one')
 sessions=sorted(df.session_id.astype(str).unique());Z=sparse.load_npz(a.zt_cache).tocsr().astype(np.float32,copy=False);assert Z.shape==(len(sessions),int(cfg['hashed_representation']['n_features']));sm={s:i for i,s in enumerate(sessions)};ri=np.fromiter((sm[str(x)] for x in df.session_id),dtype=np.int32);Xt=Z[ri].tocsr();del Z
 vec=parent.make_vectorizer(cfg['hashed_representation']);ot=df[['learning_objective_id','learning_objective']].drop_duplicates('learning_objective_id').sort_values('learning_objective_id');U=vec.transform(ot.learning_objective.astype(str).tolist()).tocsr().astype(np.float32);om={str(o):i for i,o in enumerate(ot.learning_objective_id)};oi=np.fromiter((om[str(o)] for o in df.learning_objective_id),dtype=np.int32);Xo=U[oi].tocsr();Xs=df[[f'z_s_{j:02d}' for j in range(dim)]].to_numpy(np.float32);Xr=df[[f'r_to_{j:02d}' for j in range(dim)]].to_numpy(np.float32);Xq=df[ord].to_numpy(float);y=df.is_correct.to_numpy(np.int8);g=df.session_id.astype(str).to_numpy();fa=df.fold.to_numpy(np.int16)
 outer=a.outer_fold;otr=np.flatnonzero(fa!=outer);ova=np.flatnonzero(fa==outer);assert not(set(g[otr])&set(g[ova]));split=StratifiedGroupKFold(n_splits=int(cfg['inner_crossfit']['n_splits']),shuffle=bool(cfg['inner_crossfit']['shuffle']),random_state=int(cfg['inner_crossfit']['random_state']));inners=list(split.split(np.zeros(len(otr),np.int8),y[otr],groups=g[otr]));tasks=[('outer',np.arange(len(otr)),None)]+[(f'inner{k}',it,iv) for k,(it,iv) in enumerate(inners)]
 out=a.output_dir;out.mkdir(parents=True,exist_ok=True)
 for name,it,iv in tasks:
  fp=out/f'{a.arm}_fold{outer}_{name}.npz'
  if fp.exists():print(json.dumps({'skip':name,'path':str(fp)}),flush=True);continue
  if name=='outer':tr=otr;va=ova
  else:tr=otr[it];va=otr[iv];assert not(set(g[tr])&set(g[va]))
  t=time.time();score,ni=fit(parent,a.arm,Xt,Xo,Xs,Xr,Xq,y,tr,va,cfg['base_classifier']);np.savez_compressed(fp,global_index=va.astype(np.int32),score=score.astype(np.float64),n_iter=np.asarray([ni],np.int32));print(json.dumps({'completed':name,'n_iter':ni,'rows':len(va),'seconds':time.time()-t}),flush=True)
 files=[out/f'{a.arm}_fold{outer}_{name}.npz' for name,_,_ in tasks]
 if not all(x.exists() for x in files):return
 oz=np.load(files[0]);oscore=oz['score'];oidx=oz['global_index'];rp=sigmoid(oscore);raw_ll=float(log_loss(y[oidx],rp))
 inner_scores=np.full(len(otr),np.nan);nit=[]
 for k,(it,iv) in enumerate(inners):
  z=np.load(out/f'{a.arm}_fold{outer}_inner{k}.npz');assert np.array_equal(z['global_index'],otr[iv]);inner_scores[iv]=z['score'];nit.append(int(z['n_iter'][0]))
 cal=LogisticRegression(penalty=cfg['calibrator']['penalty'],solver=cfg['calibrator']['solver'],fit_intercept=bool(cfg['calibrator']['fit_intercept']),max_iter=int(cfg['calibrator']['max_iter']),tol=float(cfg['calibrator']['tol']),class_weight=cfg['calibrator']['class_weight']);cal.fit(inner_scores.reshape(-1,1),y[otr]);cp=cal.predict_proba(oscore.reshape(-1,1))[:,1];maxi=int(cfg['base_classifier']['max_iter']);oni=int(oz['n_iter'][0]);rec={'outer_fold':outer,'arm':a.arm,'outer_n_iter':oni,'inner_n_iter':nit,'all_converged':bool(oni<maxi and all(n<maxi for n in nit)),'platt_slope':float(cal.coef_[0,0]),'platt_intercept':float(cal.intercept_[0]),'raw_log_loss':raw_ll,'calibrated_log_loss':float(log_loss(y[oidx],cp)),'response_id':df.iloc[oidx].response_id.astype(str).tolist(),'raw_score':oscore.tolist(),'raw_probability':rp.tolist(),'calibrated_probability':cp.tolist()};(out/f'{a.arm}_fold{outer}.json').write_text(json.dumps(rec,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in rec.items() if k not in ('response_id','raw_score','raw_probability','calibrated_probability')},indent=2))
if __name__=='__main__':main()
