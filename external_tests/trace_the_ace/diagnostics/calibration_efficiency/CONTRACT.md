# ECE measurement-efficiency diagnostic

## Status

**PROSPECTIVE METHOD DIAGNOSTIC — RESULT UNOBSERVED**

This successor opens only `D_efficiency` after the authorized `Gamma_cal_NI` method established that the historical ECE-10 non-inferiority comparison remained unresolved at the inherited practical margin.

It does not change the probability treatment, ECE-10 bins, target, tolerance, dataset, folds, or evidence source. It does not open `D_additional` or `D_object`, and it authorizes no CCA-derived feature.

## Fixed target

For model `m`, with ten fixed equal-width probability bins `B_b`, define the population ECE-10 functional

\[
\theta_m = \sum_{b=1}^{10}\left|E[(P_m-Y)\mathbf 1(P_m\in B_b)]\right|.
\]

The unchanged contrast is

\[
\Delta_{ECE}=\theta_{M2_S}-\theta_{M1^{cal}}.
\]

The unchanged practical non-inferiority margin is

\[
\epsilon_{ECE}=0.003997462025.
\]

No observed result may widen this margin or select another calibration metric.

## Candidate efficiency estimator

The candidate changes only the uncertainty estimator: use the paired session-cluster influence-function / sandwich variance for the same plug-in ECE-10 point contrast.

For each model and bin, let

\[
\mu_{m,b}=E[(P_m-Y)\mathbf1(P_m\in B_b)].
\]

For session `j` with response count `n_j` and bin residual sum `S_{m,j,b}`, the response-weighted cluster influence contribution is

\[
IF_{m,j}=\frac{1}{E[n_j]}\sum_b \operatorname{sign}(\mu_{m,b})\{S_{m,j,b}-\mu_{m,b}n_j\}.
\]

The paired contrast uses `IF_candidate - IF_reference`; its cluster sandwich standard error yields the frozen two-sided 95% interval.

## Nonregularity guard

Because absolute value is non-differentiable at zero, the influence-function method is not permitted to launder a near-zero bin residual into artificial precision.

For every nonempty bin of both probability objects, require

\[
|\hat\mu_{m,b}|/SE(\hat\mu_{m,b})\ge 1.96.
\]

Failure of this guard yields `HISTORICAL_NONREGULAR`; the candidate method cannot adjudicate the historical comparison.

## Prospective synthetic validity

Before the sealed historical OOF vectors are read, the method must pass clustered synthetic fixtures with the canonical label-free session-size distribution.

Regular fixtures use predictions `0.20 + 0.55*Beta(2,2)` and a known nonzero base calibration residual of `0.02`, making the ECE functional differentiable, and true candidate-minus-reference deltas of `0`, `0.5 epsilon`, `epsilon`, and `2 epsilon`. Across 100 prospectively fixed seeds, the method must satisfy the coverage and NI-behavior gates in `config.yaml`.

A separate 30-seed perfectly calibrated negative-control fixture must trigger the nonregularity guard in at least 90% of datasets.

Synthetic failure makes the method `METHOD_INVALID`; historical adjudication is then forbidden.

## Historical discriminator

Only after synthetic validity passes:

1. verify the sealed M1-cal and M2-S OOF hashes;
2. compute the unchanged plug-in `Delta_ECE`;
3. apply the regularity guard;
4. compute the paired cluster-IF 95% interval;
5. compare its width to the predecessor bootstrap width `0.0082562593`;
6. compare its upper bound to the unchanged `epsilon_ECE`.

Outcomes:

```text
METHOD_INVALID             synthetic method validity fails
HISTORICAL_NONREGULAR      influence-function regularity fails on historical data
NOT_MORE_EFFICIENT         valid/regular but IF interval is not narrower than predecessor
EFFICIENT_NOT_IDENTIFYING  narrower valid interval, but upper >= epsilon_ECE
EFFICIENT_AND_IDENTIFYING  narrower valid interval and upper < epsilon_ECE
```

Only the last outcome can support closing the ECE precision boundary through `D_efficiency`. None of these outcomes changes the tolerance or licenses a metric switch.

## Authority ceiling

This experiment can earn only local evidence about whether the same ECE-10 non-inferiority claim can be identified more efficiently from the same observations.

It cannot earn mature-baseline authority by itself, authorize a new calibrator, authorize additional data collection, replace ECE-10, or authorize `Z_E/Z_D/Z_C/Z_P`.
