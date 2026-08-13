# G1 Measurement + Treatment Contract

## Status

**FROZEN DESIGN CONTRACT — MEASUREMENT AND TREATMENT VALID IN DESIGN — APPARATUS FIDELITY UNTESTED — G1 UNTESTED — NO IMPLEMENTATION OR EXECUTION AUTHORIZED**

This artifact freezes the design-level scientific object, treatment contrast, estimand, authority ceiling, and stopping rule for G1.

It does **not** instantiate an apparatus, validate realized fidelity, select numerical operating thresholds for a concrete execution, authorize implementation, execute an experiment, or move empirical G1 authority.

\[
\boxed{
D_{\mathrm{G1\ contract}}
=
\mathrm{MEASUREMENT\_AND\_TREATMENT\_VALID\_IN\_DESIGN}
}
\]

The design-level contract is frozen. Any future apparatus-specific implementation must prospectively instantiate every still-concrete operating quantity required below before outcome data are observed.

---

## 1. Scientific object

\[
G_1:
\quad
\text{Does an independently constituted evidence package }(E,D)
\text{ causally alter a separable candidate-selection decision in direction }D\text{?}
\]

The scientific object is the **evidence package** \((E,D)\), not bare evidence \(E\).

This prevents the experiment from conflating evidential content with the displayed direction supplied to the selector.

Let the prospectively frozen candidate set be \(C\). Direction is typed as:

\[
\boxed{D\subseteq C.}
\]

Thus \(D\) is the subset of candidates favored by the independently adjudicated evidence package.

A future apparatus-specific instantiation must prospectively specify the handling of:

- ties;
- ambiguous adjudication;
- abstention or indeterminate reference judgments; and
- \(D=\varnothing\).

None of these cases may be resolved after observing selection outcomes.

---

## 2. Authority pipeline

\[
O_C(X)
\rightarrow
E_{\rm adm}
\rightarrow
D_{\rm ind}
\rightarrow
(E,D)
\rightarrow
T_E
\rightarrow
\pi
\rightarrow
C_{\rm selected},
\]

where:

- \(O_C(X)\) is the constituted observation/interface object for candidate behavior;
- \(E_{\rm adm}\) is evidence that has passed its admissibility requirements;
- \(D_{\rm ind}\) is direction adjudicated independently of the selector and outcome analysis;
- \((E,D)\) is the treatment evidence package;
- \(T_E\) is the randomized treatment indicator;
- \(\pi\) is the fixed candidate-selection mechanism or policy under test; and
- \(C_{\rm selected}\in C\) is the realized selection.

Authority may move only through this pipeline. Downstream behavior cannot retroactively repair an invalid upstream gate.

---

## 3. Upstream gates

All gates must be satisfied prospectively before outcome-bearing execution.

| Gate | Requirement |
|---|---|
| \(A_1\) | Source/interface measurement validity of \(O_C(X)\). |
| \(A_{2a}\) | Adjudicator independence from the selector and from outcome analysis. |
| \(A_{2b}\) | Direction-adjudication validity: agreement with a **frozen independent reference criterion** at a prospectively specified acceptance rate. |
| \(A_3\) | Candidate set \(C\) frozen **before** any evidence direction is known. |
| \(A_4\) | Mechanical separability: only \(T_E\) varies systematically between treatment arms. |
| \(A_5\) | Null package \(N(E)\) is structurally matched and direction-independent. |
| \(A_6\) | Prospective randomization of \(T_E\), statistical criterion, estimand decision rule, and practical margin fixed before outcomes. |

This artifact freezes these requirements, not apparatus-specific numerical values that have not yet been constituted. Missing concrete values at future execution time imply **no execution authority**, not permission to choose them after outcome inspection.

---

## 4. Treatment

\[
T_E\in\{0,1\}.
\]

### Treatment arm

\[
T_E=1:
\]

The selector receives the evidence package \((E,D)\).

### Control arm

\[
T_E=0:
\]

The selector receives a matched null package \(N(E)\).

The null package must match the treatment package in representational structure, format, length, complexity, and exposure burden while remaining independent of \(D\).

Treatment assignment is prospective randomization and must be independent of:

- potential outcomes;
- candidate identity;
- evidence content;
- adjudicator output; and
- any other pre-treatment variable not explicitly included in a prospectively randomized and balanced design.

---

## 5. Selection mechanism

\[
\pi:
\quad
\text{fixed system state + candidate set + received package}
\rightarrow
C_{\rm selected}.
\]

The mechanism \(\pi\) is part of the scientific referent.

Mechanical separability requires candidate set, system state, instruction or prompt, budget, time limit, and random-seed policy to be fixed or prospectively randomized and balanced across treatment arms.

A load-bearing change to \(\pi\) creates a new experimental referent.

---

## 6. Primary outcome and estimand

Define:

\[
Y_{\rm dir}
=
\mathbf 1[C_{\rm selected}\in D].
\]

The primary causal estimand is:

\[
\boxed{
\tau_{\rm dir}
=
P(Y_{\rm dir}=1\mid do(T_E=1))
-
P(Y_{\rm dir}=1\mid do(T_E=0)).
}
\]

This estimand asks whether receiving the independently constituted evidence package causally changes selection toward the independently adjudicated direction.

### Secondary diagnostic

Whether selection changes at all across treatment arms may be recorded as a secondary diagnostic.

It is **not** a success gate for G1.

---

## 7. Independence and baseline constraints

### 7.1 One independent episode per experimental unit

Each experimental unit contributes one independent episode.

No state may carry over across episodes unless the dependence structure, persistence channel, and corresponding analysis are explicitly modeled and prospectively specified.

Unmodeled carry-over invalidates the causal treatment contrast.

### 7.2 Non-degenerate control-generating regime

The required population/support condition is:

\[
\boxed{
0
<
P(Y_{\rm dir}=1\mid T_E=0)
<
1.
}
\]

This is a property of the **prospectively constituted control-generating regime**.

It is **not** a requirement that every finite realized control sample contain both outcome values. A finite all-zero or all-one control realization does not by itself constitute protocol failure.

Candidate sets and directions may not be selected to manufacture an easy or deterministic treatment effect.

---

## 8. Decisive outcomes

### 8.1 Positive

A positive result requires:

1. \(\tau_{\rm dir}\) to satisfy the prospectively frozen statistical criterion and practical margin; and
2. all gates \(A_1\) through \(A_6\) to remain intact.

A positive result licenses only:

> Under this frozen contract and realized apparatus, the independently constituted evidence package \((E,D)\) causally controlled candidate selection in direction \(D\) under the tested selection mechanism \(\pi\).

It does not license any broader authority.

### 8.2 Negative

If the frozen success criterion is not met while all protocol gates remain intact, the result is negative for this contract and referent.

It is retained as lineage evidence only.

### 8.3 Inconclusive

The result is inconclusive if any load-bearing gate fails, including:

- failed or invalid randomization;
- broken mechanical separability;
- invalid or unverified direction adjudication;
- state carry-over not covered by the frozen design;
- treatment/null mismatch;
- apparatus-fidelity failure; or
- failure of the prospectively constituted control-generating regime.

A broken gate is not a negative causal result.

---

## 9. Explicit non-claims

A positive result does **not** establish:

- modification efficacy;
- PMC;
- repeated correction;
- JT;
- residual capacity;
- \(C_{\rm improve}\);
- learning;
- persistent adaptation;
- general responsiveness to evidence;
- transfer beyond this evidence-package family;
- transfer beyond this candidate-selection mechanism \(\pi\); or
- any downstream causal-composition claim.

In particular:

\[
\boxed{
G_1\text{ success}
\not\Rightarrow
C_{\rm improve}.
}
\]

---

## 10. Frozen design-state adjudication

\[
\boxed{
\begin{aligned}
\text{Scientific object} &: \mathrm{VALID\_IN\_DESIGN}\\
\text{Treatment contrast} &: \mathrm{IDENTIFIED\_IN\_PRINCIPLE}\\
\tau_{\rm dir} &: \mathrm{WELL\_TYPED}\\
\text{Authority ceiling} &: \mathrm{LOCAL}\\
\text{Apparatus fidelity} &: \mathrm{UNTESTED}\\
G_1\text{ result} &: \mathrm{UNTESTED}\\
\text{Execution authority} &: \mathrm{NONE}.
\end{aligned}
}
\]

No empirical authority moves by freezing this design contract.

---

## 11. Lifecycle boundary

The next admissible sequence is:

\[
\boxed{
\text{FROZEN DESIGN CONTRACT}
\rightarrow
\text{APPARATUS FIDELITY}
\rightarrow
\text{AUTHORIZED EXECUTION}
\rightarrow
\tau_{\rm dir}
\rightarrow
\text{LOCAL }G_1\text{ ADJUDICATION}.
}
\]

The states are distinct:

\[
\boxed{
\text{contract validity}
\neq
\text{apparatus fidelity}
\neq
\text{G1 empirical result}.
}
\]

A valid design does not validate its realization. A valid realization does not itself establish a causal effect. A causal G1 result does not purchase downstream CCA claims.

---

## 12. Reopening and stopping rule

The design contract may be reopened only by:

- discriminating evidence that reaches a frozen gate; or
- a concrete apparatus/realization failure that demonstrates the frozen design cannot identify its intended object.

The following are **not** reopening triggers:

- desire for a broader claim;
- desire for additional ontology;
- desire to make the contract more comprehensive in the absence of a discriminating failure; or
- favorable or unfavorable downstream outcomes.

Therefore:

\[
\boxed{
\text{NO v5 WITHOUT A REALIZED DISCRIMINATING FAILURE.}
}
\]

Future criticism must attach to implementation fidelity, randomization, isolation, treatment/null separability, reference adjudication, or realized measurement unless new evidence directly invalidates this design object.

---

## 13. Provenance and authority preservation

This artifact is a noncanonical stacked successor to the G1 measurement-validity lineage.

Immediate predecessor:

- [`G1_FIDELITY_MEASUREMENT_VALIDITY_ATTACK.md`](G1_FIDELITY_MEASUREMENT_VALIDITY_ATTACK.md) — establishes local in-principle measurement validity for the realized-exposure fidelity object and leaves contract freeze as the next boundary.

Relevant protected ancestors:

- [`G1_REALIZED_EXPOSURE_FIDELITY_ATTACK.md`](G1_REALIZED_EXPOSURE_FIDELITY_ATTACK.md);
- [`G1_SYSTEM_FACING_EXPOSURE_INTEGRITY_ATTACK.md`](G1_SYSTEM_FACING_EXPOSURE_INTEGRITY_ATTACK.md);
- [`G1_EVIDENCE_OBJECT_CONSTITUTION_ATTACK.md`](G1_EVIDENCE_OBJECT_CONSTITUTION_ATTACK.md);
- [`../methodology/G1_APPARATUS_AUTHORIZATION_DEADLOCK_ATTACK.md`](../methodology/G1_APPARATUS_AUTHORIZATION_DEADLOCK_ATTACK.md);
- [`../methodology/RESEARCH_STATE_MACHINE.md`](../methodology/RESEARCH_STATE_MACHINE.md).

This successor does not modify those ancestors, canonical `main`, state files, ledgers, empirical results, implementation flags, or execution authority.

---

## Terminal report

```text
OBJECT:
  G1 MEASUREMENT + TREATMENT DESIGN CONTRACT

DESIGN CONTRACT:
  FROZEN

D_G1_CONTRACT:
  MEASUREMENT_AND_TREATMENT_VALID_IN_DESIGN

SCIENTIFIC OBJECT:
  VALID_IN_DESIGN

DIRECTION TYPE:
  D SUBSET_OF C

TREATMENT:
  PROSPECTIVELY RANDOMIZED (E,D) PACKAGE VS STRUCTURALLY MATCHED,
  DIRECTION-INDEPENDENT NULL PACKAGE N(E)

PRIMARY OUTCOME:
  Y_dir = 1[C_selected IN D]

PRIMARY ESTIMAND:
  tau_dir = P(Y_dir=1 | do(T_E=1)) - P(Y_dir=1 | do(T_E=0))

CONTROL SUPPORT CONDITION:
  0 < P(Y_dir=1 | T_E=0) < 1
  AS A PROPERTY OF THE CONTROL-GENERATING REGIME,
  NOT A FINITE-SAMPLE BALANCE REQUIREMENT

AUTHORITY CEILING:
  LOCAL TO THIS PACKAGE FAMILY, CANDIDATE SET CONSTITUTION,
  SELECTION MECHANISM, AND REALIZED APPARATUS

APPARATUS FIDELITY:
  UNTESTED

G1 EMPIRICAL RESULT:
  UNTESTED

IMPLEMENTATION:
  NOT AUTHORIZED

EXECUTION:
  NOT AUTHORIZED

EMPIRICAL AUTHORITY MOVEMENT:
  0

NEXT BOUNDARY:
  APPARATUS FIDELITY

REOPENING:
  ONLY DISCRIMINATING EVIDENCE AT A FROZEN GATE OR
  CONCRETE APPARATUS FAILURE
```

Do not instantiate the apparatus from this artifact alone. Do not execute G1. Do not infer downstream authority.