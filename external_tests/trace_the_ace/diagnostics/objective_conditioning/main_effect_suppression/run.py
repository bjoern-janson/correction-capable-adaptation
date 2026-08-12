#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path
import numpy as np, pandas as pd, yaml
from scipy import sparse
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import log_loss, roc_auc_score


def loadmod(name,path):
    s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def sigmoid(x):
    x=np.asarray(x,float); out=np.empty_like(x); pos=x>=0; out[pos]=1/(1+np.exp(-x[pos])); ex=np.exp(x[~pos]); out[~pos]=ex/(1+ex); return out

def per_loss(y,p):
    p=np.clip(np.asarray(p,float),1e-15,1-1e-15); y=np.asarray(y,float); return -(y*np.log(p)+(1-y)*np.log(1-p))

def boot(g,delta,reps,seed):
    t=pd.DataFrame({'session_id':g,'delta':delta}); a=t.groupby('session_id',sort=True).delta.agg(['sum','count']); sums=a['sum'].to_numpy(float); counts=a['count'].to_numpy(float); n=len(a); rng=np.random.default_rng(seed); out=np.empty(reps); done=0
    while done<reps:
        k=min(100,reps-done); draw=rng.integers(0,n,size=(k,n)); out[done:done+k]=sums[draw].sum(1)/counts[draw].sum(1); done+=k
    q=np.quantile(out,[.025,.975]); return {'point':float(np.mean(delta)),'ci95_lower':float(q[0]),'ci95_upper':float(q[1]),'clusters':int(n),'replicates':int(reps),'seed':int(seed)}

def struct(train,val):
    tr=train.copy(); va=val.copy(); med=np.nanmedian(tr,axis=0); it=np.where(np.isnan(tr)); iv=np.where(np.isnan(va)); tr[it]=med[it[1]]; va[iv]=med[iv[1]]; sc=StandardScaler(); return sc.fit_transform(tr).astype(np.float32),sc.transform(va).astype(np.float32)

def centered_r(R,obj,tr,va):
    means={}
    for o in np.unique(obj[tr]): means[o]=R[tr][obj[tr]==o].mean(0,dtype=np.float64).astype(np.float32)
    missing=set(obj[va])-set(means)
    if missing: raise AssertionError(f'validation objectives without training support: {len(missing)}')
    ctr=np.vstack([R[i]-means[obj[i]] for i in tr]).astype(np.float32); cva=np.vstack([R[i]-means[obj[i]] for i in va]).astype(np.float32)
    for o in np.unique(obj[tr]):
        m=obj[tr]==o
        if np.max(np.abs(ctr[m].mean(0,dtype=np.float64)))>2e-6: raise AssertionError('centering failure')
    return ctr,cva

def fit(parent,cfg,blocks_tr,blocks_va,ytr):
    Xtr=sparse.hstack(blocks_tr,format='csr',dtype=np.float32); Xva=sparse.hstack(blocks_va,format='csr',dtype=np.float32); m=parent.make_classifier(cfg); m.fit(Xtr,ytr); s=np.asarray(m.decision_function(Xva),float); return s,int(np.asarray(m.n_iter_).max())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',type=Path,required=True); ap.add_argument('--index',type=Path,required=True); ap.add_argument('--folds',type=Path,required=True); ap.add_argument('--m0-session-features',type=Path,required=True); ap.add_argument('--zt-cache',type=Path,required=True); ap.add_argument('--session-semantic',type=Path,required=True); ap.add_argument('--response-conditioning',type=Path,required=True); ap.add_argument('--eligible-objectives',type=Path,required=True); ap.add_argument('--parent-runner',type=Path,required=True); ap.add_argument('--output-dir',type=Path,required=True); a=ap.parse_args()
    cfg=yaml.safe_load(a.config.read_text()); assert cfg['experiment_id']=='M2_D_MAIN' and not cfg['cca_derived_features_allowed'] and not cfg['new_conditioning_operator_authorized']; parent=loadmod('parent',a.parent_runner)
    checks=[(a.index,cfg['index_sha256_required']),(a.folds,cfg['fold_sha256_required']),(a.zt_cache,cfg['zt_cache_sha256_required']),(a.session_semantic,cfg['session_semantic_sha256_required']),(a.response_conditioning,cfg['response_conditioning_sha256_required']),(a.eligible_objectives,cfg['eligible_objectives_sha256_required'])]
    for p,h in checks:
        if sha(p)!=h: raise AssertionError(f'identity mismatch: {p}')
    idx=pd.read_csv(a.index,usecols=['response_id','session_id','learning_objective_id','learning_objective','is_correct']); fd=pd.read_csv(a.folds); m0=pd.read_csv(a.m0_session_features); ss=pd.read_csv(a.session_semantic); rc=pd.read_csv(a.response_conditioning); ordc=list(cfg['ordinary_covariates'])
    df=idx.merge(fd,on='session_id',validate='many_to_one').merge(m0[['session_id',*ordc]],on='session_id',validate='many_to_one').merge(ss,on='session_id',validate='many_to_one').merge(rc,on=['response_id','session_id','learning_objective_id'],validate='one_to_one')
    elig=set(a.eligible_objectives.read_text().splitlines()); keep=df.learning_objective_id.astype(str).isin(elig).to_numpy(); df=df.loc[keep].reset_index(drop=True)
    if len(df)!=int(cfg['eligible_rows']) or df.session_id.nunique()!=int(cfg['eligible_sessions']) or df.learning_objective_id.nunique()!=int(cfg['eligible_objectives']): raise AssertionError('eligible cohort mismatch')
    sessions=sorted(idx.session_id.astype(str).unique()); Z=sparse.load_npz(a.zt_cache).tocsr().astype(np.float32,copy=False); sm={s:i for i,s in enumerate(sessions)}; ri=np.fromiter((sm[str(x)] for x in df.session_id),dtype=np.int32); Xt=Z[ri].tocsr(); del Z
    vec=parent.make_vectorizer(cfg['hashed_representation']); ot=df[['learning_objective_id','learning_objective']].drop_duplicates('learning_objective_id').sort_values('learning_objective_id'); U=vec.transform(ot.learning_objective.astype(str).tolist()).tocsr().astype(np.float32); om={str(o):i for i,o in enumerate(ot.learning_objective_id)}; oi=np.fromiter((om[str(o)] for o in df.learning_objective_id),dtype=np.int32); Xo=U[oi].tocsr()
    Xs=df[[c for c in df.columns if c.startswith('z_s_')]].to_numpy(np.float32); R=df[[c for c in df.columns if c.startswith('r_to_')]].to_numpy(np.float32); Xq=df[ordc].to_numpy(float); y=df.is_correct.to_numpy(np.int8); g=df.session_id.astype(str).to_numpy(); obj=df.learning_objective_id.astype(str).to_numpy(); fa=df.fold.to_numpy(int)
    arms=['B0','C0','B1','C1']; pred={k:np.full(len(df),np.nan) for k in arms}; iters={k:[] for k in arms}; maxit=int(cfg['base_classifier']['max_iter'])
    for outer in range(5):
        tr=np.flatnonzero(fa!=outer); va=np.flatnonzero(fa==outer); assert not(set(g[tr])&set(g[va])); qs,qv=struct(Xq[tr],Xq[va]); cr_tr,cr_va=centered_r(R,obj,tr,va)
        base0tr=[Xt[tr],sparse.csr_matrix(qs),sparse.csr_matrix(Xs[tr])]; base0va=[Xt[va],sparse.csr_matrix(qv),sparse.csr_matrix(Xs[va])]; base1tr=[Xt[tr],Xo[tr],sparse.csr_matrix(qs),sparse.csr_matrix(Xs[tr])]; base1va=[Xt[va],Xo[va],sparse.csr_matrix(qv),sparse.csr_matrix(Xs[va])]
        specs={'B0':(base0tr,base0va),'C0':(base0tr+[sparse.csr_matrix(cr_tr)],base0va+[sparse.csr_matrix(cr_va)]),'B1':(base1tr,base1va),'C1':(base1tr+[sparse.csr_matrix(cr_tr)],base1va+[sparse.csr_matrix(cr_va)])}
        for arm in arms:
            s,ni=fit(parent,cfg['base_classifier'],specs[arm][0],specs[arm][1],y[tr]); pred[arm][va]=sigmoid(s); iters[arm].append(int(ni)); print(json.dumps({'fold':outer,'arm':arm,'n_iter':ni,'rows':len(va)}),flush=True)
    if any(not np.isfinite(pred[k]).all() for k in arms): raise AssertionError('incomplete OOF')
    loss={k:per_loss(y,pred[k]) for k in arms}; d0=loss['C0']-loss['B0']; d1=loss['C1']-loss['B1']; psi=d0-d1; u=cfg['uncertainty']; b0=boot(g,d0,int(u['replicates']),int(u['seed_delta_no_main'])); b1=boot(g,d1,int(u['replicates']),int(u['seed_delta_with_main'])); bp=boot(g,psi,int(u['replicates']),int(u['seed_suppression_difference']))
    support=bool(b0['point']<0 and b0['ci95_upper']<0 and bp['point']<0 and bp['ci95_upper']<0); against=bool(b0['ci95_lower']>=0 and bp['ci95_lower']>=0); status='SUPPORT' if support else ('WEIGH_AGAINST' if against else 'UNRESOLVED'); conv=all(n<maxit for a0 in arms for n in iters[a0])
    metrics={k:{'log_loss':float(log_loss(y,pred[k])),'auc':float(roc_auc_score(y,pred[k]))} for k in arms}; rec={'schema_version':1,'experiment_id':'M2_D_MAIN','implementation':{'all_base_models_converged':conv,'fit_count':20,'max_n_iter':max(max(v) for v in iters.values()),'iters':iters},'metrics':metrics,'delta_no_main':b0,'delta_with_main':b1,'suppression_difference':bp,'D_main_local_diagnostic':status,'authority':{'broad_H_O':'OPEN','new_conditioning_operator_authorized':False,'CCA_derived_feature_authority':False}}
    out=a.output_dir; out.mkdir(parents=True,exist_ok=True); od=df[['response_id','session_id','learning_objective_id','is_correct']].copy();
    for k in arms: od[f'{k.lower()}_raw_probability']=pred[k]
    op=out/'oof_predictions.csv'; od.to_csv(op,index=False,lineterminator='\n'); rec['artifacts']={'oof_sha256':sha(op)}; rp=out/'m2_d_main_record.json'; rp.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
