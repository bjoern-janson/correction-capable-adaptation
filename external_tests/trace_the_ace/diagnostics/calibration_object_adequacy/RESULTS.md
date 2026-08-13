# ECE-10 measurement-object adequacy result

## Status

**CLOSED — LOCAL SUPPORT FOR `D_object` — ECE-10 REPLACEMENT NOT YET AUTHORIZED**

This diagnostic used only a synthetic known-probability population and the canonical label-free session response-count weights. Historical OOF predictions were forbidden and were not read.

## Candidate truth criterion

For diagnostic purposes only, bin-free population absolute calibration deviation was used as known synthetic truth:

\[
C_{L1}(P,Q)=E_w|P-Q|.
\]

The practical scale remained the existing

\[
\epsilon=0.003997462025.
\]

This experiment does not authorize `C_L1` as the historical replacement measurement.

## Declared challenge result

At true material degradation `2 epsilon`, ECE-10 correctly detected degradation for:

```text
global shift            PASS
linear tilt             PASS
smooth low frequency    PASS
localized band          PASS
```

but failed for the prospectively declared within-bin alternating defect.

For that family:

```text
true C_L1 at 0.5 epsilon    0.0020000000
ECE-10                      0.0000128878

true C_L1 at epsilon        0.0039950000
ECE-10                      0.0000257433

true C_L1 at 2 epsilon      0.0079950000
ECE-10                      0.0000515189
ECE / true L1 ratio         0.0064438869
```

Thus at a true calibration degradation of approximately `2 * epsilon`, fixed-bin ECE-10 reports only about **0.64%** of the bin-free absolute deviation and incorrectly satisfies the existing non-inferiority threshold.

The family remains directionally ordered, so the failure is not sign reversal; it is severe within-bin cancellation / under-resolution.

## Diagnosis

```text
D_object = SUPPORT_ON_DECLARED_SCOPE
```

Fixed equal-width ECE-10 is not fidelity-preserving for the declared bin-free calibration-degradation claim when heterogeneous residuals cancel within bins.

This result follows the earlier V3 efficiency diagnosis: the same ECE object also creates frequent nonregularity for a first-order IF precision repair under bin-crossing perturbations.

Together these findings localize the unresolved calibration boundary toward **measurement-object adequacy**, rather than another calibrator or a simple same-target variance estimator.

## Authority ceiling

Gained:

- local support for `D_object` on the declared synthetic challenge family;
- authorization to open a prospective replacement-measurement successor.

Not gained:

- authority to remove ECE-10 from the governing historical calibration rule;
- authority for `C_L1` or any other replacement object;
- historical calibration resolution;
- mature baseline constitution;
- `Z_E/Z_D/Z_C/Z_P` authorization;
- CCA or causal authority.

Local record SHA-256:

```text
4cf7b16164690fa968b78efe5bd28bb892bfb598960a442a56f2d5d012383565
```
