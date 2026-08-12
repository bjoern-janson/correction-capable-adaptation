#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import pandas as pd
import yaml


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20), b''):
            h.update(b)
    return h.hexdigest()


def ece_from_aggregates(counts, psums, ysums):
    counts=np.asarray(counts,float); psums=np.asarray(psums,float); ysums=np.asarray(ysums,float)
    n=counts.sum()
    mask=counts>0
    if n<=0: raise AssertionError('empty sample')
    return float(np.sum((counts[mask]/n)*np.abs(psums[mask]/counts[mask]-ysums[mask]/counts[mask])))


def session_bin_aggregates(session_codes, p, y, n_sessions, bins=10):
    p=np.asarray(p,float); y=np.asarray(y,float); s=np.asarray(session_codes,int)
    b=np.clip(np.digitize(p,np.linspace(0,1,bins+1)[1:-1],right=False),0,bins-1)
    key=s*bins+b
    size=n_sessions*bins
    cnt=np.bincount(key,minlength=size).reshape(n_sessions,bins).astype(float)
    ps=np.bincount(key,weights=p,minlength=size).reshape(n_sessions,bins).astype(float)
    ys=np.bincount(key,weights=y,minlength=size).reshape(n_sessions,bins).astype(float)
    return cnt,ps,ys


def bootstrap_ece_diff(cnt_r,ps_r,ys_r,cnt_c,ps_c,ys_c,reps,seed,batch=40):
    S=cnt_r.shape[0]; rng=np.random.default_rng(seed); out=np.empty(reps,float); done=0
    while done<reps:
        k=min(batch,reps-done)
        W=np.zeros((k,S),dtype=np.float32)
        draws=rng.integers(0,S,size=(k,S),dtype=np.int32)
        for j in range(k): W[j]=np.bincount(draws[j],minlength=S)
        for j in range(k):
            w=W[j]
            cr=w@cnt_r; pr=w@ps_r; yr=w@ys_r
            cc=w@cnt_c; pc=w@ps_c; yc=w@ys_c
            out[done+j]=ece_from_aggregates(cc,pc,yc)-ece_from_aggregates(cr,pr,yr)
        done+=k
    q=np.quantile(out,[.025,.975])
    return float(q[0]),float(q[1])


def synthetic_suite(session_sizes, eps, seeds, reps, seed_offset):
    session_sizes=np.asarray(session_sizes,int); S=len(session_sizes)
    scenarios={'S0':0.0,'S1':0.5*eps,'S2':2.0*eps}
    records=[]
    for seed in seeds:
        rng=np.random.default_rng(seed)
        pref=0.1+0.8*rng.beta(7.0,3.0,size=S)
        ysum=rng.binomial(session_sizes,pref)
        bref=np.clip(np.digitize(pref,np.linspace(0,1,11)[1:-1],right=False),0,9)
        cnt_r=np.zeros((S,10),float); ps_r=np.zeros((S,10),float); ys_r=np.zeros((S,10),float)
        rows=np.arange(S)
        cnt_r[rows,bref]=session_sizes; ps_r[rows,bref]=session_sizes*pref; ys_r[rows,bref]=ysum
        ece_r=ece_from_aggregates(cnt_r.sum(0),ps_r.sum(0),ys_r.sum(0))
        for name,delta in scenarios.items():
            pc=pref+delta
            if not (np.all(pc>0) and np.all(pc<1)): raise AssertionError('synthetic candidate outside unit interval')
            bc=np.clip(np.digitize(pc,np.linspace(0,1,11)[1:-1],right=False),0,9)
            cnt_c=np.zeros((S,10),float); ps_c=np.zeros((S,10),float); ys_c=np.zeros((S,10),float)
            cnt_c[rows,bc]=session_sizes; ps_c[rows,bc]=session_sizes*pc; ys_c[rows,bc]=ysum
            ece_c=ece_from_aggregates(cnt_c.sum(0),ps_c.sum(0),ys_c.sum(0))
            lo,hi=bootstrap_ece_diff(cnt_r,ps_r,ys_r,cnt_c,ps_c,ys_c,reps,seed_offset+seed*10+{'S0':0,'S1':1,'S2':2}[name])
            records.append({'dataset_seed':int(seed),'scenario':name,'delta_probability':float(delta),'ece_reference':ece_r,'ece_candidate':ece_c,'point_delta_ece':ece_c-ece_r,'ci95_lower':lo,'ci95_upper':hi,'passes_ece_noninferiority':bool(hi<eps)})
    counts={}
    for name in scenarios:
        rr=[r for r in records if r['scenario']==name]
        counts[name]={'pass':sum(r['passes_ece_noninferiority'] for r in rr),'fail':sum(not r['passes_ece_noninferiority'] for r in rr),'n':len(rr)}
    return records,counts


def bootstrap_linear_delta(session_codes, row_delta, reps, seed, batch=100):
    s=np.asarray(session_codes,int); d=np.asarray(row_delta,float); S=int(s.max())+1
    sums=np.bincount(s,weights=d,minlength=S); cnt=np.bincount(s,minlength=S).astype(float)
    rng=np.random.default_rng(seed); out=np.empty(reps,float); done=0
    while done<reps:
        k=min(batch,reps-done)
        draws=rng.integers(0,S,size=(k,S),dtype=np.int32)
        for j in range(k):
            w=np.bincount(draws[j],minlength=S)
            out[done+j]=(w@sums)/(w@cnt)
        done+=k
    q=np.quantile(out,[.025,.975]); return float(q[0]),float(q[1])


def bootstrap_bias_diff(session_codes,pref,pcand,y,reps,seed,batch=100):
    s=np.asarray(session_codes,int); S=int(s.max())+1
    cnt=np.bincount(s,minlength=S).astype(float)
    yr=np.bincount(s,weights=y,minlength=S)
    sr=np.bincount(s,weights=pref,minlength=S)
    sc=np.bincount(s,weights=pcand,minlength=S)
    rng=np.random.default_rng(seed); out=np.empty(reps,float); done=0
    while done<reps:
        k=min(batch,reps-done); draws=rng.integers(0,S,size=(k,S),dtype=np.int32)
        for j in range(k):
            w=np.bincount(draws[j],minlength=S); n=w@cnt; yy=w@yr
            br=abs((w@sr-yy)/n); bc=abs((w@sc-yy)/n); out[done+j]=bc-br
        done+=k
    q=np.quantile(out,[.025,.975]); return float(q[0]),float(q[1])


def historical_adjudication(index,ref_oof,cand_oof,cfg):
    idx=pd.read_csv(index,usecols=['response_id','session_id','is_correct'])
    r=pd.read_csv(ref_oof,usecols=['response_id','m1_cal_probability'])
    c=pd.read_csv(cand_oof,usecols=['response_id','m2_s_cal_probability'])
    df=idx.merge(r,on='response_id',validate='one_to_one').merge(c,on='response_id',validate='one_to_one')
    cats=pd.Categorical(df.session_id.astype(str),categories=sorted(df.session_id.astype(str).unique()))
    s=cats.codes.astype(int); S=len(cats.categories)
    y=df.is_correct.to_numpy(float); pr=df.m1_cal_probability.to_numpy(float); pc=df.m2_s_cal_probability.to_numpy(float)
    tiny=1e-15; prc=np.clip(pr,tiny,1-tiny); pcc=np.clip(pc,tiny,1-tiny)
    llr=-(y*np.log(prc)+(1-y)*np.log1p(-prc)); llc=-(y*np.log(pcc)+(1-y)*np.log1p(-pcc))
    brr=(pr-y)**2; brc=(pc-y)**2
    cr,psr,ysr=session_bin_aggregates(s,pr,y,S,10); cc,psc,ysc=session_bin_aggregates(s,pc,y,S,10)
    ecer=ece_from_aggregates(cr.sum(0),psr.sum(0),ysr.sum(0)); ecec=ece_from_aggregates(cc.sum(0),psc.sum(0),ysc.sum(0))
    biasr=abs(float(pr.mean()-y.mean())); biasc=abs(float(pc.mean()-y.mean()))
    reps=int(cfg['bootstrap']['historical_replicates']); seeds=cfg['bootstrap']['seeds']
    ll_ci=bootstrap_linear_delta(s,llc-llr,reps,int(seeds['delta_log_loss']))
    br_ci=bootstrap_linear_delta(s,brc-brr,reps,int(seeds['delta_brier']))
    ece_ci=bootstrap_ece_diff(cr,psr,ysr,cc,psc,ysc,reps,int(seeds['delta_ece']))
    bias_ci=bootstrap_bias_diff(s,pr,pc,y,reps,int(seeds['delta_bias']))
    point={'delta_log_loss':float((llc-llr).mean()),'delta_brier':float((brc-brr).mean()),'delta_ece':float(ecec-ecer),'delta_bias':float(biasc-biasr)}
    ci={'delta_log_loss':{'lower':ll_ci[0],'upper':ll_ci[1]},'delta_brier':{'lower':br_ci[0],'upper':br_ci[1]},'delta_ece':{'lower':ece_ci[0],'upper':ece_ci[1]},'delta_bias':{'lower':bias_ci[0],'upper':bias_ci[1]}}
    gates={'G_LL':ci['delta_log_loss']['upper']<0.0,'G_Brier':ci['delta_brier']['upper']<0.0,'G_ECE_NI':ci['delta_ece']['upper']<float(cfg['epsilon_ece']),'G_bias_NI':ci['delta_bias']['upper']<float(cfg['epsilon_bias'])}
    return {'rows':len(df),'sessions':S,'reference_metrics':{'log_loss':float(llr.mean()),'brier':float(brr.mean()),'ece_10':ecer,'absolute_mean_bias':biasr},'candidate_metrics':{'log_loss':float(llc.mean()),'brier':float(brc.mean()),'ece_10':ecec,'absolute_mean_bias':biasc},'point_differences':point,'bootstrap_ci95':ci,'gates':gates,'all_gates_pass':bool(all(gates.values()))}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',type=Path,required=True); ap.add_argument('--index',type=Path,required=True); ap.add_argument('--reference-oof',type=Path,required=True); ap.add_argument('--candidate-oof',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    cfg=yaml.safe_load(a.config.read_text())
    if sha256(a.reference_oof)!=cfg['reference_oof_sha256_required']: raise AssertionError('reference OOF hash mismatch')
    if sha256(a.candidate_oof)!=cfg['candidate_oof_sha256_required']: raise AssertionError('candidate OOF hash mismatch')
    idx=pd.read_csv(a.index,usecols=['session_id']); sizes=idx.groupby('session_id',sort=True).size().to_numpy(int)
    syn_records,syn_counts=synthetic_suite(sizes,float(cfg['epsilon_ece']),list(cfg['synthetic_validation']['dataset_seeds']),int(cfg['synthetic_validation']['bootstrap_replicates']),int(cfg['synthetic_validation']['bootstrap_seed_offset']))
    vg=cfg['synthetic_validation']['validity_gates']
    synthetic_gates={'S0':syn_counts['S0']['pass']>=int(vg['S0_min_pass']),'S1':syn_counts['S1']['pass']>=int(vg['S1_min_pass']),'S2':syn_counts['S2']['fail']>=int(vg['S2_min_fail'])}
    method_valid=bool(all(synthetic_gates.values()))
    record={'schema_version':1,'method_experiment_id':'GAMMA_CAL_NI','synthetic_validation':{'counts':syn_counts,'gates':synthetic_gates,'all_gates_pass':method_valid,'records':syn_records},'method_authority':{'Gamma_cal_NI':method_valid}}
    if method_valid:
        hist=historical_adjudication(a.index,a.reference_oof,a.candidate_oof,cfg)
        record['historical_successor_adjudication']=hist
        record['scientific_authority']={'mature_non_CCA_probability_treatment':bool(hist['all_gates_pass']),'mature_non_CCA_baseline':False,'CCA_derived_feature_authority':False}
    else:
        record['historical_successor_adjudication']=None
        record['scientific_authority']={'mature_non_CCA_probability_treatment':False,'mature_non_CCA_baseline':False,'CCA_derived_feature_authority':False}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'method_valid':method_valid,'synthetic_counts':syn_counts,'synthetic_gates':synthetic_gates,'historical':record['historical_successor_adjudication']},indent=2,sort_keys=True))

if __name__=='__main__': main()
