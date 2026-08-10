# Research State Machine

This document defines how scientific work is allowed to move through the Correction-Capable Adaptation program.

The purpose is procedural: **an unresolved scientific question must not become an implementation decision by accident.**

The program is cumulative. A downstream claim can acquire authority only when the upstream scientific objects, measurement structures, and every separable causal transformation required by that claim have already been warranted.

## Program maturity ladder

```text
Level 0  MEASUREMENT / SCIENTIFIC-OBJECT VALIDITY
         Can the intended scientific object be identified?
              ↓
Level 1  EVIDENCE-CONTROLLED ADAPTIVE DECISION
         Does warranted evidence acquire causal control?
              ↓
Level 2  ISOLATED MODIFICATION
         Does direct do(M=m) produce the intended target effect
         while preserving protected behavior within tolerance?
              ↓
Level 3  EVIDENCE → JUSTIFIED MODIFICATION
         Can the validated relations be composed across every
         separable transformation they cross?
              ↓
Level 4A POST-MODIFICATION CORRECTABILITY
         Do future warranted-correction conditions remain available?
              ↓
Level 4B REPEATED CORRECTION
         Are those conditions actually exercised again?
              ↓
Level 5  JUSTIFIED TRANSFORMABILITY
         What warranted transformation repertoire remains reachable,
         including materially different destinations that preserve
         or reconstitute future correction conditions?
              ↓
Level 6  ADAPTIVE VIABILITY / CAPABILITY
         Does correction-capable adaptation improve future viability?
              ↓
Level 7  EXTREME ADAPTIVE SYSTEMS
         AGI / recursive improvement / ASI as stress-test regimes
```

These levels are not averaged. Empirical maturity is limited by the first unresolved causal prerequisite of the claim being made.

The ladder is an **evidence-ordering discipline**. Unless separately established, it must not be interpreted as a universal logical or metaphysical decomposition of every adaptive system.

## CCA Causal Composition Principle

CCA adopts:

> **A downstream causal claim may not inherit authority from an upstream validated relation across a separable transformation unless that transformation is independently identified, prospectively specified and validated as an apparatus guarantee, or explicitly excluded from the claim.**

\[
\boxed{\text{validated endpoints}\not\Rightarrow\text{validated pathway}.}
\]

If a claimed path crosses a separable transformation, that transformation must be independently causally identified or prospectively specified and validated/mechanically verified as an apparatus relation. Otherwise the claim stops before the edge.

Decision record: [`../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md).

## Experiment lifecycle

Every empirical object must move through:

```text
PROPOSED
   ↓
ADVERSARIAL_REVIEW
   ↓
MEASUREMENT_VALID
   ↓
CONTRACT_FROZEN
   ↓
AUTHORIZED
   ↓
EXECUTED
   ↓
ANALYZED
   ↓
CLOSED
```

The lifecycle is a scientific authority sequence, not a software workflow.

### PROPOSED

Allowed: conceptual decomposition, counterexamples, competing formulations, non-model feasibility analysis.

Not allowed: treating implementation details as evidence, choosing an ontology for coding convenience, or presenting execution as scientific evidence.

### ADVERSARIAL_REVIEW

Required questions include:

- Is the object identifiable?
- Does measurement partly redefine the object?
- Can a shallower explanation absorb it?
- Are there constructive impossibility cases?
- What would disconfirm it?
- Does the claim cross separable transformations lacking authority?
- Is a program evidence-order being mistaken for a logical definition?

A failed adversarial review returns to `PROPOSED` or closes the proposed construction.

### MEASUREMENT_VALID

The measurement contract is sufficiently specified that the intended object can, in principle, be distinguished from relevant alternatives under the declared admissible transformations and nuisance channels.

This does not imply that the mechanism exists or that adjacent transformations are valid.

### CONTRACT_FROZEN

Before observing outcomes, the contract freezes at minimum:

- scientific proposition;
- causal path actually claimed;
- separable variables and transformations;
- identification/apparatus status of each required transformation;
- intervention space;
- independent truth/warrant mapping where required;
- target and protected outcomes;
- admissible transformation class;
- nulls and disconfirmation criteria;
- estimands and estimators;
- uncertainty/multiplicity procedure;
- sample/randomization structure;
- authorization rule;
- implementation-validity criteria.

For repertoire-level claims, the contract must also freeze whatever prospective target/transformation scope and distinctness/warrant rules constitute the claimed repertoire.

### AUTHORIZED / EXECUTED / ANALYZED / CLOSED

`AUTHORIZED` permits execution of the frozen object; it does not assert truth. `EXECUTED` records outcome-bearing execution or explicit implementation failure. `ANALYZED` applies frozen estimands/rules. `CLOSED` fixes the result under its stopping condition.

Implementation failure must not be recoded as a scientific zero. Closed negative results must not be repaired post hoc.

## Authority transfer

Evidence may increase authority only along dimensions it can identify:

```text
ΔE_t → ΔW_{t+1}
```

Authority transfer is local. Endpoint success does not identify an intervening pathway; realized trajectory evidence does not identify a broader counterfactual repertoire unless the repertoire scope was independently constituted and measured.

## Post-Modification Correctability discipline

PMC asks:

> **After a consequential change, do the conditions required for future warranted correction remain available?**

It retains:

\[
\text{future admissible evidence}
\leadsto
\text{warranted causal authority}
\leadsto
\text{consequential correction}.
\]

PMC must not be inferred from current performance/capability, generic plasticity, the success of the preceding correction, or external rescue outside the declared system boundary.

PMC remains role-only; its scope and measurement contract are unfrozen.

Decision record: [`../lineage/decisions/POST_MODIFICATION_CORRECTABILITY_ROLE.md`](../lineage/decisions/POST_MODIFICATION_CORRECTABILITY_ROLE.md).

## Capacity-survived versus capacity-exercised discipline

CCA canonically distinguishes:

\[
\boxed{\mathrm{PMC}\neq\mathrm{Repeated\ Correction}}
\]

because PMC is latent/dispositional availability while repeated correction is a realized valid correction episode.

A realized repeated correction for opportunity \(e\) provides local authority only:

\[
\mathrm{ValidRepeatedCorrection}(e)
\Rightarrow
\mathrm{LocalCorrectionAvailability}(e),
\]

not broad PMC over untested opportunities.

\[
\boxed{N_{\mathrm{corrections}}\neq C_{\mathrm{corr}}.}
\]

Decision record: [`../lineage/decisions/PMC_REPEATED_CORRECTION_DISTINCTION.md`](../lineage/decisions/PMC_REPEATED_CORRECTION_DISTINCTION.md).

## Trajectory-versus-repertoire discipline

CCA provisionally adopts **Justified Transformability (JT)** as a repertoire-level conceptual role:

> **What prospectively relevant warranted transformations remain reachable, and can materially different warranted destinations be reached while preserving or reconstituting future correction conditions?**

CCA distinguishes:

```text
PMC                  availability
Repeated Correction  realized temporal exercise
JT                   warranted transformation repertoire
```

Therefore:

\[
\boxed{\mathrm{RepeatedCorrection}\not\Rightarrow\mathrm{JT}.}
\]

Repeated valid episodes can be scripted, confined to a narrow dimension or fixed menu, or cumulatively destroy broader future transformation options.

Nor is observed repeated temporal history definitionally necessary for a repertoire claim:

\[
\boxed{\mathrm{JT}\not\Rightarrow\mathrm{ObservedRepeatedCorrectionHistory}.}
\]

A branching counterfactual design could in principle probe different warranted transformations across replicated instances.

Hence:

\[
\boxed{\text{trajectory evidence}\neq\text{repertoire evidence}}
\]

and:

\[
\boxed{\text{logical object dependency}\neq\text{program evidence-ordering dependency}.}
\]

Repeated correction remains upstream in CCA's research order as a conservative prerequisite for granting JT authority, but that is an epistemic policy, not the universal definition of JT.

Decision record: [`../lineage/decisions/JUSTIFIED_TRANSFORMABILITY_ROLE.md`](../lineage/decisions/JUSTIFIED_TRANSFORMABILITY_ROLE.md).

### JT anti-inflation guardrails

Until prospectively frozen, an agent must not treat any of the following as sufficient evidence of JT:

- raw correction episode count;
- scripted or memorized correction sequences;
- many reachable states;
- nominal benchmark diversity;
- transformations judged warranted only after seeing outcomes;
- trivial parameter/state differences declared materially distinct post hoc;
- external apparatus supplying transformations when the claim concerns system-internal repertoire.

\[
\boxed{\text{many reachable states}\not\Rightarrow\text{many warranted transformations}.}
\]

Warrant semantics, material distinctness, target-family scope, preservation/reconstitution, counterfactual availability, representation, metric, estimator, and threshold remain unfrozen.

## Frozen-object rule

A `CLOSED` object is immutable as a scientific result. Permitted work after closure includes clearer documentation, provenance repair, bounded outcome-blind diagnosis, and new descendant objects. Changing estimands, models, gates, or post-selecting outcomes to rescue the ancestor is forbidden.

## Agent / Codex guardrail

Automated implementation agents must read `research_state.json` before empirical execution work.

Implementation is authorized only when the relevant object records:

```text
measurement_state = MEASUREMENT_VALID or later
contract_state    = CONTRACT_FROZEN or later
execution_state   = AUTHORIZED
implementation_authorized = true
```

An agent must not infer authorization from directory existence, an open issue, a plausible benchmark, available compute, model availability, endpoint success, conceptual-role adoption, or a theoretical metric.

Specifically forbidden are:

- inferring broad PMC from one repeated correction;
- treating raw correction count as correction capacity;
- treating repeated correction history as the definition of JT;
- treating state count as warranted repertoire;
- defining warrantedness or distinctness retrospectively;
- implementing JT while its target-family and counterfactual semantics remain unfrozen.

## Current application

`G1` is role-fixed but empirically untested and contract-unfrozen.

`G2` remains architecture-only and must be identified through direct:

\[
\boxed{do(M=m)\rightarrow(Y_T,Y_P)}.
\]

The CCA Causal Composition Principle is canonical. PMC is role-fixed only. The PMC/repeated-correction distinction is canonical conceptually. Repeated correction remains empirically untested. JT is now role-fixed only; its warrant/distinctness semantics and measurement machinery remain unfrozen.

The next conceptual frontier is:

> **Can the warrant, distinctness, repertoire, preservation, target-family, and counterfactual-availability semantics of Justified Transformability be specified without retrospective approval, trivial-difference inflation, or benchmark-defined reachability?**

No repeated-correction or JT experiment is authorized by this transition.
