# M2 execution status

## Status

**EXECUTED UNDER THE FROZEN CONTRACT — DIAGNOSED UNRESOLVED**

The M2 scientific/model object was frozen before any M2 result was observed. The original local execution attempts failed at the harness layer and remained epistemically inert.

The harness boundary was then diagnosed without changing the scientific contract.

### Execution diagnosis

The inherited transcript representation was initially rebuilt by sequentially serializing all 22,821 transcript CSVs before hashing. A deterministic parallel cache was introduced using the already-frozen transcript serialization and `HashingVectorizer` parameters.

Semantic equivalence was checked directly: cached CSR rows sampled from each of all five cache blocks were exactly equal to the frozen sequential construction, including values and sparse indices.

A monolithic arm/fold job still exceeded the tool transport window, so execution was partitioned by outer fold and arm. Each checkpoint executed the exact frozen outer fit, the exact five inner session-grouped fits, and the exact Platt calibrator. No model, split, seed, representation, threshold, or metric changed.

An attempt to run both arms concurrently caused one process to exit 137 under the local memory envelope. That scheduling strategy was rejected. Final execution used one arm at a time.

All 60 base-model fits across both arms and all outer/inner folds converged before the frozen `max_iter=500` ceiling.

## Scientific result

The implementation-validity gate passes.

The objective-aware system shows a large total predictive gain over the mature ordinary baseline:

```text
M1-cal log loss      0.5683582154
M2_O log loss        0.5366109542
M2 log loss          0.5365875999
```

For M2 versus M1-cal:

```text
Delta LL             -0.0317706155
95% cluster CI       [-0.0341115353, -0.0293137824]
```

So total objective information passes its prospective gate.

However, the primary H_O comparison is M2 versus the objective-main-effect control M2_O:

```text
Delta LL             -0.0000233543
95% cluster CI       [-0.0001257767, 0.0000855770]
```

The point estimate is slightly favorable, but the confidence interval crosses zero. Therefore the specified sparse elementwise interaction does **not** pass the prospective H_O gate.

Calibration preservation is also mixed:

```text
                         M1-cal          M2
Brier                    0.1921277205    0.1792376299   PASS
ECE-10                   0.0159898481    0.0170492544   FAIL
absolute mean bias       0.0105359299    0.0099583593   PASS
```

Because ECE-10 worsens relative to the frozen parent, the calibration-preservation gate fails exactly as prospectively specified.

## Diagnosis

```text
implementation validity        PASS
total objective information    PASS
H_O interaction gate           FAIL
calibration preservation       FAIL
M2 baseline gate               UNRESOLVED
CCA feature-family authority   FALSE
```

The large objective-main-effect gain must not be relabeled as evidence for objective-conditioned transcript interpretation. Likewise, the small ECE degradation must not be waived after observing the result.

The current result supports only that objective information carries substantial predictive information under this operationalization. It does not establish that `Z_T * Z_O` adds nonredundant objective-conditioned relevance beyond the objective main effect.

No CCA-derived feature family is authorized by this result.
