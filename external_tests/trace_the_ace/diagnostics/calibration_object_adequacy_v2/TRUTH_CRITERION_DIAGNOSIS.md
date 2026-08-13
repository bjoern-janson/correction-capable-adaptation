# Correction to ECE object-adequacy truth criterion

## Status

**SHALLOWEST FAILURE LOCUS: SYNTHETIC TRUTH-CRITERION / CONSTRUCT FIDELITY**

The closed V1 object-adequacy experiment used

\[
E|P-Q_{latent}|
\]

as a synthetic truth criterion after constructing candidate predictions as a transformation of latent outcome probabilities. That object is generally stronger than standard calibration error.

Standard calibration is defined relative to the prediction itself:

\[
E[Y\mid P]=P.
\]

A bin-free absolute calibration deviation is therefore

\[
C_{cal,L1}=E|P-E[Y\mid P]|.
\]

If multiple latent states with different `Q_latent` map to the same prediction `P`, then

\[
E|P-E[Q_{latent}\mid P]|\le E[|P-Q_{latent}|\mid P],
\]

with strict inequality possible through legitimate conditional averaging.

Therefore a large `E|P-Q_latent|` does not by itself establish miscalibration. The V1 within-bin alternating construction can confound calibration with unresolved latent heterogeneity / individual probability accuracy.

## Consequence for V1 authority

The numerical V1 result remains immutable historical methodology work, but its claimed local `D_object` support is not licensed because the synthetic truth criterion did not establish construct fidelity to calibration.

```text
V1 numerical result                     PRESERVED
V1 truth-criterion fidelity             FAIL
V1 D_object support authority           WITHHELD
historical OOF effect                   NONE (never read)
metric replacement authority            FALSE
```

## Minimal successor

A corrected fixture must make candidate prediction `P` primitive and define the synthetic conditional outcome probability explicitly as a function `Q(P)=E[Y|P]`. Then

\[
E|P-Q(P)|
\]

is a valid bin-free population calibration object for the synthetic candidate.

Only that corrected fixture may adjudicate whether fixed-bin ECE-10 has a within-bin cancellation fidelity failure for the calibration claim.
