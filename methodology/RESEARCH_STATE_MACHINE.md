# Research State Machine

This document defines how scientific work is allowed to move through the Correction-Capable Adaptation program.

The purpose is procedural: **an unresolved scientific question must not become an implementation decision by accident.**

The program is cumulative. A downstream claim can acquire authority only when the upstream scientific objects, measurement structures, and every separable causal transformation required by that claim have already been warranted.

## Program maturity ladder

The scientific dependency ladder is:

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
         Can the validated upstream and downstream relations be
         composed across every separable transformation they cross?
              ↓
Level 4A POST-MODIFICATION CORRECTABILITY
         After consequential change, do the conditions required
         for future warranted correction remain available?
              ↓
Level 4B REPEATED CORRECTION
         Does another valid correction episode actually occur?
              ↓
Level 5  JUSTIFIED TRANSFORMABILITY
         Does repeated correction preserve or expand appropriately reachable states?
              ↓
Level 6  ADAPTIVE VIABILITY / CAPABILITY
         Does correction-capable adaptation improve prospectively defined future viability?
              ↓
Level 7  EXTREME ADAPTIVE SYSTEMS
         AGI / recursive improvement / ASI as stress-test regimes
```

These levels are **not averaged**. Empirical maturity is limited by the first unresolved causal prerequisite of the claim being made.

PMC is currently a **provisionally fixed conceptual role**, not an empirical gate with a frozen measurement contract. The Level-4A/4B split is therefore a dependency distinction, not evidence that either object has passed empirically.

## CCA Causal Composition Principle

CCA adopts the following canonical methodological rule:

> **A downstream causal claim may not inherit authority from an upstream validated relation across a separable transformation unless that transformation is independently identified, prospectively specified and validated as an apparatus guarantee, or explicitly excluded from the claim.**

Compactly:

\[
\boxed{\text{validated endpoints}\not\Rightarrow\text{validated pathway}.}
\]

and:

\[
\boxed{\text{No causal authority may be propagated across an unvalidated separable transformation.}}
\]

For a claimed path \(\pi\), every transformation the prospective contract represents as causally separable and that the claim crosses must be warranted. A separable transformation may be:

1. independently causally identified; or
2. fixed by a prospectively specified, independently validated or mechanically verified apparatus relation within the relevant scope.

If it is neither, the claim must stop before crossing it.

An apparatus guarantee is not created by declaration. If the experiment relies on a relation such as \(M=\phi(C)\), \(\phi\) must be prospectively specified and validated or verified over the claimed domain.

An apparatus-mediated link does not establish that the adaptive system itself possesses the corresponding adoption, translation, or deployment competence.

The canonical decision record is [`../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md).

## Experiment lifecycle

Every empirical object must move through the following lifecycle:

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

A scientific object or mechanism is stated clearly enough to criticize.

Allowed:

- conceptual decomposition;
- counterexamples;
- competing formulations;
- non-model feasibility analysis.

Not allowed:

- treating implementation details as evidence;
- choosing an ontology merely because it is convenient to code;
- execution presented as scientific evidence.

### ADVERSARIAL_REVIEW

The object is actively attacked before implementation.

Required questions include:

- Is the object identifiable?
- Does the measurement partly redefine the object?
- Can an ordinary or shallower explanation absorb the proposed mechanism?
- Are there constructive impossibility cases?
- What evidence would disconfirm the object or mechanism?
- Does the claimed causal path cross separable transformations that have not acquired independent authority?

A failed adversarial review returns to `PROPOSED` or closes the proposed construction.

### MEASUREMENT_VALID

The measurement contract is sufficiently specified that the intended object can, in principle, be distinguished from relevant alternatives under the declared admissible transformations and nuisance channels.

This state does **not** imply that the mechanism exists or that adjacent separable transformations are valid.

### CONTRACT_FROZEN

Before observing scientific outcomes, the contract freezes at minimum:

- scientific proposition;
- causal path actually claimed;
- separable variables and transformations used by that path;
- identification or validated-apparatus status of each required separable transformation;
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

### AUTHORIZED

Execution is allowed only after the frozen contract and its upstream dependencies have been validated.

`AUTHORIZED` means **permission to execute the frozen object**, not confidence that the hypothesis is true.

### EXECUTED

The frozen execution has produced an outcome-bearing scientific record, or an implementation failure has been recorded explicitly.

Implementation failure must not be recoded as a scientific zero.

### ANALYZED

The frozen estimands and decision rules have been applied. Post-outcome diagnostics must remain separated from the primary outcome and may not rewrite it.

### CLOSED

The scientific object has reached its prospectively defined stopping condition.

A closed negative result is evidence. It is not an invitation to alter the benchmark until it becomes positive.

## Invalid and failed executions

Two terminal-looking states are deliberately distinguished from scientific failure:

```text
UNOBSERVED / INVALID
```

The intended scientific object was not successfully instantiated or measured. No primary scientific result exists for the affected execution.

```text
NEGATIVE / NULL
```

The scientific object was validly instantiated and the frozen success criterion was not established.

These states must never be conflated.

## Failure transition rule

When a valid experiment fails:

```text
FAILED / NEGATIVE RESULT
        ↓
mechanism diagnosis
        ↓
new prospective scientific object
```

Forbidden:

```text
FAILED
  ↓
loosen gate
  ↓
change prompt / model / estimand
  ↓
rerun until positive
```

A descendant motivated by failure receives a new object identity and a new prospective contract.

## Authority transfer

Evidence may increase authority only along dimensions it can identify.

Conceptually:

```text
ΔE_t → ΔW_{t+1}
```

Logging a result is not sufficient. The evidence must change the future authority state of hypotheses, mechanisms, measurements, policies, or actions within its warranted scope.

### Causal composition

Authority transfer is local to the relation identified.

If a contract claims:

\[
A\rightarrow B\rightarrow C,
\]

then evidence for \(A\rightarrow B\) and separate evidence for an effect of \(C\) do not establish \(B\rightarrow C\).

Endpoint validity does not validate an intervening pathway.

## Post-Modification Correctability discipline

CCA provisionally adopts PMC as the conceptual object immediately upstream of repeated correction:

> **After a consequential change, do the conditions required for future warranted correction remain available?**

PMC must retain the causal content:

\[
\text{future admissible evidence}
\leadsto
\text{warranted causal authority}
\leadsto
\text{consequential correction}.
\]

PMC must not be inferred from:

- current performance or capability;
- generic plasticity or steerability;
- success of the immediately preceding correction;
- external rescue outside the declared system boundary.

PMC is not yet a scalar or metric. A future empirical contract must prospectively specify the relational correction scope, system/apparatus boundary, horizon, representation, and any measurement or preservation criterion before execution.

The canonical role decision is [`../lineage/decisions/POST_MODIFICATION_CORRECTABILITY_ROLE.md`](../lineage/decisions/POST_MODIFICATION_CORRECTABILITY_ROLE.md).

CCA currently treats:

\[
\boxed{\mathrm{PMC}\neq\mathrm{Repeated\ Correction}}
\]

as a provisional conceptual distinction under adversarial review. PMC concerns availability of another warranted correction path; repeated correction concerns an actually established subsequent correction episode.

## Frozen-object rule

A `CLOSED` object is immutable as a scientific result.

Permitted after closure:

- clearer documentation;
- provenance repair;
- outcome-blind mechanism diagnosis if prospectively bounded;
- new descendant objects.

Not permitted:

- changing the original estimand;
- replacing the model and calling it the same experiment;
- loosening acceptance gates;
- using an accepted-only subset to replace a policy-level ITT estimand;
- upgrading the claim because later theory became more ambitious.

## Agent / Codex guardrail

Automated implementation agents must read `research_state.json` before proposing or writing empirical execution code.

Implementation of a scientific experiment is authorized only when the relevant object records:

```text
measurement_state = MEASUREMENT_VALID or later
contract_state    = CONTRACT_FROZEN or later
execution_state   = AUTHORIZED
implementation_authorized = true
```

If any required field is absent, unresolved, or false, the allowed work is limited to conceptual analysis, documentation, measurement validation, contract construction, or non-scientific implementation scaffolding explicitly marked as such.

An agent must not infer authorization from:

- the existence of a directory;
- a proposed architecture;
- an open issue;
- a plausible benchmark;
- available compute;
- a model being easy to run;
- successful endpoint assays when an intervening separable transformation remains unvalidated;
- the existence of a PMC role without a frozen PMC measurement contract;
- successful one-shot correction as evidence of repeated correction or PMC.

## Current application

The scientific role of `G1` is provisionally fixed:

\[
\boxed{
G_1=
\text{warranted evidence acquiring causal control over a separable adaptive decision}
}
\]

Candidate selection is the current operational instantiation, not a universal architecture.

`G1` remains empirically untested and contract-unfrozen.

`G2` remains architecture-only and must be identified independently through direct:

\[
\boxed{do(M=m)\rightarrow(Y_T,Y_P)}.
\]

The CCA Causal Composition Principle is canonical.

PMC is now provisionally fixed **in role only**. Its future-correction environment, system boundary, horizon, representation, dimensions, metric, estimator, threshold, and protocol remain unfrozen.

The next **conceptual** frontier is:

> **Is Post-Modification Correctability scientifically distinct from repeated correction, or is PMC merely the latent precondition for an actually observed repeated-correction episode?**

This does not authorize a repeated-correction experiment. Any empirical claim about PMC or repeated correction remains blocked until its particular evidence-to-change pathway satisfies the required empirical gates, frozen contract, and every separable transformation it crosses under the CCA Causal Composition Principle.
