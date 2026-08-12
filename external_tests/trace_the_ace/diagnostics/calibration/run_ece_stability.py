#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np, pandas as pd, yaml


def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def ece(y,p,bins=10):
    y=np.asarray(y,float); p=np.asarray(p,float); bi=np.clip(np.digitize(p,np.linspace(0,1,bins+1)[1:-1]),0,bins-1); out=0.0
    for b in range(bins):
        m=bi==b
        if np.any(m): out += float(m.mean())*abs(float(p[m].mean())-float(y[m].mean()))
    return float(out)
def session_stats(session,y,p,bins):
    sid,inv=np.unique(np.asarray(session,str),return_inverse=True); bi=np.clip(np.digitize(p,np.linspace(0,1,bins+1)[1:-1]),0,bins-1); n=len(sid); cnt=np.zeros((n,bins),float); sp=np.zeros((n,bins),float); sy=np.zeros((n,bins),float); np.add.at(cnt,(inv,bi),1.0); np.add.at(sp,(inv,bi),p); np.add.at(sy,(inv,bi),y); return sid,cnt,sp,sy
def ece_from_stats(cnt,sp,sy):
    total=cnt.sum(1); pc=np.divide(sp,cnt,out=np.zeros_like(sp),where=cnt>0); yc=np.divide(sy,cnt,out=np.zeros_like(sy),where=cnt>0); return (cnt/total[:,None]*np.abs(pc-yc)).sum(1)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',type=Path,required=True); ap.add_argument('--m1-oof',type=Path,required=True); ap.add_argument('--m2-oof',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); cfg=yaml.safe_load(a.config.read_text())
    if sha(a.m1_oof)!=cfg['m1_cal_oof_sha256_required'] or sha(a.m2_oof)!=cfg['m2_sem_oof_sha256_required']: raise AssertionError('OOF identity mismatch')
    c1=cfg['m1_probability_column']; c2=cfg['m2_probability_column']; d1=pd.read_csv(a.m1_oof,usecols=['response_id','session_id','is_correct',c1]); d2=pd.read_csv(a.m2_oof,usecols=['response_id','session_id','is_correct',c2]); df=d1.merge(d2[['response_id',c2]],on='response_id',validate='one_to_one'); y=df.is_correct.to_numpy(float); p1=df[c1].to_numpy(float); p2=df[c2].to_numpy(float); bins=int(cfg['metric']['bins']); point=ece(y,p2,bins)-ece(y,p1,bins)
    sid,c1n,p1s,y1s=session_stats(df.session_id,y,p1,bins); sid2,c2n,p2s,y2s=session_stats(df.session_id,y,p2,bins); assert np.array_equal(sid,sid2); assert np.allclose(y1s.sum(1),y2s.sum(1)); reps=int(cfg['bootstrap']['replicates']); rng=np.random.default_rng(int(cfg['bootstrap']['seed'])); vals=np.empty(reps,float); n=len(sid); done=0
    while done<reps:
        k=min(20,reps-done); draw=rng.integers(0,n,size=(k,n)); A1n=c1n[draw].sum(1); A1p=p1s[draw].sum(1); A1y=y1s[draw].sum(1); A2n=c2n[draw].sum(1); A2p=p2s[draw].sum(1); A2y=y2s[draw].sum(1); vals[done:done+k]=ece_from_stats(A2n,A2p,A2y)-ece_from_stats(A1n,A1p,A1y); done+=k
    lo,hi=np.quantile(vals,[.025,.975]); status='STABLE_DEGRADATION' if point>0 and lo>0 else ('STABLE_NONDEGRADATION' if point<=0 and hi<=0 else 'NOT_STABLY_IDENTIFIED'); rec={'schema_version':1,'experiment_id':'CAL_ECE_STABILITY','m1_ece_10':ece(y,p1,bins),'m2_s_platt_ece_10':ece(y,p2,bins),'point_delta_m2_minus_m1':float(point),'bootstrap_ci95':[float(lo),float(hi)],'replicates':reps,'seed':int(cfg['bootstrap']['seed']),'clusters':n,'diagnosis':status,'authority':{'historical_gate_changed':False,'mature_calibration_authority':False,'CCA_derived_feature_authority':False}}; a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
