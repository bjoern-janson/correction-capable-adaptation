# Research State

This file is the human-readable program state. The machine-readable authority state is [`research_state.json`](research_state.json), and transition rules are defined in [`methodology/RESEARCH_STATE_MACHINE.md`](methodology/RESEARCH_STATE_MACHINE.md).

## Central question

> **Can an adaptive system increase its future viability while remaining capable of incorporating justified correction?**

The program advances only through independently validated causal prerequisites and warranted causal composition across the transformations a claim actually crosses.

## Research maturity ladder

| Level | Scientific gate | Current state |
| ---: | --- | --- |
| 0 | Measurement validity / scientific-object constitution | **G1 ROLE PROVISIONALLY FIXED / EXPERIMENT CONTRACT UNFROZEN** |
| 1 | Evidence-controlled adaptive decision | **SCIENTIFIC OBJECT DEFINED / EMPIRICALLY UNTESTED** |
| 2 | Isolated modification | **ARCHITECTURE ONLY** |
| 3 | Evidence → justified modification | **NOT AUTHORIZED / CAUSAL COMPOSITION REQUIRED** |
| 4 | Repeated correction | **CONCEPTUAL FRONTIER / EMPIRICALLY NOT AUTHORIZED** |
| 5 | Justified transformability | **THEORETICAL ONLY** |
| 6 | Adaptive viability / capability | **NOT AUTHORIZED** |
| 7 | Extreme adaptive systems | **NOT AUTHORIZED** |

These levels are not averaged into a progress percentage.

\[
\boxed{\text{empirical authority advances only when each prerequisite and required separable transformation is independently warranted}}
\]

## Canonical methodological transition — CCA Causal Composition Principle

After PRs #9 and #10, CCA canonically adopts:

> **A downstream causal claim may not inherit authority from an upstream validated relation across a separable transformation unless that transformation is independently identified, prospectively specified and validated as an apparatus guarantee, or explicitly excluded from the claim.**

Therefore:

\[
\boxed{\text{validated endpoints}\not\Rightarrow\text{validated pathway}.}
\]

and:

\[
\boxed{\text{No causal authority may be propagated across an unvalidated separable transformation.}}
\]

This is a composition law governing causal claims. It is **not** a new CCA gate, maturity level, or universal adoption/translation mechanism.

The canonical decision record is [`lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md).

### Architecture-conditional scope

The rule applies to the decomposition actually claimed.

A separable architecture may require identification of:

\[
C_{\mathrm{selected}}\rightarrow D\rightarrow M,
\]

while a direct-update architecture may instead contain:

\[
E\rightarrow M.
\]

If selection and modification are inseparable, adding an artificial bridge would manufacture a causal distinction rather than identify one.

Thus CCA requires **validated evidence-to-change causality**, not one universal intermediate graph.

### Apparatus guarantees

If an experiment uses a fixed relation such as:

\[
M=\phi(C),
\]

as apparatus plumbing, \(\phi\) must be prospectively specified and independently validated or mechanically verified over the claimed domain.

An apparatus-mediated link can support an apparatus-mediated pathway claim. It does not establish system-internal adoption or translation competence.

## Level-0 decision — scoped role of G1

CCA continues to provisionally adopt:

\[
\boxed{
G_1
=
\text{warranted evidence acquiring causal control over a separable adaptive decision}
}
\]

The current operational decomposition instantiates the adaptive decision as candidate selection:

\[
E\longrightarrow C_{\mathrm{selected}}.
\]

This is a scoped commitment about CCA's first studied empirical pathway. It is **not** a claim that every correction-capable architecture must contain an explicit candidate-selection node.

The canonical decision record is [`lineage/decisions/G1_LEVEL0_ROLE.md`](lineage/decisions/G1_LEVEL0_ROLE.md).

### What G1 is not

The adversarial analysis established that none of the following is a substitute for G1:

```text
codebook construction
relational sensitivity
representation invariance
access robustness
candidate accuracy
mechanism/channel attribution
```

The measurement attacks also separated semantic constitution, interface scope, realization policy, total warranted evidence control, realization/access heterogeneity, and mechanism attribution. Those distinctions constrain future contracts; they do not convert all of those properties into the definition of G1.

## Current empirical authority

No G1 experiment has been frozen or executed.

The following remain unfrozen:

- candidate ontology;
- semantic evidence states;
- interface contract;
- realization policy;
- scalar G1 estimand and weighting rule;
- uncertainty procedure and threshold;
- model and prompt;
- benchmark;
- ECIM contract;
- any architecture-specific selection→modification bridge estimand or intervention.

Therefore:

```text
G1 SCIENTIFIC ROLE       PROVISIONALLY FIXED
G1 EMPIRICAL RESULT      UNOBSERVED
G1 CONTRACT              UNFROZEN
G1 IMPLEMENTATION        NOT AUTHORIZED
```

## Causal non-substitutions

\[
\boxed{G_1\neq\mathrm{CCA}}
\]

and

\[
\boxed{
G_1
\not\Rightarrow
G_2
\not\Rightarrow
\text{repeated correction}
\not\Rightarrow
\text{justified transformability}
\not\Rightarrow
\text{adaptive viability}
}
\]

A positive G1 would establish only the warranted causal-control property under its frozen conditions.

Likewise:

\[
\boxed{
G_1>0\land G_2>0
\not\Rightarrow
\text{connected evidence-to-modification causality}
}
\]

when the claimed path crosses an additional separable transformation that has not itself acquired authority.

## Level 2 — modification remains independently identified

The hard design principle remains:

\[
\boxed{G_2:\ do(M=m)\rightarrow(Y_T,Y_P)}.
\]

Modification efficacy and protected interference must be identified through direct assignment of the modification, never by conditioning on whichever modification a selector happened to choose.

Selection competence is not modification competence, and modification competence does not identify how the modification acquired its value.

## Level 3 — end-to-end composition remains unauthorized

For a claimed path \(\pi\), Level 3 requires more than positive endpoint gates:

\[
\boxed{
\mathrm{ADVANCE}_{\pi}
\iff
G_1
\land
\mathrm{PathValid}(\pi)
\land
G_{2T}
\land
G_{2P}
}
\]

`PathValid(π)` requires every additional separable transformation crossed by the claim to be independently identified or prospectively specified and validated/verified as an apparatus relation.

If a transformation is explicitly excluded, the claim must stop before crossing it.

No bridge gate, bridge estimand, or bridge intervention is currently frozen.

## Measurement and bridge provenance

The scoped G1 decision is informed by six independent attack PRs:

```text
#3  broad vs relational
#4  outcome vs mechanism/channel attribution
#5  semantic vs behavioral invariance
#6  realization/access envelope
#7  causal identification
#8  scientific program role
```

The composition principle is informed by:

```text
#9  causal semantics of the G1-to-G2 bridge
#10 architecture-independent necessity of a bridge
```

These remain provenance rather than canonical empirical experiments.

## Ancestral evidence

ASI-0 remains an immutable closed ancestor:

```text
C            0
A            0
L_C          0
L_A          0
PRIMARY      STOP
REPLICATION  NOT AUTHORIZED
```

The post-outcome diagnosis localized weak evidence control over candidate identity and poor protected-behavior isolation of the tested textual modifications. That motivated the decision/modification decomposition; it did not authorize retrospective repair.

## Current authorization

```text
PROGRAM OBJECT                         PROVISIONALLY FIXED
ASI-0                                 CLOSED / IMMUTABLE
G1 scientific role                    PROVISIONALLY FIXED
G1 operational candidate-selection    CURRENT INSTANTIATION / NOT UNIVERSAL
CCA causal composition principle      CANONICAL METHODOLOGICAL RULE
G1 experiment contract                UNFROZEN
candidate ontology                    UNFROZEN
evidence intervention space           UNFROZEN
architecture-specific bridge object   UNFROZEN / UNNAMED
ECIM scientific contract              UNFROZEN
ECIM model / prompt                    NOT SELECTED
ECIM empirical implementation         NOT AUTHORIZED
new empirical execution               NOT AUTHORIZED
```

## Next conceptual frontier

The next program-level conceptual question is:

> **What must be true for a system to remain capable of incorporating warranted correction after a consequential modification?**

This is the transition from validating one correction pathway toward preservation of correction capacity across change.

It is **not** authorization to skip the unresolved empirical prerequisites. Any future repeated-correction experiment remains blocked until the particular evidence-to-change pathway it depends on has validly established its upstream gates and satisfied the CCA Causal Composition Principle across every separable transformation it claims.

No implementation is authorized by this transition.
