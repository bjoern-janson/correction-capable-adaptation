import json, math, hashlib, time
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.special import ndtr

INDEX = Path('/mnt/data/trace_tta_patch/external_tests/trace_the_ace/artifacts/index.csv')
PREDECESSOR = Path('/mnt/data/calibration_resolution_run/results/final.json')
OUTDIR = Path('/mnt/data/calibration_information_scaling_run/results')
WORKDIR = Path('/mnt/data/calibration_information_scaling_run/work')
OUTDIR.mkdir(parents=True, exist_ok=True)
WORKDIR.mkdir(parents=True, exist_ok=True)

INDEX_SHA = '296399770b0818fa528f33382497bc7f4793b3c54a2e49e56e77efbc19d55c60'
SALT = 'SMECE_CAL_REPLACEMENT_V1|'
RHO = 0.15
SENTINELS = [('coarse',0.1,0), ('fine',0.000048828125,11)]
RATIOS = np.array([0.0,0.125,0.25,0.50],dtype=np.float64)
MULTIPLIERS = [1,2,4,8,16]
C_R = 0.010
B = 2000
N_REP = 100
N0 = 35072
S0 = 22821
BOOT_CHUNK = 32

# Prospectively frozen execution mechanics for PR #44:
# 1) Baseline gate reruns the exact PR #43 endpoint apparatus using seeds 1823/1824.
# 2) Scaling outcomes use independent per-(sentinel,ratio,replicate,cohort) streams:
#      SeedSequence([1831, sentinel_index, ratio_index, synthetic_replicate, cohort_index]).
# 3) Scaling cluster-bootstrap draws use SeedSequence([1832, multiplier_index]), B=2000,
#    and are common to all sentinel/ratio cells at a multiplier.
# 4) Cohorts are nested by deterministic reuse of stored cohort session-noise blocks;
#    multiplier m uses the first m cohort blocks.
# 5) Exact multinomial/session-cluster bootstrap counts are stored as uint8 memmaps;
#    counts are asserted <=255. Multiplication/quantiles use float64.
# 6) Generated arrays remain local. Only result summaries/hashes are committed.

def rng_for(base,*coords):
    return np.random.default_rng(np.random.SeedSequence([int(base),*map(int,coords)]))

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def truth_from_response_id(response_ids):
    def one(x):
        h=hashlib.sha256((SALT+str(x)).encode()).digest()
        u=(int.from_bytes(h[:8],'big')+0.5)/(2**64)
        return 0.05+0.90*u
    return np.fromiter((one(x) for x in response_ids),dtype=np.float64,count=len(response_ids))

def scale_sign(T,h):
    z=np.sin(2*np.pi*T/h)
    s=np.sign(z)
    s[z==0.0]=0.0
    return s.astype(np.float64)

def setup_geometry():
    assert sha256(INDEX)==INDEX_SHA
    df=pd.read_csv(INDEX,usecols=['response_id','session_id'])
    assert len(df)==N0 and df['session_id'].nunique()==S0
    T=truth_from_response_id(df['response_id'].astype(str).to_numpy())
    sessions=np.sort(df['session_id'].astype(str).unique())
    smap={s:i for i,s in enumerate(sessions)}
    codes=np.fromiter((smap[x] for x in df['session_id'].astype(str)),dtype=np.int32,count=len(df))
    order=np.argsort(codes,kind='stable')
    sorted_codes=codes[order]
    starts=np.r_[0,np.flatnonzero(np.diff(sorted_codes))+1]
    sizes=np.add.reduceat(np.ones(len(df),dtype=np.int32)[order],starts).astype(np.float64)
    assert len(sizes)==S0 and int(sizes.sum())==N0
    return T,codes,order,starts,sizes

def draw_outcomes_matrix_pr43(T,codes,n_sessions,n_reps,rng):
    Z=rng.normal(size=(n_sessions,n_reps))
    eps=rng.normal(size=(len(T),n_reps))
    L=math.sqrt(RHO)*Z[codes,:]+math.sqrt(1-RHO)*eps
    return ndtr(L)<=T[:,None]

def session_noise_matrix(T,s,Y,order,starts):
    q=s[:,None]*(T[:,None]-Y)
    return np.add.reduceat(q[order,:],starts,axis=0)

def percentile_valid(x,qs=(0.025,0.975)):
    return tuple(float(v) for v in np.quantile(np.asarray(x,dtype=np.float64),qs))

def pr43_bootstrap_counts():
    rng=rng_for(1824)
    W=np.zeros((B,S0),dtype=np.uint16)
    for b in range(B):
        idx=rng.integers(0,S0,size=S0,dtype=np.int32)
        W[b,:]=np.bincount(idx,minlength=S0).astype(np.uint16)
    assert np.all(W.sum(axis=1)==S0)
    return W

def summarize_cell(qs,sizes,Wf,Rtrue):
    denom_boot=Wf@sizes
    qboot=Wf@qs
    Cref_boot=C_R+qboot/denom_boot[:,None]
    invalid=Cref_boot<=0.0
    invalid_frac=np.mean(invalid,axis=0)
    loR=np.full(N_REP,np.nan); hiR=np.full(N_REP,np.nan)
    loC=np.full(N_REP,np.nan); hiC=np.full(N_REP,np.nan)
    cover=np.zeros(N_REP,dtype=bool); ni=np.zeros(N_REP,dtype=bool)
    denom_guard=np.zeros(N_REP,dtype=bool); interval_valid=np.zeros(N_REP,dtype=bool)
    delta=float(Rtrue*C_R)
    for j in range(N_REP):
        good=~invalid[:,j]
        if invalid_frac[j] <=0.01 and int(good.sum())>0:
            cb=Cref_boot[good,j]
            loC[j],hiC[j]=percentile_valid(cb)
            denom_guard[j]=loC[j]>0.0
            rb=np.zeros_like(cb) if delta==0.0 else delta/cb
            loR[j],hiR[j]=percentile_valid(rb)
            interval_valid[j]=True
            cover[j]=(loR[j] <= Rtrue <= hiR[j])
            ni[j]=(hiR[j] < 0.25)
    point=np.sum(qs,axis=0)/float(np.sum(sizes))+C_R
    coverage=float(np.mean(cover)); ni_rate=float(np.mean(ni)); denom_rate=float(np.mean(denom_guard))
    valid_rate=float(np.mean(interval_valid)); invalid_ok=bool(np.all(invalid_frac<=0.01))
    coverage_ok=bool(0.90<=coverage<=0.99)
    ni_ok=bool(ni_rate>=0.80) if Rtrue in (0.0,0.125) else bool(ni_rate<=0.10)
    denom_ok=bool(denom_rate>=0.95)
    cell_pass=bool(invalid_ok and coverage_ok and ni_ok and denom_ok)
    return {
        'R_true':float(Rtrue),'coverage':coverage,'NI_pass_rate':ni_rate,
        'denominator_guard_rate':denom_rate,'interval_valid_rate':valid_rate,
        'max_invalid_bootstrap_fraction':float(np.max(invalid_frac)),
        'invalid_fraction_mean':float(np.mean(invalid_frac)),
        'coverage_pass':coverage_ok,'NI_pass':ni_ok,'denominator_pass':denom_ok,
        'invalid_bootstrap_pass':invalid_ok,'pass':cell_pass,
        'point_Cref_mean':float(np.mean(point)),'point_Cref_sd':float(np.std(point,ddof=1)),
        'median_interval_width_R':float(np.nanmedian(hiR-loR)),
        'median_lower_Cref':float(np.nanmedian(loC)),
    }

def baseline_reproduction(T,codes,order,starts,sizes):
    predecessor=json.loads(PREDECESSOR.read_text())
    W=pr43_bootstrap_counts(); Wf=W.astype(np.float64)
    out={'status':'PASS','cells':{},'mismatches':[]}
    for label,h,hi in SENTINELS:
        s=scale_sign(T,h)
        out['cells'][label]={}
        for ri,Rtrue in enumerate(RATIOS):
            Y=draw_outcomes_matrix_pr43(T,codes,S0,N_REP,rng_for(1823,hi,ri))
            qs=session_noise_matrix(T,s,Y,order,starts)
            got=summarize_cell(qs,sizes,Wf,float(Rtrue))
            exp=predecessor['decision'][f'h_{hi}']['cells'][f'R_{Rtrue:g}']
            same=(got==exp)
            out['cells'][label][f'R_{Rtrue:g}']={'exact_match':same,'got':got,'expected':exp}
            if not same: out['mismatches'].append({'sentinel':label,'R':float(Rtrue)})
            del Y,qs
    if out['mismatches']: out['status']='FAIL'
    p=OUTDIR/'baseline_reproduction.json'; p.write_text(json.dumps(out,indent=2))
    return out

def generate_nested_session_noise(T,codes,order,starts):
    paths={}
    for si,(label,h,_) in enumerate(SENTINELS):
        s=scale_sign(T,h)
        for ri,Rtrue in enumerate(RATIOS):
            path=WORKDIR/f'noise_{label}_r{ri}.dat'
            mm=np.memmap(path,mode='w+',dtype=np.float64,shape=(16*S0,N_REP))
            for c in range(16):
                block=mm[c*S0:(c+1)*S0,:]
                for rep in range(N_REP):
                    rng=rng_for(1831,si,ri,rep,c)
                    Z=rng.normal(size=S0)
                    eps=rng.normal(size=N0)
                    L=math.sqrt(RHO)*Z[codes]+math.sqrt(1-RHO)*eps
                    Y=ndtr(L)<=T
                    q=s*(T-Y)
                    block[:,rep]=np.add.reduceat(q[order],starts)
                mm.flush()
                print(f'NOISE sentinel={label} R={Rtrue:g} cohort={c+1}/16',flush=True)
            del mm
            paths[(si,ri)]=path
    return paths

def generate_bootstrap_memmap(S,midx):
    path=WORKDIR/f'bootstrap_m{MULTIPLIERS[midx]}.dat'
    W=np.memmap(path,mode='w+',dtype=np.uint8,shape=(B,S))
    rng=rng_for(1832,midx)
    max_count=0
    for b in range(B):
        idx=rng.integers(0,S,size=S,dtype=np.int32)
        cnt=np.bincount(idx,minlength=S)
        mc=int(cnt.max()); max_count=max(max_count,mc)
        assert mc<=255
        W[b,:]=cnt.astype(np.uint8)
    W.flush(); del W
    return path,max_count

def bootstrap_q_from_memmaps(Wpath,qpath,S,sizes_m):
    W=np.memmap(Wpath,mode='r',dtype=np.uint8,shape=(B,S))
    q=np.memmap(qpath,mode='r',dtype=np.float64,shape=(16*S0,N_REP))
    qview=q[:S,:]
    qboot=np.empty((B,N_REP),dtype=np.float64)
    denom=np.empty(B,dtype=np.float64)
    for lo in range(0,B,BOOT_CHUNK):
        hi=min(B,lo+BOOT_CHUNK)
        Wf=np.asarray(W[lo:hi,:],dtype=np.float64)
        qboot[lo:hi,:]=Wf@qview
        denom[lo:hi]=Wf@sizes_m
    point_noise=np.sum(qview,axis=0)/float(np.sum(sizes_m))
    del q,W
    return qboot,denom,point_noise

def summarize_from_boot(qboot,denom,point_noise,Rtrue):
    Cref_boot=C_R+qboot/denom[:,None]
    invalid=Cref_boot<=0.0
    invalid_frac=np.mean(invalid,axis=0)
    loR=np.full(N_REP,np.nan); hiR=np.full(N_REP,np.nan)
    loC=np.full(N_REP,np.nan); hiC=np.full(N_REP,np.nan)
    cover=np.zeros(N_REP,dtype=bool); ni=np.zeros(N_REP,dtype=bool)
    denom_guard=np.zeros(N_REP,dtype=bool); interval_valid=np.zeros(N_REP,dtype=bool)
    delta=float(Rtrue*C_R)
    for j in range(N_REP):
        good=~invalid[:,j]
        if invalid_frac[j] <=0.01 and int(good.sum())>0:
            cb=Cref_boot[good,j]
            loC[j],hiC[j]=percentile_valid(cb)
            denom_guard[j]=loC[j]>0.0
            rb=np.zeros_like(cb) if delta==0.0 else delta/cb
            loR[j],hiR[j]=percentile_valid(rb)
            interval_valid[j]=True
            cover[j]=(loR[j] <= Rtrue <= hiR[j])
            ni[j]=(hiR[j] < 0.25)
    point=C_R+point_noise
    coverage=float(np.mean(cover)); ni_rate=float(np.mean(ni)); denom_rate=float(np.mean(denom_guard))
    valid_rate=float(np.mean(interval_valid)); invalid_ok=bool(np.all(invalid_frac<=0.01))
    coverage_ok=bool(0.90<=coverage<=0.99)
    ni_ok=bool(ni_rate>=0.80) if Rtrue in (0.0,0.125) else bool(ni_rate<=0.10)
    denom_ok=bool(denom_rate>=0.95)
    cell_pass=bool(invalid_ok and coverage_ok and ni_ok and denom_ok)
    return {
        'R_true':float(Rtrue),'coverage':coverage,'NI_pass_rate':ni_rate,
        'denominator_guard_rate':denom_rate,'interval_valid_rate':valid_rate,
        'max_invalid_bootstrap_fraction':float(np.max(invalid_frac)),
        'invalid_fraction_mean':float(np.mean(invalid_frac)),
        'coverage_pass':coverage_ok,'NI_pass':ni_ok,'denominator_pass':denom_ok,
        'invalid_bootstrap_pass':invalid_ok,'pass':cell_pass,
        'point_Cref_mean':float(np.mean(point)),'point_Cref_sd':float(np.std(point,ddof=1)),
        'median_interval_width_R':float(np.nanmedian(hiR-loR)),
        'median_lower_Cref':float(np.nanmedian(loC)),
    }

def run():
    t0=time.time()
    T,codes,order,starts,sizes=setup_geometry()
    result={
        'experiment_id':'GAMMA_CAL_INFORMATION_SCALING','status':'EXECUTING',
        'source':{'index_sha256':sha256(INDEX),'rows_per_cohort':N0,'sessions_per_cohort':S0,'labels_read':False},
        'baseline_reproduction':None,'curve':{},'outputs':{},
        'execution':{
            'scaling_outcome_seed_derivation':'SeedSequence([1831,sentinel_index,ratio_index,synthetic_replicate,cohort_index])',
            'scaling_bootstrap_seed_derivation':'SeedSequence([1832,multiplier_index])',
            'nested_cohorts':True,'bootstrap_B':B,'bootstrap_chunk':BOOT_CHUNK,
            'bootstrap_count_storage':'uint8 memmap with max-count assertion','numeric_dtype':'float64'
        }
    }
    base=baseline_reproduction(T,codes,order,starts,sizes)
    result['baseline_reproduction']={'status':base['status'],'artifact_sha256':sha256(OUTDIR/'baseline_reproduction.json'),'mismatch_count':len(base['mismatches'])}
    if base['status']!='PASS':
        result['status']='IMPLEMENTATION_FAILURE_BASELINE_REPRODUCTION'
        (OUTDIR/'final.json').write_text(json.dumps(result,indent=2))
        print('BASELINE REPRODUCTION FAIL',base['mismatches'],flush=True)
        return result
    print('BASELINE REPRODUCTION PASS',flush=True)

    paths=generate_nested_session_noise(T,codes,order,starts)
    sentinel_pass_vectors={label:[] for label,_,_ in SENTINELS}
    joint=[]
    for midx,m in enumerate(MULTIPLIERS):
        S=m*S0
        sizes_m=np.tile(sizes,m)
        Wpath,max_count=generate_bootstrap_memmap(S,midx)
        mrec={'m':m,'rows':m*N0,'sessions':S,'bootstrap_max_cluster_count':max_count,'sentinels':{}}
        print(f'BOOTSTRAP READY m={m} S={S} max_count={max_count}',flush=True)
        for si,(label,h,_) in enumerate(SENTINELS):
            cells={}; sentinel_pass=True
            for ri,Rtrue in enumerate(RATIOS):
                qboot,denom,point_noise=bootstrap_q_from_memmaps(Wpath,paths[(si,ri)],S,sizes_m)
                cell=summarize_from_boot(qboot,denom,point_noise,float(Rtrue))
                cells[f'R_{Rtrue:g}']=cell; sentinel_pass &= cell['pass']
                print(f'SCALE m={m} h={label} R={Rtrue:.3f} cov={cell["coverage"]:.3f} NI={cell["NI_pass_rate"]:.3f} width={cell["median_interval_width_R"]:.6f} invmax={cell["max_invalid_bootstrap_fraction"]:.4f} pass={cell["pass"]}',flush=True)
            mrec['sentinels'][label]={'h':h,'cells':cells,'pass':bool(sentinel_pass)}
            sentinel_pass_vectors[label].append(bool(sentinel_pass))
        jp=bool(all(mrec['sentinels'][label]['pass'] for label,_,_ in SENTINELS)); joint.append(jp)
        mrec['joint_pass']=jp; result['curve'][f'm_{m}']=mrec
        print(f'MULTIPLIER m={m} coarse={mrec["sentinels"]["coarse"]["pass"]} fine={mrec["sentinels"]["fine"]["pass"]} joint={jp}',flush=True)
        (OUTDIR/'checkpoint.json').write_text(json.dumps(result,indent=2))
        Path(Wpath).unlink(missing_ok=True)

    def first_pass(v):
        for m,p in zip(MULTIPLIERS,v):
            if p:return m
        return None
    mc=first_pass(sentinel_pass_vectors['coarse']); mf=first_pass(sentinel_pass_vectors['fine']); mj=first_pass(joint)
    result['outputs']={
        'm_min_decision_coarse':mc if mc is not None else 'NONE_IDENTIFIED_WITHIN_GRID',
        'm_min_decision_fine':mf if mf is not None else 'NONE_IDENTIFIED_WITHIN_GRID',
        'm_min_decision_joint':mj if mj is not None else 'NONE_IDENTIFIED_WITHIN_GRID',
        'n_min_decision_joint':(mj*N0) if mj is not None else 'NONE_IDENTIFIED_WITHIN_GRID',
        'coarse_pass_vector':sentinel_pass_vectors['coarse'],'fine_pass_vector':sentinel_pass_vectors['fine'],'joint_pass_vector':joint,
        'D_additional_evidence':'SUPPORTED_AS_INFORMATION_QUANTITY' if (mj is not None and mj>1) else 'NOT_IDENTIFIED_WITHIN_GRID'
    }
    result['status']='EXECUTED'; result['elapsed_seconds']=time.time()-t0
    (OUTDIR/'final.json').write_text(json.dumps(result,indent=2))
    print('FINAL',json.dumps(result['outputs'],indent=2),flush=True)
    print(f'elapsed={result["elapsed_seconds"]:.1f}s',flush=True)
    return result

if __name__=='__main__': run()
