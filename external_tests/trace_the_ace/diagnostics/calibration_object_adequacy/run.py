#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np,pandas as pd,yaml

def bins(p,n=10): return np.clip(np.digitize(np.asarray(p,float),np.linspace(0,1,n+1)[1:-1],right=False),0,n-1)
def weighted_l1(w,p,q): return float(np.sum(w*np.abs(p-q))/np.sum(w))
def population_ece(w,p,q,n=10):
    b=bins(p,n);N=float(np.sum(w));return float(sum(abs(float(np.sum(w[b==k]*(p[b==k]-q[b==k]))/N)) for k in range(n) if np.any(b==k)))
def shape(name,q):
    if name=='global_shift': return np.ones_like(q)
    if name=='linear_tilt': return 2*q-1
    if name=='smooth_low_frequency': return np.sin(4*math.pi*q)
    if name=='localized_band': return ((q>=0.45)&(q<=0.65)).astype(float)
    if name=='within_bin_alternating':
        s=np.sign(np.sin(40*math.pi*q));s[s==0]=1;return s
    raise ValueError(name)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--config',type=Path,required=True);ap.add_argument('--index',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();cfg=yaml.safe_load(a.config.read_text());pop=cfg['synthetic_population'];eps=float(cfg['scientific_scale']['epsilon']);w=pd.read_csv(a.index,usecols=['session_id']).groupby('session_id',sort=True).size().to_numpy(float);S=len(w);q=np.linspace(float(pop['q_min']),float(pop['q_max']),S);amps=np.linspace(float(pop['amplitude_grid_min']),float(pop['amplitude_grid_max']),int(pop['amplitude_grid_points']));lo=float(pop['probability_lower_exclusive']);hi=float(pop['probability_upper_exclusive']);tol=float(pop['target_match_absolute_tolerance']);targets=[float(x)*eps for x in pop['target_multipliers']];records={};family_gates={}
    for name in pop['defect_families']:
        h=shape(name,q);rows=[]
        for target in targets:
            best=None
            for amp in amps:
                p=q+amp*h
                if p.min()<=lo or p.max()>=hi: continue
                true=weighted_l1(w,p,q);err=abs(true-target);cand=(err,float(amp),true)
                if best is None or cand<best:best=cand
            if best is None or best[0]>tol: raise AssertionError(f'target unreachable {name} {target}: {best}')
            err,amp,true=best;p=q+amp*h;ece=population_ece(w,p,q,int(cfg['measurement_under_test']['bins']));rows.append({'target':target,'amplitude':amp,'true_L1':true,'target_abs_error':err,'ECE10':ece,'ECE_to_L1_ratio':float(ece/true) if true>0 else None,'ece_indicates_NI':bool(ece<eps)})
        sub,bound,mat=rows;directional=bool(sub['ECE10']<=bound['ECE10']+1e-15 and bound['ECE10']<=mat['ECE10']+1e-15);g={'submargin_protection':bool(sub['ECE10']<eps),'material_degradation_detection':bool(mat['ECE10']>=eps),'directional_nondecreasing':directional};family_gates[name]=g;records[name]=rows
    all_pass=all(all(x.values()) for x in family_gates.values());outcome='ECE10_ADEQUATE_ON_DECLARED_SCOPE' if all_pass else 'ECE10_INADEQUATE_ON_DECLARED_SCOPE';rec={'schema_version':1,'method_experiment_id':cfg['method_experiment_id'],'epsilon':eps,'families':records,'family_gates':family_gates,'all_adequacy_gates_pass':all_pass,'diagnostic_outcome':outcome,'historical_oof_read':False,'authority':{'D_object_local_weight':'AGAINST' if all_pass else 'SUPPORT','ECE10_replacement_authorized':False,'mature_non_CCA_probability_treatment':False,'CCA_derived_feature_authority':False}};a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n');print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__':main()
