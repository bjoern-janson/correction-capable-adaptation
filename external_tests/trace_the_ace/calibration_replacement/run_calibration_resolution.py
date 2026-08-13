import os, json, math, hashlib, time
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.special import ndtr

INDEX = Path('/mnt/data/trace_tta_patch/external_tests/trace_the_ace/artifacts/index.csv')
OUTDIR = Path('/mnt/data/calibration_resolution_run/results')
OUTDIR.mkdir(parents=True, exist_ok=True)
INDEX_SHA = '296399770b0818fa528f33382497bc7f4793b3c54a2e49e56e77efbc19d55c60'
SALT = 'SMECE_CAL_REPLACEMENT_V1|'
RHO = 0.15
SCALES = np.array([0.1,0.05,0.025,0.0125,0.00625,0.003125,0.0015625,0.00078125,0.000390625,0.0001953125,0.00009765625,0.000048828125], dtype=np.float64)
RATIOS = np.array([0.0,0.125,0.25,0.50], dtype=np.float64)
C_DETECT = 0.010
C_R = 0.010
B = 2000
N_NULL_TRAIN=200
N_NULL_EVAL=100
N_DETECT=100
N_DECISION=100

# Execution mechanics frozen before any scientific result:
# - session IDs sorted lexicographically for cluster indexing;
# - independent RNG streams use SeedSequence([base_seed, *coordinates]);
# - decision/bootstrap cells use one common, prospectively seeded BxS cluster-count matrix.
#   Reusing these result-independent bootstrap draws across synthetic datasets is a common-random-number
#   execution optimization; for each dataset each row remains an exact S-draw cluster bootstrap replicate.

def rng_for(base, *coords):
    return np.random.default_rng(np.random.SeedSequence([int(base), *map(int, coords)]))

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def truth_from_response_id(response_ids):
    def one(x):
        h=hashlib.sha256((SALT+str(x)).encode()).digest()
        u=(int.from_bytes(h[:8],'big')+0.5)/(2**64)
        return 0.05+0.90*u
    return np.fromiter((one(x) for x in response_ids), dtype=np.float64, count=len(response_ids))

def scale_sign(T,h):
    z=np.sin(2*np.pi*T/h)
    s=np.sign(z)
    s[z==0.0]=0.0
    return s.astype(np.float64)

def min_sorted_gap(x):
    xs=np.sort(np.asarray(x,dtype=np.float64))
    return float(np.min(np.diff(xs)))

def fixture(T,s,C):
    meanabs=float(np.mean(np.abs(s)))
    a=float(C/meanabs)
    P=T+a*s
    gap=min_sorted_gap(P)
    return P, a, {
        'mean_abs_sign':meanabs,
        'amplitude':a,
        'bounds_pass':bool(np.all((P>=0.0)&(P<=1.0))),
        'min_sorted_gap':gap,
        'injective_pass':bool(gap>1e-12),
        'construct':float(np.mean(np.abs(P-T))),
        'construct_error':float(abs(np.mean(np.abs(P-T))-C)),
        'construct_pass':bool(abs(np.mean(np.abs(P-T))-C)<=1e-12),
    }

def setup_geometry():
    got=sha256(INDEX)
    assert got==INDEX_SHA,(got,INDEX_SHA)
    df=pd.read_csv(INDEX,usecols=['response_id','session_id'])
    assert len(df)==35072
    assert df['session_id'].nunique()==22821
    T=truth_from_response_id(df['response_id'].astype(str).to_numpy())
    sessions=np.sort(df['session_id'].astype(str).unique())
    smap={s:i for i,s in enumerate(sessions)}
    codes=np.fromiter((smap[x] for x in df['session_id'].astype(str)),dtype=np.int32,count=len(df))
    order=np.argsort(codes,kind='stable')
    sorted_codes=codes[order]
    starts=np.r_[0,np.flatnonzero(np.diff(sorted_codes))+1]
    sizes=np.add.reduceat(np.ones(len(df),dtype=np.int32)[order],starts).astype(np.float64)
    assert len(sizes)==22821 and int(sizes.sum())==35072
    return df,T,codes,order,starts,sizes

def draw_outcomes(T,codes,n_sessions,n_reps,rng):
    Z=rng.normal(size=(n_sessions,n_reps))
    eps=rng.normal(size=(len(T),n_reps))
    L=math.sqrt(RHO)*Z[codes,:]+math.sqrt(1-RHO)*eps
    U=ndtr(L)
    return (U<=T[:,None])

def oracle_values(T,s,Y):
    den=float(np.mean(np.abs(s)))
    noise=np.mean(s[:,None]*(T[:,None]-Y),axis=0)/den
    return noise

def session_noise(T,s,Y,order,starts):
    q=s[:,None]*(T[:,None]-Y)
    return np.add.reduceat(q[order,:],starts,axis=0)

def make_bootstrap_counts(n_sessions):
    rng=rng_for(1824)
    W=np.zeros((B,n_sessions),dtype=np.uint16)
    for b in range(B):
        idx=rng.integers(0,n_sessions,size=n_sessions,dtype=np.int32)
        W[b,:]=np.bincount(idx,minlength=n_sessions).astype(np.uint16)
    assert np.all(W.sum(axis=1)==n_sessions)
    return W

def percentile_valid(x, qs=(0.025,0.975)):
    x=np.asarray(x,dtype=np.float64)
    return tuple(float(v) for v in np.quantile(x,qs))

def run():
    t0=time.time()
    df,T,codes,order,starts,sizes=setup_geometry()
    N=len(T); S=len(sizes)
    result={
      'experiment_id':'GAMMA_CAL_RESOLUTION_DIAGNOSTIC',
      'status':'EXECUTED',
      'source':{'index_sha256':sha256(INDEX),'rows':N,'sessions':S,'columns_read':['response_id','session_id'],'labels_read':False},
      'execution':{
        'rng_derivation':'default_rng(SeedSequence([base_seed,*integer_coordinates]))',
        'session_order':'lexicographic session_id',
        'bootstrap_common_random_numbers':True,
        'bootstrap_counts_dtype':'uint16',
        'bootstrap_B':B,
      },
      'fixture_constitution':{},
      'detection':{},
      'decision':{},
      'resolution_output':{},
    }
    signs=[]
    for hi,h in enumerate(SCALES):
        s=scale_sign(T,float(h)); signs.append(s)
        rec={}
        for C in [0.010,0.01125,0.0125,0.015]:
            _,_,chk=fixture(T,s,C)
            rec[f'C_{C:.5f}']=chk
        result['fixture_constitution'][f'h_{hi}']={'h':float(h),'checks':rec,'all_pass':bool(all(v['bounds_pass'] and v['injective_pass'] and v['construct_pass'] for v in rec.values()))}
    if not all(v['all_pass'] for v in result['fixture_constitution'].values()):
        result['status']='FIXTURE_CONSTITUTION_FAILURE'
        Path(OUTDIR/'final.json').write_text(json.dumps(result,indent=2))
        print(json.dumps({'status':result['status'],'fixture_constitution':result['fixture_constitution']},indent=2),flush=True)
        return result

    det_pass=[]
    for hi,h in enumerate(SCALES):
        s=signs[hi]
        ytr=draw_outcomes(T,codes,S,N_NULL_TRAIN,rng_for(1821,hi))
        null_train=oracle_values(T,s,ytr)
        crit=float(np.quantile(null_train,0.95,method='higher'))
        del ytr
        y0=draw_outcomes(T,codes,S,N_NULL_EVAL,rng_for(1822,hi,0))
        null_eval=oracle_values(T,s,y0); del y0
        y1=draw_outcomes(T,codes,S,N_DETECT,rng_for(1822,hi,1))
        defect=C_DETECT+oracle_values(T,s,y1); del y1
        fpr=float(np.mean(null_eval>crit)); power=float(np.mean(defect>crit))
        pas=bool(fpr<=0.10 and power>=0.80); det_pass.append(pas)
        result['detection'][f'h_{hi}']={'h':float(h),'null_critical':crit,'null_train_mean':float(np.mean(null_train)),'null_train_sd':float(np.std(null_train,ddof=1)),'fpr':fpr,'power':power,'pass':pas}
        print(f'DET h={h:.12g} crit={crit:.6g} fpr={fpr:.3f} power={power:.3f} pass={pas}',flush=True)
    passing=[float(h) for h,p in zip(SCALES,det_pass) if p]
    hmin_detect=min(passing) if passing else None

    print('BUILD bootstrap count matrix',flush=True)
    W=make_bootstrap_counts(S)
    Wf=W.astype(np.float64)
    denom_boot=Wf@sizes
    assert np.all(denom_boot>0)
    print(f'BOOT matrix ready shape={W.shape} elapsed={time.time()-t0:.1f}s',flush=True)

    dec_scale_pass=[]
    for hi,h in enumerate(SCALES):
        s=signs[hi]
        scale_cells={}
        all_cell_pass=True
        for ri,Rtrue in enumerate(RATIOS):
            rng=rng_for(1823,hi,ri)
            Y=draw_outcomes(T,codes,S,N_DECISION,rng)
            qs=session_noise(T,s,Y,order,starts)
            del Y
            noise_point=np.sum(qs,axis=0)/float(np.sum(np.abs(s)))
            Cref_point=C_R+noise_point
            delta=float(Rtrue*C_R)
            qboot=Wf@qs
            Cref_boot=C_R+qboot/denom_boot[:,None]
            invalid=Cref_boot<=0.0
            invalid_frac=np.mean(invalid,axis=0)
            loR=np.full(N_DECISION,np.nan); hiR=np.full(N_DECISION,np.nan)
            loC=np.full(N_DECISION,np.nan); hiC=np.full(N_DECISION,np.nan)
            cover=np.zeros(N_DECISION,dtype=bool); ni=np.zeros(N_DECISION,dtype=bool); denom_guard=np.zeros(N_DECISION,dtype=bool); interval_valid=np.zeros(N_DECISION,dtype=bool)
            for j in range(N_DECISION):
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
            coverage=float(np.mean(cover))
            ni_rate=float(np.mean(ni))
            denom_rate=float(np.mean(denom_guard))
            valid_rate=float(np.mean(interval_valid))
            invalid_ok=bool(np.all(invalid_frac<=0.01))
            coverage_ok=bool(0.90<=coverage<=0.99)
            ni_ok=bool(ni_rate>=0.80) if Rtrue in (0.0,0.125) else bool(ni_rate<=0.10)
            denom_ok=bool(denom_rate>=0.95)
            cell_pass=bool(invalid_ok and coverage_ok and ni_ok and denom_ok)
            all_cell_pass &= cell_pass
            scale_cells[f'R_{Rtrue:g}']={
                'R_true':float(Rtrue),'coverage':coverage,'NI_pass_rate':ni_rate,'denominator_guard_rate':denom_rate,'interval_valid_rate':valid_rate,
                'max_invalid_bootstrap_fraction':float(np.max(invalid_frac)),'invalid_fraction_mean':float(np.mean(invalid_frac)),
                'coverage_pass':coverage_ok,'NI_pass':ni_ok,'denominator_pass':denom_ok,'invalid_bootstrap_pass':invalid_ok,'pass':cell_pass,
                'point_Cref_mean':float(np.mean(Cref_point)),'point_Cref_sd':float(np.std(Cref_point,ddof=1)),
                'median_interval_width_R':float(np.nanmedian(hiR-loR)),'median_lower_Cref':float(np.nanmedian(loC)),
            }
            print(f'DEC h={h:.12g} R={Rtrue:.3f} cov={coverage:.3f} NI={ni_rate:.3f} denom={denom_rate:.3f} invmax={np.max(invalid_frac):.4f} pass={cell_pass}',flush=True)
            del qs,qboot,Cref_boot
        result['decision'][f'h_{hi}']={'h':float(h),'cells':scale_cells,'pass':bool(all_cell_pass)}
        dec_scale_pass.append(bool(all_cell_pass))
        print(f'DEC-SCALE h={h:.12g} pass={all_cell_pass}',flush=True)
        tmp=dict(result)
        tmp['resolution_output']={'h_min_detect':hmin_detect,'h_min_decision':None,'detection_pass_vector':det_pass,'decision_pass_vector':dec_scale_pass}
        Path(OUTDIR/'checkpoint.json').write_text(json.dumps(tmp,indent=2))
    passing_dec=[float(h) for h,p in zip(SCALES,dec_scale_pass) if p]
    hmin_dec=min(passing_dec) if passing_dec else None
    def nonmono(v):
        seen_fail=False
        for x in v:
            if not x: seen_fail=True
            elif seen_fail: return True
        return False
    result['resolution_output']={
        'h_min_detect':hmin_detect if hmin_detect is not None else 'NONE_IDENTIFIED',
        'h_min_decision':hmin_dec if hmin_dec is not None else 'NONE_IDENTIFIED',
        'detection_pass_vector':det_pass,
        'decision_pass_vector':dec_scale_pass,
        'detection_nonmonotone':nonmono(det_pass),
        'decision_nonmonotone':nonmono(dec_scale_pass),
        'scales':[float(x) for x in SCALES],
    }
    result['elapsed_seconds']=time.time()-t0
    Path(OUTDIR/'final.json').write_text(json.dumps(result,indent=2))
    print('FINAL',json.dumps(result['resolution_output'],indent=2),flush=True)
    print(f'elapsed={result["elapsed_seconds"]:.1f}s',flush=True)
    return result

if __name__=='__main__':
    run()
