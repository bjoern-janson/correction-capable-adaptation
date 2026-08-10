# Experiment Record Template

Every empirical object should have one canonical record using this structure.

## Identity

```text
OBJECT_ID:
PARENT_OBJECT:
PROGRAM_LEVEL:
OWNER:
```

A descendant created after a negative result receives a new `OBJECT_ID`.

## Lifecycle

```text
LIFECYCLE_STATE: PROPOSED
MEASUREMENT_STATE: UNRESOLVED
CONTRACT_STATE: UNFROZEN
EXECUTION_STATE: NOT_AUTHORIZED
IMPLEMENTATION_AUTHORIZED: false
```

Allowed lifecycle values:

```text
PROPOSED
ADVERSARIAL_REVIEW
MEASUREMENT_VALID
CONTRACT_FROZEN
AUTHORIZED
EXECUTED
ANALYZED
CLOSED
```

## Scientific object

What proposition or mechanism is the experiment intended to identify?

## Upstream dependencies

List required program gates and their authoritative evidence records.

```text
DEPENDENCY:
STATUS:
SOURCE:
```

If a required dependency is unresolved, execution cannot be authorized.

## Measurement structure

Define:

- the observed variables;
- the admissible transformation class;
- the mapping from observations to the scientific object;
- known non-identifiability boundaries;
- nuisance channels and licensed invariances.

## Intervention

Define the admissible intervention class and what remains matched.

## Truth / warrant mapping

Where warranted selection is part of the object, define the independent mapping before model behavior is observed.

## Outcomes

### Target outcome

```text
Y_T:
DIRECTION / THRESHOLD:
```

### Protected outcomes

```text
Y_P:
PROTECTED SET:
EQUIVALENCE / NONINTERFERENCE TOLERANCE:
```

Non-significance alone cannot establish preservation.

## Estimands

State the quantities the estimator is intended to recover.

## Nulls and disconfirmation

What observations count against each proposed mechanism?

## Decision / authorization rule

Prefer conjunctive authorization when all mechanisms are required:

\[
\mathrm{ADVANCE}\iff G_1\land G_2\land\cdots\land G_k.
\]

No compensatory score may allow downstream success to erase upstream failure.

## Implementation validity

Define conditions that make the experiment `UNOBSERVED / INVALID` rather than scientifically negative.

## Pre-execution freeze

Before `AUTHORIZED`, freeze:

```text
scientific object
measurement structure
intervention space
truth / warrant mapping where required
target and protected outcomes
nulls and disconfirmation
estimands / estimators
uncertainty / multiplicity
sample / randomization structure
authorization rule
implementation validity checks
```

## Execution record

```text
MANIFEST HASH:
CODE REVISION:
DATA / MODEL REVISION:
START:
END:
DEVIATIONS:
```

## Primary result

Record exactly the frozen primary output. Do not substitute post-selected analyses.

## Post-outcome diagnosis

Keep diagnostic evidence separate from the primary result. Diagnosis may motivate a descendant object but cannot rewrite the ancestor.

## Closure

```text
FINAL_STATE:
CLAIM_EARNED:
CLAIMS_NOT_EARNED:
DESCENDANT_AUTHORIZATION:
```
