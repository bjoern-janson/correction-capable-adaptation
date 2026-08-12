#!/usr/bin/env python3
"""Aggregate complete M2-SEM fold artifacts and apply frozen calibrated primary gate; raw comparison stays separate."""
from __future__ import annotations
import argparse, importlib.util, json, hashlib
from pathlib import Path
import numpy as np, pandas as pd, yaml
from sklearn.metrics import log_loss, roc_auc_score

def loadmod(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha(p):
    h=hashlib.sha256();f=open(p,'rb')
    for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--index',type=Path,required=True);ap.add_argument('--fold-dir',type=Path,required=True);ap.add_argument('--historical-m2-oof',type=Path,required=True);ap.add_argument('--config',type=Path,required=True);ap.add_argument('--parent-runner',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True);a=ap.parse_args()
    cfg=yaml.safe_load(a.config.read_text());parent=loadmod('p',a.parent_runner);idx=pd.read_csv(a.index,usecols=['response_id','session_id','is_correct']); hist=pd.read_csv(a.historical_m2_oof)[['response_id','m2_o_probability']];df=idx.merge(hist,on='response_id',validate='one_to_one')
    rows=[]; frecs=[]
    for fold in range(5):
        arms={}
        for arm in ['M2_S','M2_SC']:
            rec=json.load(open(a.fold_dir/f'{arm}_fold{fold}.json')); arms[arm]=rec
            rows.extend(zip(rec['response_id'],[arm]*len(rec['response_id']),rec['raw_score'],rec['raw_probability'],rec['calibrated_probability']))
        frecs.append({'outer_fold':fold,'arms':{arm:{kk:vv for kk,vv in rec.items() if kk not in ('response_id','raw_score','raw_probability','calibrated_probability')} for arm,rec in arms.items()}})
    pred=pd.DataFrame(rows,columns=['response_id','arm','raw_score','raw_probability','calibrated_probability']); w=pred.pivot(index='response_id',columns='arm',values=['raw_score','raw_probability','calibrated_probability']); w.columns=['_'.join(x).lower() for x in w.columns];w=w.reset_index();df=df.merge(w,on='response_id',validate='one_to_one');y=df.is_correct.to_numpy(np.int8);g=df.session_id.astype(str).to_numpy()
    ms_raw=df.raw_probability_m2_s.to_numpy();msc_raw=df.raw_probability_m2_sc.to_numpy();ms_cal=df.calibrated_probability_m2_s.to_numpy();msc_cal=df.calibrated_probability_m2_sc.to_numpy();m2o=df.m2_o_probability.to_numpy()
    boot=lambda cand,base,seed: parent.paired_session_bootstrap(g,parent.per_row_log_loss(y,cand),parent.per_row_log_loss(y,base),int(cfg['uncertainty']['replicates']),int(seed))
    rawu=boot(msc_raw,ms_raw,cfg['uncertainty']['random_seed_primary']); prim=boot(msc_cal,ms_cal,cfg['uncertainty']['random_seed_primary']); sem=boot(ms_cal,m2o,cfg['uncertainty']['random_seed_semantic_control']); total=boot(msc_cal,m2o,cfg['uncertainty']['random_seed_total'])
    cal=lambda p: parent.calibration_summary(y,p); cms=cal(ms_cal); cmsc=cal(msc_cal); cm2=cal(m2o)
    ppass=bool(log_loss(y,msc_cal)<log_loss(y,ms_cal) and prim['ci95_upper']<0); impl=all(rec['all_converged'] for fr in frecs for rec in fr['arms'].values())
    out={'schema_version':1,'experiment_id':'M2_SEM','hypothesis_id':'H_O_SEM','status':'DIAGNOSED_PASS' if (ppass and impl) else 'DIAGNOSED_UNRESOLVED','raw_uncalibrated_comparison':{'m2_s_log_loss':float(log_loss(y,ms_raw)),'m2_sc_log_loss':float(log_loss(y,msc_raw)),'delta_m2_sc_minus_m2_s':float(log_loss(y,msc_raw)-log_loss(y,ms_raw)),'uncertainty':rawu,'interpretation':'diagnostic_separate_from_calibrated_primary_gate'},'calibrated_primary':{'m2_s_log_loss':float(log_loss(y,ms_cal)),'m2_sc_log_loss':float(log_loss(y,msc_cal)),'delta_m2_sc_minus_m2_s':float(log_loss(y,msc_cal)-log_loss(y,ms_cal)),'m2_s_auc':float(roc_auc_score(y,ms_cal)),'m2_sc_auc':float(roc_auc_score(y,msc_cal)),'uncertainty':prim,'H_O_SEM_gate_pass':ppass},'diagnostic_vs_historical_m2_o':{'historical_m2_o_log_loss':float(log_loss(y,m2o)),'m2_s_delta':float(log_loss(y,ms_cal)-log_loss(y,m2o)),'m2_sc_delta':float(log_loss(y,msc_cal)-log_loss(y,m2o)),'m2_s_uncertainty':sem,'m2_sc_uncertainty':total},'calibration_diagnostics':{'historical_m2_o':cm2,'m2_s':cms,'m2_sc':cmsc,'historical_M2_calibration_failure_repaired_by_this_branch':False},'implementation':{'all_base_models_converged':impl,'folds':frecs},'authority':{'gained':['objective_conditioned_semantic_reweighting_predictive_value_under_M2_SEM'] if ppass and impl else [],'not_gained':['CCA_support','causal_evidence','G1_evidence','PMC_evidence','repeated_correction_evidence','JT_evidence','C_improve_measurement','CCA_derived_feature_authorization']}}
    a.output_dir.mkdir(parents=True,exist_ok=True); od=df[['response_id','session_id','is_correct','m2_o_probability']].copy();od['m2_s_raw_score']=df.raw_score_m2_s;od['m2_sc_raw_score']=df.raw_score_m2_sc;od['m2_s_raw_probability']=ms_raw;od['m2_sc_raw_probability']=msc_raw;od['m2_s_cal_probability']=ms_cal;od['m2_sc_cal_probability']=msc_cal; op=a.output_dir/'oof_predictions.csv'; od.sort_values('response_id').to_csv(op,index=False,lineterminator='\n'); rp=a.output_dir/'m2_sem_record.json';rp.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); out['artifacts']={'oof_sha256':sha(op)};rp.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
