#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
import pandas as pd
import yaml

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def bin_index(p,bins=10): return np.clip(np.digitize(np.asarray(p,float),np.linspace(0,1,bins+1)[1:-1],right=False),0,bins-1)
def population_ece(session_sizes,p,q,bins=10):
    n=np.asarray(session_sizes,float);p=np.asarray(p,float);q=np.asarray(q,float);b=bin_index(p,bins);N=float(n.sum());return float(sum(abs(float(np.sum(n[b==k]*(p[b==k]-q[b==k]))/N)) for k in range(bins) if np.any(b==k)))
def session_residual_aggregates(session_codes,p,y,n_sessions,bins=10):
    p=np.asarray(p,float);y=np.asarray(y,float);s=np.asarray(session_codes,int);b=bin_index(p,bins);key=s*bins+b;size=n_sessions*bins;cnt=np.bincount(key,minlength=size).reshape(n_sessions,bins).astype(float);resid=np.bincount(key,weights=p-y,minlength=size).reshape(n_sessions,bins).astype(float);n_j=np.bincount(s,minlength=n_sessions).astype(float);return cnt,resid,n_j
def constant_session_prediction_aggregates(session_sizes,p,ysum,bins=10):
    n=np.asarray(session_sizes,float);p=np.asarray(p,float);ysum=np.asarray(ysum,float);S=len(n);b=bin_index(p,bins);rows=np.arange(S);cnt=np.zeros((S,bins),float);resid=np.zeros((S,bins),float);cnt[rows,b]=n;resid[rows,b]=n*p-ysum;return cnt,resid,n.copy()
def model_if(cnt,resid,n_j,regularity_threshold):
    S=len(n_j);N=float(n_j.sum());mean_n=N/S;mu=resid.sum(axis=0)/N;nonempty=cnt.sum(axis=0)>0;signs=np.sign(mu);if_bin=(resid-n_j[:,None]*mu[None,:])/mean_n;se_bin=if_bin.std(axis=0,ddof=1)/math.sqrt(S);z=np.full_like(mu,np.nan,float)
    for b in range(len(mu)):
        if not nonempty[b]:continue
        z[b]=math.inf if se_bin[b]==0 and abs(mu[b])>0 else (0.0 if se_bin[b]==0 else abs(mu[b])/se_bin[b])
    regular=bool(np.all(z[nonempty]>=regularity_threshold));return {'theta':float(np.abs(mu).sum()),'mu':mu,'nonempty':nonempty,'se_bin':se_bin,'z_bin':z,'regular':regular,'if_total':(if_bin*signs[None,:]).sum(axis=1)}
def paired_if_interval(cnt_r,resid_r,n_r,cnt_c,resid_c,n_c,zcrit,regularity_threshold):
    if not np.array_equal(n_r,n_c):raise AssertionError('paired cluster counts differ')
    rr=model_if(cnt_r,resid_r,n_r,regularity_threshold);cc=model_if(cnt_c,resid_c,n_c,regularity_threshold);d=cc['if_total']-rr['if_total'];S=len(d);se=float(d.std(ddof=1)/math.sqrt(S));point=float(cc['theta']-rr['theta']);lo=point-zcrit*se;hi=point+zcrit*se
    return {'point_delta_ece':point,'se':se,'ci95_lower':float(lo),'ci95_upper':float(hi),'ci95_width':float(hi-lo),'regularity_pass':bool(rr['regular'] and cc['regular']),'reference':{'ece_10':rr['theta'],'bin_mu':rr['mu'].tolist(),'bin_se':rr['se_bin'].tolist(),'bin_abs_signal_z':rr['z_bin'].tolist(),'nonempty_bins':rr['nonempty'].tolist(),'regularity_pass':rr['regular']},'candidate':{'ece_10':cc['theta'],'bin_mu':cc['mu'].tolist(),'bin_se':cc['se_bin'].tolist(),'bin_abs_signal_z':cc['z_bin'].tolist(),'nonempty_bins':cc['nonempty'].tolist(),'regularity_pass':cc['regular']}}
def constitute_fixture(session_sizes,cfg):
    fx=cfg['synthetic_fixture'];S=len(session_sizes);u=(np.arange(S,dtype=float)+0.5)/S;pref=0.15+0.70*u;rb=bin_index(pref,10);sg=np.where(rb%2==0,1.0,-1.0);mag=float(fx['reference_bin_residual_magnitude']);q=pref-mag*sg
    if np.any(q<=0) or np.any(q>=1):raise AssertionError('synthetic q outside unit interval')
    ref_ece=population_ece(session_sizes,pref,q);agrid=np.linspace(float(fx['a_grid_min']),float(fx['a_grid_max']),int(fx['a_grid_points']));bgrid=np.linspace(float(fx['b_grid_min']),float(fx['b_grid_max']),int(fx['b_grid_points']));targets={k:float(v) for k,v in fx['scenarios'].items()};chosen={};tol=float(fx['target_match_absolute_tolerance']);minchg=float(fx['minimum_bin_membership_change_fraction_nonzero']);lo=float(fx['probability_lower_exclusive']);hi=float(fx['probability_upper_exclusive'])
    for name,target in targets.items():
        best=None
        for a in agrid:
            for b in bgrid:
                pc=pref+a+b*sg
                if np.min(pc)<=lo or np.max(pc)>=hi:continue
                change=float(np.mean(bin_index(pc,10)!=rb));d=population_ece(session_sizes,pc,q)-ref_ece;err=abs(d-target);candidate=(err,float(a),float(b),float(d),change)
                if best is None or candidate[:3]<best[:3]:best=candidate
        if best is None:raise AssertionError(f'no admissible candidate {name}')
        err,a,b,d,change=best
        if err>tol:raise AssertionError(f'target not reachable {name}: err={err}')
        if target!=0 and change<minchg:raise AssertionError(f'insufficient bin change {name}: {change}')
        chosen[name]={'target_delta':target,'a':a,'b':b,'true_delta':d,'target_abs_error':err,'bin_membership_change_fraction':change}
    return pref,q,ref_ece,chosen
def synthetic_regular(session_sizes,cfg):
    fx=cfg['synthetic_fixture'];pref,q,ref_ece,chosen=constitute_fixture(session_sizes,cfg);zcrit=float(cfg['uncertainty_candidate']['z_critical']);rz=float(cfg['uncertainty_candidate']['regularity_gate_z']);start=int(fx['outcome_seeds_start']);count=int(fx['outcome_seed_count']);sg=np.where(bin_index(pref,10)%2==0,1.0,-1.0);records=[]
    for seed in range(start,start+count):
        rng=np.random.default_rng(seed);ysum=rng.binomial(session_sizes,q);cr,rr,nr=constant_session_prediction_aggregates(session_sizes,pref,ysum)
        for name,spec in chosen.items():
            pc=pref+float(spec['a'])+float(spec['b'])*sg;cc,rc,nc=constant_session_prediction_aggregates(session_sizes,pc,ysum);rec=paired_if_interval(cr,rr,nr,cc,rc,nc,zcrit,rz);true=float(spec['true_delta']);rec.update({'dataset_seed':seed,'scenario':name,'true_delta_ece':true,'covers_true_delta':bool(rec['ci95_lower']<=true<=rec['ci95_upper']),'passes_noninferiority':bool(rec['ci95_upper']<float(cfg['scientific_target']['epsilon_ece']))});records.append(rec)
    summary={}
    for name in chosen:
        r=[x for x in records if x['scenario']==name];summary[name]={'n':len(r),'coverage_rate':float(np.mean([x['covers_true_delta'] for x in r])),'NI_pass_rate':float(np.mean([x['passes_noninferiority'] for x in r])),'regularity_pass_rate':float(np.mean([x['regularity_pass'] for x in r])),'median_width':float(np.median([x['ci95_width'] for x in r]))}
    return {'reference_population_ece':ref_ece,'scenario_identity':chosen},records,summary
def synthetic_nonregular(session_sizes,cfg):
    fx=cfg['synthetic_fixture'];S=len(session_sizes);u=(np.arange(S,dtype=float)+0.5)/S;p=0.15+0.70*u;q=p.copy();zcrit=float(cfg['uncertainty_candidate']['z_critical']);rz=float(cfg['uncertainty_candidate']['regularity_gate_z']);start=int(fx['nonregular_negative_control_seeds_start']);count=int(fx['nonregular_negative_control_count']);out=[]
    for seed in range(start,start+count):
        rng=np.random.default_rng(seed);ysum=rng.binomial(session_sizes,q);c,r,n=constant_session_prediction_aggregates(session_sizes,p,ysum);rec=paired_if_interval(c,r,n,c,r,n,zcrit,rz);out.append({'dataset_seed':seed,'regularity_pass':rec['regularity_pass'],'bin_abs_signal_z':rec['reference']['bin_abs_signal_z']})
    return out,{'n':len(out),'regularity_fail_rate':float(np.mean([not x['regularity_pass'] for x in out]))}
def validate(fixture,summary,nonreg,cfg):
    g=cfg['synthetic_fixture']['validity_gates'];gates={}
    for name in ['S1','SB','S2']:gates[f'coverage_{name}']=summary[name]['coverage_rate']>=float(g['minimum_coverage_each_nonzero_scenario'])
    gates['NI_S1']=summary['S1']['NI_pass_rate']>=float(g['minimum_NI_pass_rate_S1']);gates['NI_SB']=summary['SB']['NI_pass_rate']<=float(g['maximum_NI_pass_rate_SB']);gates['NI_S2']=1-summary['S2']['NI_pass_rate']>=float(g['minimum_NI_fail_rate_S2']);gates['regularity_regular']=min(summary[k]['regularity_pass_rate'] for k in ['S0','S1','SB','S2'])>=float(g['minimum_regularity_pass_rate_regular_scenarios']);gates['regularity_nonregular']=nonreg['regularity_fail_rate']>=float(g['minimum_regularity_fail_rate_nonregular_control']);gates['nondegenerate_width']=min(summary[k]['median_width'] for k in ['S1','SB','S2'])>=float(g['minimum_median_ci_width_nonzero_scenarios']);gates['target_matches']=all(v['target_abs_error']<=float(cfg['synthetic_fixture']['target_match_absolute_tolerance']) for v in fixture['scenario_identity'].values());return gates,bool(all(gates.values()))
def historical(index,ref_oof,cand_oof,cfg):
    idx=pd.read_csv(index,usecols=['response_id','session_id','is_correct']);r=pd.read_csv(ref_oof,usecols=['response_id','m1_cal_probability']);c=pd.read_csv(cand_oof,usecols=['response_id','m2_s_cal_probability']);df=idx.merge(r,on='response_id',validate='one_to_one').merge(c,on='response_id',validate='one_to_one');cats=pd.Categorical(df.session_id.astype(str),categories=sorted(df.session_id.astype(str).unique()));s=cats.codes.astype(int);S=len(cats.categories);y=df.is_correct.to_numpy(float);pr=df.m1_cal_probability.to_numpy(float);pc=df.m2_s_cal_probability.to_numpy(float);cr,rr,nr=session_residual_aggregates(s,pr,y,S);cc,rc,nc=session_residual_aggregates(s,pc,y,S);rec=paired_if_interval(cr,rr,nr,cc,rc,nc,float(cfg['uncertainty_candidate']['z_critical']),float(cfg['uncertainty_candidate']['regularity_gate_z']));oldw=float(cfg['predecessor_bootstrap_ece_ci95']['width']);eps=float(cfg['scientific_target']['epsilon_ece']);regular=rec['regularity_pass'];narrower=rec['ci95_width']<oldw;identifies=rec['ci95_upper']<eps
    if not regular:outcome='HISTORICAL_NONREGULAR'
    elif not narrower:outcome='NOT_MORE_EFFICIENT'
    elif not identifies:outcome='EFFICIENT_NOT_IDENTIFYING'
    else:outcome='EFFICIENT_AND_IDENTIFYING'
    rec.update({'predecessor_ci95':cfg['predecessor_bootstrap_ece_ci95'],'predecessor_width':oldw,'epsilon_ece':eps,'is_narrower_than_predecessor':bool(narrower),'identifies_noninferiority':bool(identifies),'diagnostic_outcome':outcome,'rows':len(df),'sessions':S});return rec
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--config',type=Path,required=True);ap.add_argument('--index',type=Path,required=True);ap.add_argument('--reference-oof',type=Path,required=True);ap.add_argument('--candidate-oof',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();cfg=yaml.safe_load(a.config.read_text());sizes=pd.read_csv(a.index,usecols=['session_id']).groupby('session_id',sort=True).size().to_numpy(int);fixture,reg_records,summary=synthetic_regular(sizes,cfg);nonreg_records,nonreg=synthetic_nonregular(sizes,cfg);gates,valid=validate(fixture,summary,nonreg,cfg);record={'schema_version':1,'method_experiment_id':cfg['method_experiment_id'],'fixture_identity':fixture,'synthetic_validation':{'summary':summary,'nonregular_control_summary':nonreg,'gates':gates,'all_gates_pass':valid,'regular_records':reg_records,'nonregular_records':nonreg_records},'method_valid':valid}
    if valid:
        if sha256(a.reference_oof)!=cfg['reference_oof_sha256_required']:raise AssertionError('reference OOF hash mismatch')
        if sha256(a.candidate_oof)!=cfg['candidate_oof_sha256_required']:raise AssertionError('candidate OOF hash mismatch')
        record['historical']=historical(a.index,a.reference_oof,a.candidate_oof,cfg)
    else:record['historical']=None
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n');print(json.dumps({'method_valid':valid,'fixture_identity':fixture,'synthetic_summary':summary,'nonregular_control':nonreg,'gates':gates,'historical':record['historical']},indent=2,sort_keys=True))
if __name__=='__main__':main()
