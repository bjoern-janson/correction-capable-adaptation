# Research Method Note: Claim Scope, Operators, and Reopenability

**Status: methodological clarification only. No experiment state or scientific result changes.**

## 1. Narrow the claim before enlarging the experiment

When an object is underidentified, first reduce the claim to the smallest contrast supported by the available distinctions. More data, model capacity, apparatus, or experimental complexity does not by itself repair an invalid or overbroad object.

## 2. Record inference scope explicitly

Evidence should be recorded by the kinds of inference it supports, not as one global quality score.

Useful fields:

```text
INFERENCE_SCOPE_GAINED
INFERENCE_SCOPE_RETAINED
INFERENCE_SCOPE_REVOKED
INFERENCE_SCOPE_OUT_OF_SCOPE
NON_IMPLICATIONS
```

Examples:

```text
FIDELITY_PASS does not imply SCIENTIFIC_HYPOTHESIS_PASS
PREDICTIVE_PASS does not imply PROCESS_ATTRIBUTION
AUXILIARY_SOURCE does not imply MATURE_SOURCE
```

## 3. Freeze the operator and protected invariants

For each load-bearing measurement, intervention, transformation, remapping, challenge, or return operation, record:

```text
OPERATOR_ID
PRECONDITIONS
INPUTS
TRANSFORMATION
PROTECTED_INVARIANTS
EQUIVALENCE_RULE
OUTPUT
FAILURE_OR_ABORT_CONDITIONS
MAXIMUM_INTERPRETIVE_SCOPE
```

Compactly:

```text
change THIS; preserve THESE; observe THAT
```

Freezing the operation preserves experimental identity; it does not validate the operation.

## 4. Use M-I-V alignment as a preflight check

Use only as a diagnostic lens:

```text
M = measurement object
I = intervention object
V = evaluation object
```

Before running, ask:

```text
M intended == M realized?
I specified == I realized?
Does V evaluate the object M constituted?
Does transport from M/I to V preserve the distinctions required by the claim?
```

A consequential mismatch leaves the affected interpretation unresolved.

## 5. Validity is not reopenability

A result may remain valid for its original question while retained artifacts are too lossy for a later, more specific question.

Prospectively record the minimum structure needed for the question family intended to remain reopenable:

```text
INTERMEDIATE_OBJECTS
ROW_OR_UNIT_IDENTITY
SPLIT_OR_RANDOMIZATION_IDENTITY
PRE_TRANSFORMATION_OBJECTS
CODE_CONFIG_RUNTIME_IDENTITY
REOPENABLE_QUESTION_FAMILY
QUESTIONS_NOT_GUARANTEED_REOPENABLE
```

Rule:

> Preserve enough intermediate structure to reopen the questions the contract declares reopenable.

This is scoped retention, not a requirement to save everything indefinitely.

## Minimal contract extension

For new empirical contracts, make explicit:

```text
1. scientific object / claim
2. operator and protected invariants
3. M-I-V alignment status
4. inference scope and non-implications
5. reopenability / retention obligations
```
