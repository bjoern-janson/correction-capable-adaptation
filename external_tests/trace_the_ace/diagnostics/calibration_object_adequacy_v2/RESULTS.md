# ECE-10 object adequacy V2 result

## Status

**CLOSED — CONSTRUCT-FAITHFUL LOCAL SUPPORT FOR `D_object` — REPLACEMENT SUCCESSOR AUTHORIZED, REPLACEMENT ITSELF NOT AUTHORIZED**

## Correction lineage

The predecessor V1 object-adequacy experiment used `E|P-Q_latent|` as its synthetic truth criterion. That can exceed standard calibration error when latent states with different risks map to the same prediction, so V1's claimed `D_object` authority is withheld for construct-fidelity failure. Its numerical result remains preserved as historical methodology work.

V2 corrected only that boundary. Candidate prediction `P` is primitive and the conditional outcome probability is explicitly defined as `Q(P)=E[Y|P]`. Therefore

\[
C_{cal,L1}=E_w|P-Q(P)|
\]

is a valid bin-free calibration truth object for the synthetic candidate.

Historical OOF predictions remained forbidden and were not read.

## Result

At true material degradation `2 epsilon`, ECE-10 correctly detects the global-shift, linear-tilt, smooth-low-frequency, and localized-band defects.

For the prospectively declared within-bin alternating calibration defect:

```text
true calibration L1 at 0.5 epsilon   0.0020000000
ECE-10                                0.0000128878

true calibration L1 at epsilon       0.0039950000
ECE-10                                0.0000257433

true calibration L1 at 2 epsilon     0.0079950000
ECE-10                                0.0000515189
ECE / true calibration ratio         0.0064438869
```

Thus a genuine standard-calibration defect of approximately `2 * epsilon` is measured at only ~0.64% of its bin-free absolute magnitude and ECE-10 incorrectly indicates non-inferiority.

```text
D_object = SUPPORT_ON_DECLARED_SCOPE
```

## Diagnosis

The construct-faithful successor independently re-establishes the within-bin cancellation failure after invalidating the predecessor truth criterion. Fixed equal-width ECE-10 is not fidelity-preserving for the declared calibration family because heterogeneous `P-Q(P)` residuals can cancel inside its fixed bins.

This conclusion is scoped. It does not imply that ECE-10 is useless generally, nor does it authorize a replacement metric by itself.

## Current calibration topology

```text
D_efficiency    tested IF route failed prospective method gates
D_object        SUPPORT on corrected declared scope
D_additional    UNOPENED
```

The next authorized calibration edge is a prospective replacement-measurement successor. No historical re-adjudication may occur until that successor independently earns measurement authority.

## Authority ceiling

Gained:

- corrected local support for `D_object`;
- authority to open a replacement-measurement successor.

Not gained:

- authority to remove ECE-10 from the governing historical rule;
- authority for any replacement measurement;
- calibration closure or `M_mature` constitution;
- CCA-feature authorization.

Local record SHA-256:

```text
a4b5dda01bf08da6ac7a8e6f140260210069e2284946223ea07bcadfdd41ffa0
```
