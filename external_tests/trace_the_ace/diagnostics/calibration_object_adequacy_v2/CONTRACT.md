# ECE-10 measurement-object adequacy V2 — construct-faithful fixture

## Status

**PROSPECTIVE CORRECTED METHODOLOGICAL DIAGNOSTIC — RESULT UNOBSERVED**

V2 repairs only the synthetic truth-criterion fidelity defect diagnosed in V1. Historical OOF access remains forbidden. ECE-10, its ten fixed equal-width bins, and `epsilon_ECE=0.003997462025` remain unchanged.

## Construct-faithful synthetic object

Candidate prediction `P` is deterministic and primitive, spanning 0.15 to 0.85 by canonical session rank. For each predeclared defect shape `h(P)` and amplitude `a`, define the conditional outcome probability

\[
Q(P)=P-a h(P).
\]

Thus by construction

\[
E[Y\mid P]=Q(P)
\]

and the bin-free absolute calibration deviation is exactly

\[
C_{cal,L1}=E_w|P-Q(P)|.
\]

The reference predictor is `P_ref=Q(P)`, which is perfectly calibrated for the same synthetic outcomes.

## Frozen challenge family

The same prospectively declared defect families are retained:

```text
global_shift              h(p)=+1
linear_tilt               h(p)=2p-1
smooth_low_frequency      h(p)=sin(4*pi*p)
localized_band            h(p)=1[p in 0.45..0.65]
within_bin_alternating    h(p)=sign(sin(40*pi*p))
```

For each family, a deterministic amplitude search realizes known `C_cal,L1` targets `0.5 epsilon`, `epsilon`, and `2 epsilon` within absolute error `5e-6`. Candidate `Q(P)` must stay in `(0.001,0.999)`.

## Measurement under test

Population fixed-bin ECE-10 is

\[
ECE_{10}(P,Q)=\sum_b|E_w[(P-Q(P))\mathbf1(P\in B_b)]|.
\]

## Adequacy gates

For every declared family:

1. at true `0.5 epsilon`, `ECE_10 < epsilon`;
2. at true `2 epsilon`, `ECE_10 >= epsilon`;
3. ECE-10 is nondecreasing across the three target levels.

All families must pass for adequacy on the declared scope. Any prospectively declared material calibration defect that ECE-10 classifies as non-inferior yields local support for `D_object`.

## Authority ceiling

A failure can earn local evidence that ECE-10 is not fidelity-preserving for the standard calibration construct on the declared family and authorize a replacement-measurement successor. It cannot itself authorize a replacement object, change the historical calibration decision, constitute `M_mature`, or open CCA-derived features.
