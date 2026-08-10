# ASI-0 — Contract

## Status

**Historical frozen contract. The experiment is closed.**

ASI-0 is preserved because it is the immediate empirical ancestor of the current mechanism architecture. Despite the name, it did **not** test ASI, recursive self-improvement, general intelligence, or viability.

## Scientific question

> Can a fixed-base-model agent use correctly assigned development evidence to select a bounded modification that improves concealed future capability relative to fixed base and evidence-misaligned assignment under matched resources?

## Frozen two-axis object

Capability:

\[
C=E[Y_{\mathrm{aligned}}-Y_{\mathrm{base}}].
\]

Evidence attribution:

\[
A=E[Y_{\mathrm{aligned}}-Y_{\mathrm{misaligned}}].
\]

A positive result required both:

\[
L_C>0
\quad\land\quad
L_A>0.
\]

The hypotheses were conjunctive:

\[
H_0:(C\le0)\lor(A\le0),
\qquad
H_1:(C>0)\land(A>0).
\]

## Treatment object

The causal treatment was the evidence-to-target assignment mechanism:

```text
ALIGNED
relevant development evidence -> its own target

MISALIGNED
matched evidence -> a different target within stratum
```

The intent was to hold evidence quantity and generic information structure fixed while breaking target relevance.

## Modification boundary

The canonical instance used one bounded textual policy patch with frozen model weights and a deterministic protected-regression acceptance rule.

A candidate patch entered the effective arm only if it preserved protected behavior according to the frozen gate. Otherwise the policy-level intervention became a no-op.

## Inference

The primary uncertainty procedure used a one-sided target-cluster bootstrap with prospectively fixed settings. Replication was authorized only if the primary conjunctive gate passed.

## Nonclaims

Even a positive result would not have established:

```text
intelligence
viability
recursive self-improvement
architecture superiority
ASI
```

The maximum positive claim was intentionally local: correctly assigned evidence causally contributed to selecting a bounded modification that improved concealed future capability under the frozen conditions.
