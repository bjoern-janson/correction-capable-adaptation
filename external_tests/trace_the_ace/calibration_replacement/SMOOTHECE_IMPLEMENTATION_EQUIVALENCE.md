# SmoothECE implementation-equivalence record

## Status

**PASS — apparatus equivalence only**

This record contains no model-performance result and no calibration-method authority. It verifies that the local execution path used for the candidate reproduces the pinned SmoothECE point measurement and automatic bandwidth selection before any `F0..F6` scientific fixture is adjudicated.

## Pinned source identity

The candidate contract pinned the Apple reference implementation at:

```text
repo    apple/ml-calibration
commit  18ff21a7e4e409fc4885690129f50211b32ea144

metrics.py blob  662821b962ea67c21515b1a133a7692ae6ac793d
kernels.py blob  a55bec6793ef18ea735e58466e6d5143f5e5b660
config.py blob   65059c7f156df78ef44b8bd43dfd85fda216ef8d
```

The GitHub source reads confirmed these exact blob identities before execution.

Frozen candidate defaults verified:

```text
kernel                    reflected Gaussian
use_logit_scaling         false
smECE_mesh_pts            200
automatic bandwidth eps   0.001
search start              1.0
search refinements        10
manual bandwidth          forbidden
```

## Deterministic equivalence suite

The contract requires:

```text
seed             1809
n_test_vectors   12
lengths          8, 31, 257, 4096
boundary values  included
comparison       point SmoothECE + selected bandwidth
max error gate   <= 1e-10
```

The executed deterministic suite used three prospectively fixed vector constructions per declared length, with boundary predictions included where specified, and compared the independent local execution path against the pinned reference path.

Result:

```text
cases tested             12
max abs point/bw error   0.0
required maximum         1e-10
implementation gate      PASS
```

Local reproducibility artifact SHA-256:

```text
791f9d9f75f06fb786a27a32cd5a76bebdd9f13beb6acc31ee1105627695979f
```

## Authority ceiling

This pass establishes only apparatus equivalence for the candidate execution path. It does not imply `G_F`, `G_detect`, `G_U`, `G_decision`, replacement-measurement authority, historical calibration closure, mature-baseline authority, or any CCA-feature authority.
