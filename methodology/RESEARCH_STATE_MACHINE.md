# Research State Machine

This document defines how scientific work is allowed to move through the Correction-Capable Adaptation program.

The purpose is procedural: **an unresolved scientific question must not become an implementation decision by accident.**

The program is cumulative. A downstream gate can be entered only when the upstream scientific object, measurement structure, and authorization conditions required by that gate have already been established.

## Program maturity ladder

The scientific dependency ladder is:

```text
Level 0  MEASUREMENT VALIDITY
         Can the intended scientific object be identified?
              ↓
Level 1  EVIDENCE-CONTROLLED SELECTION
         Does evidence control warranted candidate choice?
              ↓
Level 2  ISOLATED MODIFICATION
         Does direct do(M=m) produce the intended target effect
         while preserving protected behavior within tolerance?
              ↓
Level 3  EVIDENCE → JUSTIFIED MODIFICATION
         Do selection and modification mechanisms work together?
              ↓
Level 4  REPEATED CORRECTION
         Can justified correction recur without destroying prior valid structure?
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

These levels are **not averaged**. Program maturity is defined by the first unresolved causal prerequisite.

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

A failed adversarial review returns to `PROPOSED` or closes the proposed construction.

### MEASUREMENT_VALID

The measurement contract is sufficiently specified that the intended object can, in principle, be distinguished from relevant alternatives under the declared admissible transformations and nuisance channels.

This state does **not** imply that the mechanism exists.

### CONTRACT_FROZEN

Before observing scientific outcomes, the contract freezes at minimum:

- scientific proposition;
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
- a model being easy to run.

## Current application

The current frontier is Level 0.

```text
G1 scientific object
G1^broad vs G1^relational
→ ADVERSARIAL_REVIEW
```

Measurement analysis has already established:

```text
universal relational codebook       REFUTED
ontology-conditional construction   FEASIBLE IN PRINCIPLE
```

But the program has not selected which G1 object it intends to test. Therefore ontology selection, evidence-space freezing, model selection, prompt engineering, and ECIM execution remain unauthorized.
