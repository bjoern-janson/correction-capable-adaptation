#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np, pandas as pd, yaml
from scipy.optimize import minimize
from sklearn.metrics import brier_score_loss, log_loss


def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def sigmoid(x):
    x=np.asarray(x,float); out=np.empty_like(x); pos=x>=0; out[pos]=1/(1+np.exp(-x[pos])); ex=np.exp(x[~pos]); out[~pos]=ex/(1+ex); return out
def calibration_summary(y,p,bins=10):
    p=np.asarray(p,float); y=np.asarray(y,float); edges=np.linspace(0,1,bins+1); idx=np.clip(np.digitize(p,edges[1:-1],right=False),0,bins-1); ece=0.0
    for b in range(bins):
        m=idx==b
        if np.any(m): ece += float(m.mean())*abs(float(p[m].mean())-float(y[m].mean()))
    return {'mean_probability':float(p.mean()),'observed_rate':float(y.mean()),'brier_score':float(brier_score_loss(y,p)),'ece_10_equal_width':float(ece),'absolute_mean_probability_bias':abs(float(p.mean()-y.mean()))}
def per_row_loss(y,p):
    p=np.clip(np.asarray(p,float),1e-15,1-1e-15); y=np.asarray(y,float); return -(y*np.log(p)+(1-y)*np.log(1-p))
def bootstrap(session_ids,y,cand,base,reps,seed):
    tmp=pd.DataFrame({'session_id':session_ids,'delta':per_row_loss(y,cand)-per_row_loss(y,base)}); agg=tmp.groupby('session_id',sort=True).delta.agg(['sum','count']); sums=agg['sum'].to_numpy(float); counts=agg['count'].to_numpy(float); n=len(agg); rng=np.random.default_rng(seed); out=np.empty(reps,float); done=0
    while done<reps:
        k=min(100,reps-done); draw=rng.integers(0,n,size=(k,n)); out[done:done+k]=sums[draw].sum(1)/counts[draw].sum(1); done+=k
    q=np.quantile(out,[.025,.975]); return {'point_delta_log_loss':float((per_row_loss(y,cand)-per_row_loss(y,base)).mean()),'ci95_lower':float(q[0]),'ci95_upper':float(q[1]),'replicates':int(reps),'seed':int(seed),'clusters':int(n)}
def verify_manifest(score_dir,manifest,required):
    if sha256(manifest)!=required: raise AssertionError('manifest hash mismatch')
    lines=manifest.read_text().splitlines()
    if len(lines)!=30: raise AssertionError('expected 30 score artifacts')
    for line in lines:
        name,size_s,h=line.split('\t'); p=score_dir/name
        if p.stat().st_size!=int(size_s) or sha256(p)!=h: raise AssertionError(f'score artifact mismatch: {name}')
def beta_fit(raw_score,y,cfg):
    eps=float(cfg['raw_probability_clip']); p0=np.clip(sigmoid(raw_score),eps,1-eps); X=np.column_stack([np.log(p0),-np.log1p(-p0),np.ones(len(p0))]); y=np.asarray(y,float)
    def fg(t):
        z=X@t; pr=sigmoid(z); f=float(np.sum(np.logaddexp(0.0,z)-y*z)); g=X.T@(pr-y); return f,g
    x0=np.asarray(cfg['initial'],float); bounds=[(float(cfg['a_lower_bound']),None),(float(cfg['b_lower_bound']),None),(None,None)]; options={'maxiter':int(cfg['maxiter']),'ftol':float(cfg['ftol']),'gtol':float(cfg['gtol'])}; res=minimize(lambda t:fg(t)[0],x0,jac=lambda t:fg(t)[1],method=cfg['optimizer'],bounds=bounds,options=options)
    return res
def beta_predict(raw_score,coef,cfg):
    eps=float(cfg['raw_probability_clip']); p0=np.clip(sigmoid(raw_score),eps,1-eps); z=coef[0]*np.log(p0)-coef[1]*np.log1p(-p0)+coef[2]; return sigmoid(z)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',type=Path,required=True); ap.add_argument('--index',type=Path,required=True); ap.add_argument('--folds',type=Path,required=True); ap.add_argument('--score-dir',type=Path,required=True); ap.add_argument('--score-manifest',type=Path,required=True); ap.add_argument('--parent-oof',type=Path,required=True); ap.add_argument('--output-dir',type=Path,required=True); a=ap.parse_args(); cfg=yaml.safe_load(a.config.read_text()); assert cfg['experiment_id']=='M_MATURE_BETA_CAL' and not cfg['cca_derived_features_allowed'] and not cfg['base_model_retraining_allowed']
    if sha256(a.index)!=cfg['index_sha256_required'] or sha256(a.folds)!=cfg['fold_sha256_required']:
        raise AssertionError('index/fold identity mismatch')
    verify_manifest(a.score_dir,a.score_manifest,cfg['m2_s_score_manifest_sha256_required'])
    if sha256(a.parent_oof)!=cfg['parent_m2_sem_oof_sha256_required']: raise AssertionError('parent OOF hash mismatch')
    idx=pd.read_csv(a.index,usecols=['response_id','session_id','is_correct']); folds=pd.read_csv(a.folds); df=idx.merge(folds,on='session_id',validate='many_to_one'); y=df.is_correct.to_numpy(np.int8); g=df.session_id.astype(str).to_numpy(); fa=df.fold.to_numpy(int)
    po=pd.read_csv(a.parent_oof,usecols=['response_id','m2_s_cal_probability']); po=idx[['response_id']].merge(po,on='response_id',validate='one_to_one'); p_parent=po.m2_s_cal_probability.to_numpy(float); p_beta=np.full(len(df),np.nan,float); fold_records=[]; bc=cfg['beta_calibrator']
    for outer in range(5):
        otr=np.flatnonzero(fa!=outer); ova=np.flatnonzero(fa==outer); oz=np.load(a.score_dir/f'M2_S_fold{outer}_outer.npz'); pos={int(ix):j for j,ix in enumerate(oz['global_index'])}; os=np.asarray([oz['score'][pos[int(ix)]] for ix in ova],float); inner=np.full(len(df),np.nan,float); seen=set()
        for k in range(5):
            z=np.load(a.score_dir/f'M2_S_fold{outer}_inner{k}.npz'); gi=np.asarray(z['global_index'],int)
            if seen.intersection(map(int,gi)): raise AssertionError('inner overlap')
            seen.update(map(int,gi)); inner[gi]=np.asarray(z['score'],float)
        if seen!=set(map(int,otr)) or not np.isfinite(inner[otr]).all(): raise AssertionError('inner coverage mismatch')
        res=beta_fit(inner[otr],y[otr],bc); coef=np.asarray(res.x,float); pred=beta_predict(os,coef,bc); p_beta[ova]=pred; cm=calibration_summary(y[ova],pred); fold_records.append({'fold':outer,'optimizer_success':bool(res.success),'optimizer_status':int(res.status),'optimizer_message':str(res.message),'iterations':int(res.nit),'a':float(coef[0]),'b':float(coef[1]),'c':float(coef[2]),'log_loss':float(log_loss(y[ova],pred)),'brier':cm['brier_score'],'ece_10':cm['ece_10_equal_width']})
    if not np.isfinite(p_beta).all(): raise AssertionError('incomplete beta OOF')
    mb=calibration_summary(y,p_beta); mp=calibration_summary(y,p_parent); unc=bootstrap(g,y,p_beta,p_parent,int(cfg['uncertainty']['replicates']),int(cfg['uncertainty']['seed'])); gates={'optimizer_success_all_outer_folds':all(r['optimizer_success'] for r in fold_records),'ece_10_not_worse_than_historical_m1_cal':mb['ece_10_equal_width']<=float(cfg['historical_m1_cal_reference']['ece_10']),'log_loss_strictly_better_than_parent_platt':float(log_loss(y,p_beta))<float(cfg['parent_platt_metrics']['log_loss']),'log_loss_bootstrap_ci95_upper_below_zero':unc['ci95_upper']<0,'brier_not_worse_than_parent_platt':mb['brier_score']<=float(cfg['parent_platt_metrics']['brier']),'absolute_mean_probability_bias_not_worse_than_historical_m1_cal':mb['absolute_mean_probability_bias']<=float(cfg['historical_m1_cal_reference']['absolute_mean_probability_bias'])}; passed=all(gates.values()); rec={'schema_version':1,'experiment_id':'M_MATURE_BETA_CAL','status':'DIAGNOSED_PASS' if passed else 'DIAGNOSED_UNRESOLVED','parent':'M2_S_PLATT','successor':'M2_S_BETA','parent_metrics':mp|{'log_loss':float(log_loss(y,p_parent))},'successor_metrics':mb|{'log_loss':float(log_loss(y,p_beta))},'uncertainty':unc,'gates':gates,'all_gates_pass':passed,'folds':fold_records,'authority':{'mature_non_CCA_probability_treatment':bool(passed),'CCA_derived_feature_authority':False}}
    out=a.output_dir; out.mkdir(parents=True,exist_ok=True); oof=idx[['response_id','session_id','is_correct']].copy(); oof['m2_s_platt_probability']=p_parent; oof['mature_beta_probability']=p_beta; op=out/'oof_predictions.csv'; oof.to_csv(op,index=False,lineterminator='\n'); rec['artifacts']={'oof_sha256':sha256(op)}; rp=out/'mature_beta_record.json'; rp.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
