# ECE efficiency diagnostic V2 — fixture repair

## Status

**PROSPECTIVE VALIDATION-APPARATUS SUCCESSOR — RESULT UNOBSERVED**

V1 failed because its uniform-shift synthetic fixture made the paired ECE difference algebraically deterministic under stable bin signs. This successor changes only that synthetic validation fixture.

Unchanged:

```text
candidate uncertainty method: paired session-cluster IF/sandwich
ECE target: fixed equal-width ECE-10
practical margin: epsilon_ECE = 0.003997462025
historical M1-cal and M2-S probability vectors and hashes
regularity guard
historical decision rules
```

## Repaired synthetic population

The synthetic reference predictions are deterministic across the canonical label-free session-size distribution, spanning 0.15 to 0.85 by session rank.

For each reference ECE bin, the true residual `p_ref - q` is fixed at magnitude `0.03` with alternating sign by bin. This creates a smooth, strongly identified reference ECE object while preserving heterogeneous binwise calibration structure.

Candidate predictions use only a uniform shift `lambda`, but because the true reference residual signs alternate by bin, shifting predictions reassigns some sessions across bins and the paired ECE difference is no longer algebraically outcome-free.

For each target scenario (`0`, `0.5 epsilon`, `epsilon`, `2 epsilon`), a deterministic label-free grid search over `lambda in [0,0.03]` selects the value whose **population** ECE difference, computed from known synthetic outcome probabilities, is nearest the target. The target error must be <= `5e-5`; otherwise the fixture is invalid and execution stops.

Only after these population fixture identities are constituted are outcomes sampled across the prospectively fixed 100 seeds.

## Additional discriminating gate

For every nonzero scenario, the median 95% interval width must exceed `0.0001`. This explicitly rejects another algebraically degenerate fixture.

Coverage, boundary-NI behavior, regularity, and the separate perfectly calibrated nonregular negative control remain prospectively gated as specified in `config.yaml`.

## Historical order

The historical OOF hashes may be verified/read only if all repaired synthetic method-validity gates pass.

Historical outcomes and authority ceilings are unchanged from V1.

## Authority ceiling

V2 can validate or reject the same IF efficiency candidate for this declared scope. It cannot change ECE-10, the margin, calibration treatment, evidence source, or authorize CCA-derived features.
