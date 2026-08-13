# M2-SEM — Semantic objective-conditioning result

## Status

**EXECUTED — PRIMARY H_O_SEM GATE FAIL — DIAGNOSED UNRESOLVED**

The prospectively frozen semantic successor was executed over the same 35,072 response rows / 22,821 session-grouped validation apparatus. No CCA-derived feature family was present.

Frozen comparison:

```text
M2_O  = [Z_T, Z_O, X_ordinary]
M2_S  = [Z_T, Z_O, X_ordinary, Z_S]
M2_SC = [Z_T, Z_O, X_ordinary, Z_S, R_TO]

R_TO = Z_C(O) - Z_S
```

The primary comparison is `M2_SC vs M2_S`. The semantic-capacity comparisons against historical `M2_O` are diagnostic and cannot substitute for the primary gate.

## Raw, uncalibrated comparison

The raw outer-fold decision scores were converted to sigmoid probabilities and recorded **before any Platt calibrator was fit**.

```text
M2_S  raw log loss      0.5547119693
M2_SC raw log loss      0.5546563889
Delta SC - S           -0.0000555803
```

Paired 2,000-replicate session-cluster bootstrap:

```text
95% CI  [-0.0002456427, 0.0001471991]
clusters 22,821
```

The point estimate is slightly favorable to conditioning, but the interval crosses zero. This raw comparison is a diagnostic kept separate from the inherited calibration layer.

## Calibrated primary H_O_SEM test

Using the inherited leakage-safe inner-OOF Platt procedure:

```text
M2_S  log loss           0.5359576100
M2_SC log loss           0.5359414160
Delta SC - S            -0.0000161940

M2_S  AUC                0.7347266225
M2_SC AUC                0.7347911571
```

Paired 2,000-replicate session-cluster bootstrap:

```text
95% CI  [-0.0001311129, 0.0001051583]
clusters 22,821
```

The prospective primary rule required both a favorable point estimate and a strictly negative 95% CI upper bound. The second condition fails.

```text
H_O_SEM gate: FAIL
```

This failure reaches only the frozen semantic-conditioning operationalization. It does not establish that objective-conditioned relevance is generally absent.

## Fold-wise conditioned-minus-control differences

```text
         raw Delta LL       calibrated Delta LL
fold 0   -0.0004211827      -0.0001149221
fold 1   -0.0004752146      -0.0000410870
fold 2   +0.0000356928      +0.0000803745
fold 3   +0.0006094706      +0.0001641409
fold 4   -0.0000265482      -0.0001694689
```

The mixed signs are consistent with the pooled cluster-bootstrap null and do not support elevating the tiny pooled point gain into stable interaction evidence.

## Matched semantic-capacity diagnostic

Historical objective-main-effect control:

```text
M2_O log loss            0.5366109542
```

Objective-independent semantic control:

```text
M2_S log loss            0.5359576100
Delta M2_S - M2_O       -0.0006533442
95% CI                  [-0.0010827476, -0.0002291105]
```

Total semantic successor:

```text
M2_SC log loss           0.5359414160
Delta M2_SC - M2_O      -0.0006695382
95% CI                  [-0.0010977837, -0.0002406518]
```

The matched control therefore supplies local evidence that this objective-independent semantic representation adds predictive information beyond historical `M2_O`. That gain is not evidence for objective-conditioned semantic selection because `M2_SC` does not reliably beat `M2_S`.

## Calibration diagnostics — separate branch

```text
                         historical M2_O      M2_S             M2_SC
Brier                    0.1792456843         0.1790775429      0.1790710499
ECE-10                   0.0170412672         0.0169437791      0.0177334943
mean probability         0.6924696960         0.6922186077      0.6917299240
observed rate            0.7024692062         0.7024692062      0.7024692062
absolute mean bias       0.0099995102         0.0102505985      0.0107392822
```

These are diagnostics only. Historical M2's calibration-preservation failure remains a separately identified unresolved branch and is not repaired by this experiment.

## Implementation validity

All frozen implementation gates needed for interpretation passed:

```text
constituted GloVe resource identity             PASS
all 398 objective embeddings nonzero            PASS
all sessions have semantic utterance evidence   PASS
Z_S objective-independent by construction       PASS
R_TO nonzero                                    PASS
R_TO multi-objective variation                  PASS
outer session isolation                         PASS
inner session isolation                         PASS
all 60 base-model fits converged                 PASS
maximum base-model iteration count              113 / 500
```

The label-free semantic feature apparatus was frozen before any estimator fit. Its artifact identities are:

```text
session semantic features SHA-256
  d4eafecc328ae42df8456673bff97adc1095d53aeb3609efc2f7953fc50e10d4
response conditioning features SHA-256
  794b3605f733ad53927f93a8a20a8c0998b4660bf4f351f885ad610bf5362b8c
```

Generated result rows remain local and are not committed:

```text
OOF predictions SHA-256
  64679b828af9737e5245dd1348f2c8e0cf5a38e013eefaee02266de7277e096f
M2-SEM record SHA-256
  7a5720140e589afeaf352418c9f509528c807da83672b10e63892b4ec8669f17
```

## Diagnosis and authority

```text
resource / feature validity              PASS
estimator convergence                    PASS
generic semantic-capacity diagnostic     PASS
raw conditioning comparison              NOT ESTABLISHED
H_O_SEM calibrated primary gate          FAIL
historical calibration branch            UNRESOLVED
CCA-derived feature-family authority     FALSE
```

Earned local conclusion:

> Under this frozen apparatus, objective-independent semantic pooling adds modest held-out predictive information beyond the historical objective-main-effect baseline. The specified objective-conditioned semantic reweighting residual does not establish stable incremental predictive value beyond that matched semantic control.

Not earned:

```text
CCA support or refutation
causal evidence
G1 evidence
PMC evidence
repeated-correction evidence
JT evidence
C_improve measurement
authorization of Z_E, Z_D, Z_C, or Z_P
```
