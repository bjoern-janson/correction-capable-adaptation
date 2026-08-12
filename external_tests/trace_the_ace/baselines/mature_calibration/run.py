#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np, pandas as pd, yaml
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import log_loss, brier_score_loss


def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def calibration_summary(y,p,bins=10):
    p=np.asarray(p,float); y=np.asarray(y,float)
    edges=np.linspace(0,1,bins+1); idx=np.clip(np.digitize(p,edges[1:-1],right=False),0,bins-1); ece=0.0
    for b in range(bins):
        m=idx==b
        if np.any(m): ece += float(m.mean())*abs(float(p[m].mean())-float(y[m].mean()))
    return {'mean_probability':float(p.mean()),'observed_rate':float(y.mean()),'brier_score':float(brier_score_loss(y,p)),'ece_10_equal_width':float(ece),'absolute_mean_probability_bias':abs(float(p.mean()-y.mean()))}

def per_row_loss(y,p):
    p=np.clip(np.asarray(p,float),1e-15,1-1e-15); y=np.asarray(y,float); return -(y*np.log(p)+(1-y)*np.log(1-p))

def bootstrap(session_ids,cand,base,reps,seed):
    tmp=pd.DataFrame({'session_id':session_ids,'delta':per_row_loss(cand[0],cand[1])-per_row_loss(base[0],base[1])})
    agg=tmp.groupby('session_id',sort=True).delta.agg(['sum','count']); sums=agg['sum'].to_numpy(float); counts=agg['count'].to_numpy(float); n=len(agg)
    rng=np.random.default_rng(seed); out=np.empty(reps,float); done=0
    while done<reps:
        k=min(100,reps-done); draw=rng.integers(0,n,size=(k,n)); out[done:done+k]=sums[draw].sum(1)/counts[draw].sum(1); done+=k
    q=np.quantile(out,[.025,.975]); d=per_row_loss(cand[0],cand[1])-per_row_loss(base[0],base[1])
    return {'point_delta_log_loss':float(d.mean()),'ci95_lower':float(q[0]),'ci95_upper':float(q[1]),'replicates':int(reps),'seed':int(seed),'clusters':int(n)}

def verify_manifest(score_dir:Path, manifest:Path, required:str):
    if sha256(manifest)!=required: raise AssertionError('manifest hash mismatch')
    lines=[]
    for line in manifest.read_text().splitlines():
        name,size_s,h=line.split('\t'); p=score_dir/name
        if p.stat().st_size!=int(size_s) or sha256(p)!=h: raise AssertionError(f'score artifact mismatch: {name}')
        lines.append(name)
    if len(lines)!=30: raise AssertionError('expected 30 score artifacts')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',type=Path,required=True); ap.add_argument('--index',type=Path,required=True); ap.add_argument('--folds',type=Path,required=True); ap.add_argument('--score-dir',type=Path,required=True); ap.add_argument('--score-manifest',type=Path,required=True); ap.add_argument('--parent-oof',type=Path,required=True); ap.add_argument('--output-dir',type=Path,required=True); a=ap.parse_args()
    cfg=yaml.safe_load(a.config.read_text()); assert cfg['experiment_id']=='M_MATURE_CAL'; assert not cfg['cca_derived_features_allowed']; assert not cfg['base_model_retraining_allowed']
    if sha256(a.index)!=cfg['index_sha256_required'] or sha256(a.folds)!=cfg['fold_sha256_required']: raise AssertionError('index/fold identity mismatch')
    verify_manifest(a.score_dir,a.score_manifest,cfg['m2_s_score_manifest_sha256_required'])
    if sha256(a.parent_oof)!=cfg['parent_m2_sem_oof_sha256_required']: raise AssertionError('parent OOF hash mismatch')
    idx=pd.read_csv(a.index,usecols=['response_id','session_id','is_correct']); folds=pd.read_csv(a.folds); df=idx.merge(folds,on='session_id',validate='many_to_one'); y=df.is_correct.to_numpy(np.int8); g=df.session_id.astype(str).to_numpy(); fold_arr=df.fold.to_numpy(int)
    parent=pd.read_csv(a.parent_oof,usecols=['response_id','m2_s_cal_probability']); parent=idx[['response_id']].merge(parent,on='response_id',validate='one_to_one'); p_parent=parent.m2_s_cal_probability.to_numpy(float)
    p_iso=np.full(len(df),np.nan,float); fold_records=[]; c=cfg['successor_calibrator']
    for outer in range(5):
        otr=np.flatnonzero(fold_arr!=outer); ova=np.flatnonzero(fold_arr==outer)
        oz=np.load(a.score_dir/f'M2_S_fold{outer}_outer.npz'); assert np.array_equal(np.sort(oz['global_index']),np.sort(ova)); oscore=np.asarray(oz['score'],float); pos={int(ix):j for j,ix in enumerate(oz['global_index'])}; oscore=np.asarray([oscore[pos[int(ix)]] for ix in ova],float)
        inner_score=np.full(len(df),np.nan,float); seen=set()
        for k in range(5):
            z=np.load(a.score_dir/f'M2_S_fold{outer}_inner{k}.npz'); gi=np.asarray(z['global_index'],int)
            if seen.intersection(map(int,gi)): raise AssertionError('inner overlap')
            seen.update(map(int,gi)); inner_score[gi]=np.asarray(z['score'],float)
        if seen!=set(map(int,otr)) or not np.isfinite(inner_score[otr]).all(): raise AssertionError('inner coverage mismatch')
        iso=IsotonicRegression(y_min=float(c['y_min']),y_max=float(c['y_max']),increasing=bool(c['increasing']),out_of_bounds=c['out_of_bounds']); iso.fit(inner_score[otr],y[otr]); pred=np.asarray(iso.predict(oscore),float); p_iso[ova]=pred
        cm=calibration_summary(y[ova],pred); fold_records.append({'fold':outer,'rows':int(len(ova)),'thresholds':int(len(iso.X_thresholds_)),'log_loss':float(log_loss(y[ova],pred)),'brier':cm['brier_score'],'ece_10':cm['ece_10_equal_width']})
    if not np.isfinite(p_iso).all(): raise AssertionError('incomplete OOF')
    m_iso=calibration_summary(y,p_iso); m_parent=calibration_summary(y,p_parent); unc=bootstrap(g,(y,p_iso),(y,p_parent),int(cfg['uncertainty']['replicates']),int(cfg['uncertainty']['seed']))
    gates={'ece_10_not_worse_than_historical_m1_cal':m_iso['ece_10_equal_width']<=float(cfg['historical_m1_cal_reference']['ece_10']),'log_loss_strictly_better_than_parent_platt':float(log_loss(y,p_iso))<float(cfg['parent_platt_metrics']['log_loss']),'log_loss_bootstrap_ci95_upper_below_zero':unc['ci95_upper']<0,'brier_not_worse_than_parent_platt':m_iso['brier_score']<=float(cfg['parent_platt_metrics']['brier']),'absolute_mean_probability_bias_not_worse_than_historical_m1_cal':m_iso['absolute_mean_probability_bias']<=float(cfg['historical_m1_cal_reference']['absolute_mean_probability_bias'])}
    passed=all(gates.values()); rec={'schema_version':1,'experiment_id':'M_MATURE_CAL','status':'DIAGNOSED_PASS' if passed else 'DIAGNOSED_UNRESOLVED','parent':'M2_S_PLATT','successor':'M2_S_ISOTONIC','parent_metrics':m_parent|{'log_loss':float(log_loss(y,p_parent))},'successor_metrics':m_iso|{'log_loss':float(log_loss(y,p_iso))},'uncertainty':unc,'gates':gates,'all_gates_pass':passed,'folds':fold_records,'authority':{'mature_non_CCA_probability_treatment':bool(passed),'CCA_derived_feature_authority':False}}
    out=a.output_dir; out.mkdir(parents=True,exist_ok=True); oof=idx[['response_id','session_id','is_correct']].copy(); oof['m2_s_platt_probability']=p_parent; oof['mature_isotonic_probability']=p_iso; op=out/'oof_predictions.csv'; oof.to_csv(op,index=False,lineterminator='\n'); rec['artifacts']={'oof_sha256':sha256(op)}; rp=out/'mature_cal_record.json'; rp.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); rec['artifacts']['record_sha256_pre_self_hash']=sha256(rp); rp.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
