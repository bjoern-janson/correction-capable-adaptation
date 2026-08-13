# ECE-10 measurement-object adequacy diagnostic

## Status

**PROSPECTIVE METHODOLOGICAL DIAGNOSTIC — RESULT UNOBSERVED — NO REPLACEMENT METRIC AUTHORIZED**

This successor opens only `D_object` after the same-target influence-function efficiency route failed prospective validity under a repaired synthetic challenge.

It does not change the historical calibration gate, read historical OOF predictions, relax `epsilon_ECE`, or authorize any replacement measurement object.

## Candidate latent claim

The intended calibration-specific claim is provisionally represented, for synthetic validation only, by the bin-free population absolute calibration deviation

\[
C_{L1}(P,Q)=E_w|P-Q|,
\]

where `Q` is the known conditional outcome probability and `w` uses the canonical label-free response-count weights by session.

This object is used only as a known synthetic truth criterion for testing whether fixed equal-width ECE-10 preserves the practical decision carried by the current gate. It is **not** authorized as the historical replacement metric by this experiment.

The practical scale remains unchanged:

\[
\epsilon=\epsilon_{ECE}=0.003997462025.
\]

## Measurement under test

For candidate probabilities `P`, population fixed-bin ECE-10 is

\[
ECE_{10}(P,Q)=\sum_{b=1}^{10}|E_w[(P-Q)\mathbf1(P\in B_b)]|.
\]

The reference treatment is perfectly calibrated (`P_ref=Q`), so both reference calibration objects are zero.

## Frozen synthetic challenge family

Use deterministic `Q` values spanning `0.15` to `0.85` by canonical session rank. For each predeclared defect shape `h(Q)`, select a scalar amplitude deterministically so that the **known population** `C_L1` degradation is nearest each target:

```text
0.5 * epsilon
1.0 * epsilon   (boundary diagnostic)
2.0 * epsilon
```

with absolute target error <= `5e-6`.

Defect families:

```text
global_shift              h(q) = +1
linear_tilt               h(q) = 2q - 1
smooth_low_frequency      h(q) = sin(4*pi*q)
localized_band            h(q) = 1[q in 0.45..0.65]
within_bin_alternating    h(q) = sign(sin(40*pi*q))
```

All candidate probabilities must remain in `(0.001,0.999)`.

The final family is an explicit challenge to within-bin cancellation; it is included prospectively rather than selected after observing ECE behavior.

## Adequacy gates

For every declared family:

1. **Sub-margin protection:** at true `C_L1 = 0.5 epsilon`, ECE-10 must also indicate non-inferiority: `ECE_10 < epsilon`.
2. **Material-degradation detection:** at true `C_L1 = 2 epsilon`, ECE-10 must not indicate non-inferiority: `ECE_10 >= epsilon`.
3. **Directional ordering:** ECE-10 at the three target levels must be nondecreasing.

All declared families must satisfy all three gates for `ECE10_ADEQUATE_ON_DECLARED_SCOPE`.

Any material false-noninferiority in a declared family yields `ECE10_INADEQUATE_ON_DECLARED_SCOPE` and supports `D_object` locally.

## Interpretation boundary

A failure demonstrates a scoped mismatch between fixed-bin ECE-10 and the bin-free absolute calibration-degradation claim under the declared synthetic family. It does not by itself authorize removal of ECE-10, adoption of `C_L1`, or any historical re-adjudication.

A positive adequacy result would only lower local weight on `D_object`; it would not close calibration by itself.

## Authority ceiling

This experiment can earn only local methodological evidence about ECE-10 measurement-object adequacy. It cannot change the historical calibration state, authorize additional evidence, constitute `M_mature`, or open `Z_E/Z_D/Z_C/Z_P`.
