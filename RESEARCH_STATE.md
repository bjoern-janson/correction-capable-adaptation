# Research State

This file is the human-readable program state. The machine-readable authority state is [`research_state.json`](research_state.json), and transition rules are defined in [`methodology/RESEARCH_STATE_MACHINE.md`](methodology/RESEARCH_STATE_MACHINE.md).

## Central question

> **Can an adaptive system increase its future viability while remaining capable of incorporating justified correction?**

The program advances only through independently validated causal prerequisites and warranted causal composition across the transformations a claim actually crosses.

## Research returnability

CCA now explicitly gives the research program itself a reopening path.

No conceptual, methodological, or scientific authority state is permanently immune to new discriminating evidence.

\[
\boxed{\text{current authority}\neq\text{permanent immunity from revision}}
\]

Reopening follows CARS localization: open the smallest boundary implicated by the evidence, preserve unaffected structure and provenance, revise through an explicit amendment or successor, and stop when no discriminating residual remains.

\[
\boxed{\text{redescription}\neq\text{re-localization}}
\]

A closed empirical result remains immutable as the historical result under its original object identity and contract. The surrounding research remains reopenable through descendants, amended scope/interpretation, or revised conceptual and methodological rules.

\[
\boxed{\text{historical immutability}\neq\text{epistemic irreversibility}}
\]

Rule: [`methodology/RESEARCH_RETURNABILITY.md`](methodology/RESEARCH_RETURNABILITY.md).

## Research maturity ladder

| Level | Scientific gate | Current state |
| ---: | --- | --- |
| 0 | Measurement validity / scientific-object constitution | **G1 ROLE PROVISIONALLY FIXED / EXPERIMENT CONTRACT UNFROZEN** |
| 1 | Evidence-controlled adaptive decision | **SCIENTIFIC OBJECT DEFINED / EMPIRICALLY UNTESTED** |
| 2 | Isolated modification | **ARCHITECTURE ONLY** |
| 3 | Evidence → justified modification | **NOT AUTHORIZED / CAUSAL COMPOSITION REQUIRED** |
| 4A | Post-Modification Correctability | **ROLE PROVISIONALLY FIXED / METRIC & CONTRACT UNFROZEN** |
| 4B | Repeated correction | **CONCEPTUALLY DISTINCT / EMPIRICALLY UNTESTED** |
| 5 | Justified Transformability | **ROLE PROVISIONALLY FIXED / WARRANT & DISTINCTNESS SEMANTICS UNDER REVIEW** |
| 6 | Adaptive viability / capability | **NOT AUTHORIZED** |
| 7 | Extreme adaptive systems | **NOT AUTHORIZED** |

These levels are not averaged into a progress percentage.

Every current role, distinction, and methodological rule in this table is reopenable under the Research Returnability Rule when new discriminating evidence reaches it. Until then, its current authority remains operative.

\[
\boxed{\text{empirical authority advances only when each prerequisite and required separable transformation is independently warranted}}
\]

## CCA Causal Composition Principle

CCA currently adopts:

> **A downstream causal claim may not inherit authority from an upstream validated relation across a separable transformation unless that transformation is independently identified, prospectively specified and validated as an apparatus guarantee, or explicitly excluded from the claim.**

Therefore:

\[
\boxed{\text{validated endpoints}\not\Rightarrow\text{validated pathway}.}
\]

and:

\[
\boxed{\text{No causal authority may be propagated across an unvalidated separable transformation.}}
\]

This is a composition law, not a new CCA gate or universal intermediate mechanism. The exact causal decomposition remains architecture-dependent.

Decision record: [`lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md).

## Scoped role of G1

CCA provisionally adopts:

\[
\boxed{
G_1
=
\text{warranted evidence acquiring causal control over a separable adaptive decision}
}
\]

The current operational instantiation is candidate selection:

\[
E\longrightarrow C_{\mathrm{selected}}.
\]

This is not a universal architectural claim. No G1 experiment has been frozen or executed.

```text
G1 SCIENTIFIC ROLE       PROVISIONALLY FIXED / REOPENABLE
G1 EMPIRICAL RESULT      UNOBSERVED
G1 CONTRACT              UNFROZEN
G1 IMPLEMENTATION        NOT AUTHORIZED
```

Decision record: [`lineage/decisions/G1_LEVEL0_ROLE.md`](lineage/decisions/G1_LEVEL0_ROLE.md).

## Level 2 — modification remains independently identified

The hard design principle remains:

\[
\boxed{G_2:\ do(M=m)\rightarrow(Y_T,Y_P)}.
\]

Modification efficacy and protected interference must be identified through direct assignment of the modification, never by conditioning on whichever modification a selector happened to choose.

Selection competence is not modification competence, and modification competence does not identify how the modification acquired its value.

## Level 3 — end-to-end composition remains unauthorized

For a claimed path \(\pi\):

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

`PathValid(π)` requires every additional separable transformation crossed by the claim to be independently identified or prospectively specified and validated/verified as an apparatus relation. If a transformation is explicitly excluded, the claim must stop before crossing it.

No universal bridge gate is frozen.

## Post-Modification Correctability — provisional role

CCA provisionally adopts **Post-Modification Correctability (PMC)** as the conceptual object immediately upstream of repeated correction.

Its role is:

> **After a consequential change, do the conditions required for future warranted correction remain available?**

The causal content remains:

\[
\boxed{
\text{future admissible evidence}
\leadsto
\text{warranted causal authority}
\leadsto
\text{consequential correction}
}
\]

within a prospectively declared correction scope.

PMC is not current performance, current capability, generic plasticity, or one-shot correction success. It is not provisionally treated as an intrinsic scalar of \(S_{t+1}\) alone.

Its environment, system boundary, horizon, topology, dimensions, preservation/degradation criterion, scalarization, estimand, estimator, threshold, and protocol all remain unfrozen.

Decision record: [`lineage/decisions/POST_MODIFICATION_CORRECTABILITY_ROLE.md`](lineage/decisions/POST_MODIFICATION_CORRECTABILITY_ROLE.md).

## Current PMC ↔ repeated-correction distinction

CCA currently preserves:

\[
\boxed{\mathrm{PMC}\neq\mathrm{Repeated\ Correction}}
\]

or:

\[
\boxed{\text{capacity survived}\neq\text{capacity exercised}.}
\]

PMC is latent/dispositional availability. Repeated correction is a realized subsequent valid correction episode.

A realized valid repeated correction provides only local authority:

\[
\boxed{
\mathrm{ValidRepeatedCorrection}(e)
\Rightarrow
\mathrm{LocalCorrectionAvailability}(e)
}
\]

for the realized opportunity \(e\), but:

\[
\boxed{
\mathrm{LocalCorrectionAvailability}(e)
\not\Rightarrow
\mathrm{PMC}(\Omega_{\mathrm{broader}}).
}
\]

Thus:

\[
\boxed{N_{\mathrm{corrections}}\neq C_{\mathrm{corr}}.}
\]

Decision record: [`lineage/decisions/PMC_REPEATED_CORRECTION_DISTINCTION.md`](lineage/decisions/PMC_REPEATED_CORRECTION_DISTINCTION.md).

## Justified Transformability — provisional conceptual role

After PR #13, CCA provisionally adopts **Justified Transformability (JT)** as a distinct repertoire-level conceptual object.

Its current role is:

> **What prospectively relevant warranted transformations remain reachable from a system state, and can materially different warranted destinations be reached while preserving or reconstituting the causal conditions required for future warranted correction?**

CCA therefore preserves:

\[
\boxed{\mathrm{PMC}=\text{availability}}
\]

\[
\boxed{\mathrm{RepeatedCorrection}=\text{realized temporal exercise}}
\]

\[
\boxed{\mathrm{JT}=\text{warranted transformation repertoire}}
\]

and the non-equivalences:

\[
\boxed{
\mathrm{PMC}\not\Rightarrow\mathrm{RepeatedCorrection},
\qquad
\mathrm{RepeatedCorrection}\not\Rightarrow\mathrm{JT}.
}
\]

A prospectively established repertoire claim also need not imply that one physical instance has already traversed a repeated correction history:

\[
\boxed{\mathrm{JT}\not\Rightarrow\mathrm{ObservedRepeatedCorrectionHistory}.}
\]

Compactly:

\[
\boxed{\text{trajectory evidence}\neq\text{repertoire evidence}.}
\]

Repeated correction may remain an upstream **research evidence-ordering prerequisite** because it tests survival across actual consequential temporal change. That is not a universal definition of JT:

\[
\boxed{\text{logical object dependency}\neq\text{program evidence-ordering dependency}.}
\]

Decision record: [`lineage/decisions/JUSTIFIED_TRANSFORMABILITY_ROLE.md`](lineage/decisions/JUSTIFIED_TRANSFORMABILITY_ROLE.md).

### What JT does not yet mean

The following remain explicitly unfrozen:

```text
warrant semantics
material / appropriate distinctness semantics
target or transformation family
reachable-state / reachable-transformation formalism
novelty or distance thresholds
repertoire breadth / diversity / coverage
preservation versus reconstitution semantics
system / apparatus boundary
counterfactual availability criterion
estimand / estimator
metric / threshold
empirical protocol
```

JT must not be inferred from raw correction count, scripted repetition, a large reachable-state count, or retrospective approval of whichever transformation happened to occur.

\[
\boxed{\text{many reachable states}\not\Rightarrow\text{many warranted transformations}.}
\]

JT also does not canonize `C_improve` and does not establish that the transformation repertoire improved.

## Causal non-substitutions

\[
\boxed{G_1\neq\mathrm{CCA}}
\]

and:

\[
\boxed{
G_1
\not\Rightarrow
G_2
\not\Rightarrow
\mathrm{PMC}
\not\Rightarrow
\text{repeated correction}
\not\Rightarrow
\mathrm{JT}
\not\Rightarrow
\text{adaptive viability}
}
\]

A positive result at one layer grants authority only to the scientific object it actually identifies.

## Adversarial provenance

```text
#3–#8   G1 scientific-object attacks
#9–#10  causal-composition attacks
#11     PMC scientific-object attack
#12     PMC versus repeated-correction attack
#13     repeated correction versus Justified Transformability attack
```

These remain provenance rather than empirical experiments.

## Current authorization

```text
PROGRAM GOVERNANCE                      RETURNABLE UNDER NEW DISCRIMINATING EVIDENCE
ASI-0 historical result                 CLOSED / IMMUTABLE AS HISTORICAL RESULT / DESCENDANTS REOPENABLE
G1 scientific role                      PROVISIONALLY FIXED / REOPENABLE
CCA causal composition principle        CURRENT CANONICAL METHODOLOGICAL RULE / REOPENABLE
PMC conceptual role                     PROVISIONALLY FIXED / REOPENABLE
PMC ↔ repeated correction distinction   CURRENT CANONICAL CONCEPTUAL DISTINCTION / REOPENABLE
JT conceptual role                      PROVISIONALLY FIXED / REOPENABLE
JT warrant / distinctness semantics     UNFROZEN / UNDER ADVERSARIAL REVIEW
PMC metric / contract                   UNFROZEN
repeated-correction contract            UNFROZEN
repeated-correction empirical result    UNOBSERVED
JT metric / contract                    UNFROZEN
G1 experiment contract                  UNFROZEN
ECIM scientific contract                UNFROZEN
ECIM implementation                     NOT AUTHORIZED
repeated-correction experiment          NOT AUTHORIZED
JT experiment                           NOT AUTHORIZED
new empirical execution                 NOT AUTHORIZED
```

Research returnability changes the permanence semantics of scientific authority states. It does **not** authorize any empirical execution.

## Next conceptual frontier

The next attack remains:

> **Can the warrant, distinctness, repertoire, preservation, target-family, and counterfactual-availability semantics of Justified Transformability be specified without retrospective approval, trivial-difference inflation, or benchmark-defined reachability?**

This remains conceptual. No JT, repeated-correction, PMC, G1, or ECIM empirical implementation is authorized by this transition.
