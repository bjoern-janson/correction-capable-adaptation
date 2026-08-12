# D_main execution apparatus diagnostic

## Status

**APPARATUS BOUNDARY OPEN — SCIENTIFIC RESULT STILL UNOBSERVED**

The prospectively frozen `M2_D_MAIN` scientific object is unchanged. This artifact opens only the execution-apparatus boundary after repeated exact-cell attempts produced no result artifact.

## Preserved scientific identity

The following remain immutable for this apparatus successor:

```text
eligible cohort: 319 objectives / 34,978 responses / 22,783 sessions
arms: B0, C0, B1, C1 exactly as frozen
same canonical folds
same HashingVectorizer representation
same ordinary covariates and semantic features
same centered historical R_TO residual
same SGDClassifier family
same SGDClassifier hyperparameters
same random_state=17
same raw-sigmoid-log-loss primary measurement
same paired session-cluster bootstrap
same Delta0, Delta1, Psi adjudication
```

No scientific simplification is authorized to satisfy runtime.

## Localized execution evidence

For `B0 / outer fold 0`, exact preprocessing and matrix construction complete normally:

```text
pre-fit assembly             11.34 s
train shape                  27,987 x 262,198
train nonzeros               73,098,728
CSR sorted indices           true
CSR canonical format         true
explicit stored zeros        0
```

Local execution environment:

```text
logical CPUs                  5
RAM                           ~5.9 GiB
Python                        3.13.5
scikit-learn                  1.8.0
SciPy                         1.17.0
NumPy                         2.3.5
```

The exact frozen `SGDClassifier.fit()` did not return within a 900-second cell window. The cell writes only after successful fit completion.

Therefore:

```text
persisted prediction cells    0
P_main                        absent
D_R                           unavailable
D_H                           unavailable
Delta W                       0
```

This is apparatus evidence only.

## Discriminated implementation hypotheses

The current evidence weighs against preprocessing, objective-centering, serialization, and malformed sparse-layout explanations as the dominant bottleneck. The implicated boundary is the throughput/resource envelope of the exact estimator execution on the current container.

It does not establish that the scientific object is intrinsically infeasible on a larger or more suitable exact execution environment.

## Authorized apparatus successor

A successor execution may change only mechanics that preserve the exact scientific object, including:

```text
hardware CPU/RAM envelope
process scheduling
cell/arm/fold partitioning
caching of immutable input matrices
serialization/checkpoint layout
sparse storage/layout when numerical feature values are unchanged
```

Every successful result-bearing cell must verify the same sealed input/config identities before fitting.

The successor may not change:

```text
model family or hyperparameters
max_iter or tol
average setting
random seed
feature construction or values
cohort or folds
measurement or diagnostic gates
```

## Stop rule

If an exact sealed cell completes under a larger/suitable apparatus, continue the already-frozen 20-cell execution and aggregate only after all required cells are present.

If exact execution remains infeasible after a materially larger resource envelope with identical software/model identity, reopen the implementation-validity boundary explicitly. Do not silently replace the estimator.

## Authority ceiling

Opening this apparatus boundary earns no weight for or against `D_main`, broad `H_O`, calibration, CCA, or any CCA-derived feature family.

\[
\boxed{\text{blocked execution} \neq \text{negative scientific evidence}}
\]
