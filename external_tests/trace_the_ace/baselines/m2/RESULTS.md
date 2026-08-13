# M2 — Objective-conditioning result

## Status

**EXECUTED — DIAGNOSED UNRESOLVED**

The M2 contract was frozen before execution. No CCA-derived feature family is present.

## Frozen comparisons

```text
M1-cal = [Z_T, X_ordinary]
M2_O   = [Z_T, Z_O, X_ordinary]
M2     = [Z_T, Z_O, Z_T * Z_O, X_ordinary]
```

The primary H_O comparison is `M2 vs M2_O`. `M2 vs M1-cal` measures total objective information and cannot by itself establish objective-conditioned relevance.

## Pooled OOF results

```text
M1-cal log loss           0.5683582154
M2_O log loss             0.5366109542
M2 log loss               0.5365875999

M2_O - M1-cal            -0.0317472612
M2   - M1-cal            -0.0317706155
M2   - M2_O              -0.0000233543
```

AUC:

```text
M1-cal                    0.6765200311
M2_O                      0.7337559709
M2                        0.7337645478
```

## Uncertainty

Paired 2,000-replicate session-cluster bootstrap:

```text
M2 vs M1-cal
95% CI  [-0.0341115353, -0.0293137824]
PASS

M2_O vs M1-cal
95% CI  [-0.0340643821, -0.0293823143]
DIAGNOSTIC STRONG GAIN

M2 vs M2_O
95% CI  [-0.0001257767,  0.0000855770]
FAIL H_O GATE
```

The interaction point estimate is slightly favorable, but its interval crosses zero. Under the prospective rule, H_O does not pass.

## Fold-wise M2 minus M2_O log-loss difference

```text
fold 0   -0.0000552141
fold 1   -0.0000821975
fold 2   +0.0000987207
fold 3   +0.0000279741
fold 4   -0.0001060381
```

The mixed signs are consistent with the pooled bootstrap result and do not support treating the tiny pooled point gain as stable interaction evidence.

## Calibration

```text
                         M1-cal          M2
Brier                    0.1921277205    0.1792376299
ECE-10                   0.0159898481    0.0170492544
absolute mean bias       0.0105359299    0.0099583593
```

Prospective calibration-preservation gates:

```text
Brier not worse          PASS
ECE-10 not worse         FAIL
mean-bias not worse      PASS
```

The ECE failure is small in magnitude but remains a failure because the non-degradation rule was frozen before execution.

## Implementation validity

All implementation gates pass:

```text
objective ID/text mapping one-to-one        PASS
objective block nonzero                     PASS
interaction block nonzero                   PASS
within-session objective-feature variation  PASS
all 60 base-model fits converged             PASS
```

Representation audit:

```text
unique objective IDs       398
unique objective texts     398
objective matrix nnz       417,406
interaction matrix nnz     373,693
```

The execution harness was repaired without changing the scientific object. A deterministic cached `Z_T` was validated for exact sparse-row equality against the frozen sequential construction across samples from all five cache blocks. Fold/arm checkpointing changed only execution scheduling.

## Diagnosis

```text
implementation validity        PASS
total objective information    PASS
H_O interaction gate           FAIL
calibration preservation       FAIL
M2 baseline gate               UNRESOLVED
CCA feature-family authority   FALSE
```

The earned conclusion is:

> Under the frozen operationalization, learning-objective information adds substantial held-out predictive information beyond the mature ordinary semantic baseline. The specified sparse elementwise transcript-objective interaction does not establish incremental predictive value beyond the objective main effect.

This result does not support or refute CCA, G1, PMC, repeated correction, JT, or `C_improve`.

## Local result artifact identities

Generated competition-derived rows remain local and are not committed.

```text
OOF predictions SHA-256  87e6fc4621f7e7ebf8d0fbe84ba0ace87b055c9a287f12217e9016a53d7eaa04
M2 record SHA-256        67e80c6e6d7698a4eba4e9c175c9f211ac4d9bb6affefe40ad9abd1bb60fde98
Z_T cache SHA-256        4b7e8b23ea93740f86afa0a99c8352031925e079a66aa252362b964f1fb97e18
```
