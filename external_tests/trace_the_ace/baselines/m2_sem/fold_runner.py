#!/usr/bin/env python3
"""Run one frozen outer fold for M2_S and M2_SC, preserving raw and calibrated outputs."""
from __future__ import annotations
import argparse, importlib.util, json, time
from pathlib import Path
import numpy as np, pandas as pd, yaml
from scipy import sparse
from sklearn.metrics import log_loss
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler


def loadmod(name,path):
    spec=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def sigmoid(x):
    x=np.asarray(x,dtype=float); out=np.empty_like(x); pos=x>=0
    out[pos]=1/(1+np.exp(-x[pos])); ex=np.exp(x[~pos]); out[~pos]=ex/(1+ex); return out

def structured(X,tr,va):
    a=X[tr].copy(); b=X[va].copy(); med=np.nanmedian(a,axis=0)
    ia=np.where(np.isnan(a)); ib=np.where(np.isnan(b)); a[ia]=med[ia[1]]; b[ib]=med[ib[1]]
    sc=StandardScaler(); return sc.fit_transform(a).astype(np.float32),sc.transform(b).astype(np.float32)

def fit_score(parent,arm,Xt,Xo,Xs,Xr,Xstruct,y,tr,va,cfg):
    ats,avs=structured(Xstruct,tr,va)
    trb=[Xt[tr],Xo[tr],sparse.csr_matrix(ats),sparse.csr_matrix(Xs[tr])]
    vab=[Xt[va],Xo[va],sparse.csr_matrix(avs),sparse.csr_matrix(Xs[va])]
    if arm=='M2_SC': trb.append(sparse.csr_matrix(Xr[tr])); vab.append(sparse.csr_matrix(Xr[va]))
    elif arm!='M2_S': raise AssertionError(arm)
    Xtr=sparse.hstack(trb,format='csr',dtype=np.float32); Xva=sparse.hstack(vab,format='csr',dtype=np.float32)
    model=parent.make_classifier(cfg); model.fit(Xtr,y[tr]); score=np.asarray(model.decision_function(Xva),dtype=float).reshape(-1)
    return score,int(np.asarray(model.n_iter_).max())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--outer-fold',type=int,required=True); ap.add_argument('--index',type=Path,required=True); ap.add_argument('--folds',type=Path,required=True)
    ap.add_argument('--m0-session-features',type=Path,required=True); ap.add_argument('--historical-m2-oof',type=Path,required=True); ap.add_argument('--zt-cache',type=Path,required=True)
    ap.add_argument('--session-semantic',type=Path,required=True); ap.add_argument('--response-conditioning',type=Path,required=True); ap.add_argument('--config',type=Path,required=True)
    ap.add_argument('--parent-runner',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    parent=loadmod('parent',a.parent_runner); cfg=yaml.safe_load(a.config.read_text()); assert cfg['experiment_id']=='M2_SEM'
    assert parent.sha256_file(a.folds)==cfg['fold_sha256_required']; assert parent.sha256_file(a.historical_m2_oof)==cfg['historical_m2_oof_sha256_required']
    idx=pd.read_csv(a.index,usecols=['response_id','session_id','learning_objective_id','learning_objective','is_correct']); folds=pd.read_csv(a.folds); m0=pd.read_csv(a.m0_session_features)
    hist=pd.read_csv(a.historical_m2_oof); ss=pd.read_csv(a.session_semantic); rc=pd.read_csv(a.response_conditioning)
    ordinary=list(cfg['ordinary_covariates']); dim=int(cfg['external_semantic_resource']['vector_dimension'])
    df=idx.merge(folds,on='session_id',validate='many_to_one').merge(m0[['session_id',*ordinary]],on='session_id',validate='many_to_one').merge(hist[['response_id','m2_o_probability']],on='response_id',validate='one_to_one').merge(ss,on='session_id',validate='many_to_one').merge(rc,on=['response_id','session_id','learning_objective_id'],validate='one_to_one')
    sessions=sorted(df.session_id.astype(str).unique()); Xsess=sparse.load_npz(a.zt_cache).tocsr().astype(np.float32,copy=False)
    assert Xsess.shape==(len(sessions),int(cfg['hashed_representation']['n_features']))
    smap={s:i for i,s in enumerate(sessions)}; ridx=np.fromiter((smap[str(s)] for s in df.session_id),dtype=np.int32); Xt=Xsess[ridx].tocsr(); del Xsess
    vec=parent.make_vectorizer(cfg['hashed_representation']); ot=df[['learning_objective_id','learning_objective']].drop_duplicates('learning_objective_id').sort_values('learning_objective_id')
    Xou=vec.transform(ot.learning_objective.astype(str).tolist()).tocsr().astype(np.float32); omap={str(o):i for i,o in enumerate(ot.learning_objective_id)}; oidx=np.fromiter((omap[str(o)] for o in df.learning_objective_id),dtype=np.int32); Xo=Xou[oidx].tocsr()
    Xs=df[[f'z_s_{j:02d}' for j in range(dim)]].to_numpy(np.float32); Xr=df[[f'r_to_{j:02d}' for j in range(dim)]].to_numpy(np.float32); Xstruct=df[ordinary].to_numpy(float)
    y=df.is_correct.to_numpy(np.int8); groups=df.session_id.astype(str).to_numpy(); fa=df.fold.to_numpy(np.int16)
    outer=a.outer_fold; otr=np.flatnonzero(fa!=outer); ova=np.flatnonzero(fa==outer); assert not(set(groups[otr])&set(groups[ova]))
    max_iter=int(cfg['base_classifier']['max_iter']); icfg=cfg['inner_crossfit']; result={'outer_fold':outer,'arms':{}}
    for arm in ['M2_S','M2_SC']:
        t0=time.time(); oscore,onit=fit_score(parent,arm,Xt,Xo,Xs,Xr,Xstruct,y,otr,ova,cfg['base_classifier'])
        # Freeze and record the uncalibrated consequence before any calibrator is fitted.
        rp=sigmoid(oscore); raw_ll=float(log_loss(y[ova],rp))
        inner=np.full(len(otr),np.nan); nit=[]; splitter=StratifiedGroupKFold(n_splits=int(icfg['n_splits']),shuffle=bool(icfg['shuffle']),random_state=int(icfg['random_state'])); yo=y[otr]; go=groups[otr]
        for itr,iva in splitter.split(np.zeros(len(otr),np.int8),yo,groups=go):
            tr=otr[itr]; va=otr[iva]; assert not(set(groups[tr])&set(groups[va])); sc,ni=fit_score(parent,arm,Xt,Xo,Xs,Xr,Xstruct,y,tr,va,cfg['base_classifier']); inner[iva]=sc; nit.append(int(ni))
        assert np.isfinite(inner).all(); cal=parent_logistic(cfg['calibrator']); cal.fit(inner.reshape(-1,1),yo); cp=cal.predict_proba(oscore.reshape(-1,1))[:,1]
        result['arms'][arm]={'outer_n_iter':int(onit),'inner_n_iter':nit,'all_converged':bool(onit<max_iter and all(x<max_iter for x in nit)),'platt_slope':float(cal.coef_[0,0]),'platt_intercept':float(cal.intercept_[0]),'raw_log_loss':raw_ll,'calibrated_log_loss':float(log_loss(y[ova],cp)),'elapsed_seconds':time.time()-t0,'response_id':df.iloc[ova].response_id.astype(str).tolist(),'raw_score':oscore.tolist(),'raw_probability':rp.tolist(),'calibrated_probability':cp.tolist()}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,separators=(',',':'))+'\n'); print(json.dumps({'outer_fold':outer,'arms':{k:{kk:vv for kk,vv in v.items() if kk not in ('response_id','raw_score','raw_probability','calibrated_probability')} for k,v in result['arms'].items()}},indent=2))

def parent_logistic(c):
    from sklearn.linear_model import LogisticRegression
    return LogisticRegression(penalty=c['penalty'],solver=c['solver'],fit_intercept=bool(c['fit_intercept']),max_iter=int(c['max_iter']),tol=float(c['tol']),class_weight=c['class_weight'])
if __name__=='__main__': main()
