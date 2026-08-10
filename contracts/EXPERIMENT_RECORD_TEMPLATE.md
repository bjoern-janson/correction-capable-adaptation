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

## Claimed causal path

Write the object-level causal path the experiment intends to support.

```text
CLAIMED_PATH:
```

Do not use gate names such as `G1 -> G2` as substitutes for object-level variables.

## Separable transformations

List every transformation the claimed path prospectively treats as causally separable.

For each one record:

```text
TRANSFORMATION:
STATUS: INDEPENDENTLY_IDENTIFIED | VALIDATED_APPARATUS_GUARANTEE | NOT_CROSSED_BY_CLAIM
INTERVENTION / VERIFICATION:
SOURCE:
CLAIM_SCOPE:
```

The CCA Causal Composition Principle applies:

> A downstream causal claim may not inherit authority from an upstream validated relation across a separable transformation unless that transformation is independently identified, prospectively specified and validated as an apparatus guarantee, or explicitly excluded from the claim.

If `STATUS = NOT_CROSSED_BY_CLAIM`, the scientific claim must stop before that transformation.

A deterministic apparatus mapping is not a validated guarantee unless it is prospectively specified and independently validated or mechanically verified over the claimed domain.

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

Where warranted selection or change is part of the object, define the independent mapping before model behavior is observed.

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

What observations count against each proposed mechanism or separable transformation?

## Decision / authorization rule

Prefer conjunctive authorization when all mechanisms are required.

For a claimed path \(\pi\):

\[
\mathrm{ADVANCE}_{\pi}
\iff
\left(\bigwedge_k G_k\right)
\land
\mathrm{PathValid}(\pi).
\]

`PathValid(π)` requires warranted status for every additional separable transformation the claim crosses.

No compensatory score may allow downstream success to erase upstream failure or an invalid middle transformation.

## Implementation validity

Define conditions that make the experiment `UNOBSERVED / INVALID` rather than scientifically negative.

Include failures of any apparatus relation on which causal composition depends.

## Pre-execution freeze

Before `AUTHORIZED`, freeze:

```text
scientific object
claimed causal path
separable transformations and their authority status
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
