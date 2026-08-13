# G1 Apparatus Fidelity Contract

## Status

**FROZEN DESIGN CONTRACT — APPARATUS FIDELITY CONTRACT VALID IN DESIGN — CONCRETE APPARATUS UNTESTED — NO IMPLEMENTATION OR EXECUTION AUTHORIZED — G1 UNTESTED**

This artifact freezes the minimum fidelity requirements that a concrete apparatus must satisfy to count as a candidate realization of the already-frozen G1 Measurement + Treatment Design Contract.

It does **not** instantiate an apparatus, audit a running system, authorize implementation, authorize execution, estimate a treatment effect, or move empirical G1 authority.

\[
\boxed{
D_{\mathrm{G1\ apparatus\ contract}}
=
\mathrm{APPARATUS\_FIDELITY\_CONTRACT\_VALID\_IN\_DESIGN}
}
\]

The running-apparatus result remains a separate object:

\[
D_{\mathrm{G1\ apparatus}}
\in
\{
\mathrm{FIDELITY\_PASS},
\mathrm{FIDELITY\_FAIL},
\mathrm{INVALID/UNRESOLVED}
\}.
\]

At freeze:

\[
\boxed{
D_{\mathrm{G1\ apparatus}}=\mathrm{UNTESTED},
\qquad
\mathrm{AUTH(execution)}=\mathrm{FALSE},
\qquad
G_1=\mathrm{UNTESTED}.
}
\]

---

## 1. Purpose

This contract answers only:

> Does a concrete apparatus implement the frozen G1 design without breaking independence, isolation, ordering, randomization, or the realized selector-facing exposure boundary?

The contract defines design-valid fidelity requirements. A future audit of a concrete running apparatus is a separate empirical/engineering object.

---

## 2. Authority typing

The stacked design state is:

\[
\begin{aligned}
D_{\mathrm{G1\ design}}
&=\mathrm{MEASUREMENT\_AND\_TREATMENT\_VALID\_IN\_DESIGN},\\
D_{\mathrm{G1\ apparatus\ contract}}
&=\mathrm{APPARATUS\_FIDELITY\_CONTRACT\_VALID\_IN\_DESIGN},\\
D_{\mathrm{G1\ apparatus}}
&=\mathrm{UNTESTED},\\
\mathrm{AUTH(execution)}
&=\mathrm{FALSE},\\
G_1
&=\mathrm{UNTESTED}.
\end{aligned}
\]

Passing this contract establishes only that the fidelity requirements are adequate in design for the declared scope.

A running apparatus is never labeled `VALID_IN_DESIGN`. It must instead receive one of the audit states in §8.

No apparatus-fidelity result licenses modification efficacy, PMC, repeated correction, JT, residual capacity, \(C_{\rm improve}\), learning, or any other downstream claim.

---

## 3. Required temporal and causal chain

A conforming apparatus must enforce and audit the complete chain:

\[
\boxed{
C\ \mathrm{locked}
\rightarrow
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
S_{\rm realized}
\rightarrow
\pi
\rightarrow
C_{\rm selected}
}
\]

where the symbols retain their meanings from the frozen G1 Measurement + Treatment Design Contract.

Fidelity concerns the **realized selector-facing exposure** \(S_{\rm realized}\), not merely whether upstream generators executed in the intended order.

A future audit must therefore establish both temporal precedence and the fidelity of the realized interface actually available to the selector.

---

## 4. Gate-by-gate fidelity requirements

| Design gate | Fidelity requirement |
|---|---|
| \(A_1\) | The source/interface chain \(O_C(X)\rightarrow E\) is fixed, documented, and inspectable. No undocumented transformation may inject direction information. |
| \(A_{2a}\) | The adjudicator is isolated from the selector and outcome-analysis pipeline. No shared parameters, prompts, memory, mutable state, or unlicensed side channels. Isolation must be mechanically demonstrable. |
| \(A_{2b}\) | Direction labels agree with the frozen independent reference criterion. The criterion is fixed before experimental units and is not updated on them. |
| \(A_3\) | Candidate set \(C\) is locked before direction information for the unit is available. Auditable records must establish temporal precedence. |
| \(A_4\) | Only \(T_E\) varies systematically between arms. All other decision-relevant inputs are fixed or prospectively randomized under a frozen assignment design. “Balanced” refers to the prospective design/randomization mechanism, not realized finite-sample equality. |
| \(A_5\) | Null package \(N(E)\) is produced by a frozen procedure preserving representational structure, format, length, complexity, and exposure burden while remaining independent of \(D\). |
| \(A_6\) | \(T_E\) is prospectively randomized independently of potential outcomes, evidence content, adjudicator output, and candidate identity. Randomization records are immutable and attributable to the bound apparatus referent. |
| **\(A_7\)** | **Realized-exposure fidelity holds at the complete selector-facing boundary defined in §5.** |

These gates are conjunctive. Success at one gate cannot compensate for failure or unresolved status at another.

---

## 5. Realized-exposure fidelity — \(A_7\)

### 5.1 Transformation boundary

Every renderer, serializer, formatter, wrapper, routing layer, or other transformation between the constituted treatment object and the selector-facing input must be:

1. prospectively frozen; or
2. prospectively licensed under an explicit equivalence relation that states what may vary and why the variation is scientifically inert.

Undocumented transformations cannot silently inherit fidelity authority.

### 5.2 Complete selector-facing boundary

The final system-facing boundary must contain no independent treatment or direction cue outside the licensed package.

The audit boundary must include every experimentally controlled or system-accessible path by which arm identity, \(D\), evaluator information, history, or state could reach the selector, including where applicable:

- routing metadata;
- filenames and identifiers;
- timestamps or timing classes;
- tool availability and permissions;
- retrieval state;
- files and stores;
- conversation or session history;
- evaluator-derived fields;
- scheduler state;
- environment or request metadata;
- persistent memory or cache;
- any other selector-accessible coordinate.

A channel capable of carrying treatment/direction information remains load-bearing until independently shown inaccessible or irrelevant within the bound apparatus referent.

### 5.3 No independent direction cue

No selector-accessible channel outside the licensed package may independently encode or predict:

- \(T_E\);
- \(D\);
- expected selection;
- adjudicator output; or
- evaluator state relevant to the decision.

A demonstrated unlicensed cue is `FIDELITY_FAIL`.

A potentially consequential channel whose accessibility or content cannot be resolved is `INVALID/UNRESOLVED`.

### 5.4 Reset and isolation

Reset/isolation must cover every experimentally controlled or selector-accessible persistence path capable of carrying information across experimental units.

A nominally fresh prompt, request ID, or conversation is not sufficient by itself.

Persistent state may be permitted only when its dependence structure is prospectively specified, modeled, and included in the frozen design. Otherwise attributable carry-over is a fidelity failure; unresolved potentially consequential persistence is `INVALID/UNRESOLVED`.

### 5.5 Audit target

Fidelity auditing must inspect the **realized interface**, not merely generator source code or generation logs.

A correct package generator followed by a leaking renderer or platform boundary does not pass.

---

## 6. Non-degeneracy

The frozen non-degeneracy requirement is prospective and regime-level:

\[
\boxed{
0<P(Y_{\rm dir}=1\mid do(T_E=0))<1.
}
\]

It must be justified for the constituted control-generating regime using information independent of the experimental outcomes.

Finite samples that happen to realize only one outcome remain valid realizations of a non-degenerate regime. They are not discarded merely for empirical degeneracy.

Conditioning the analyzed sample on realized or anticipated outcomes is forbidden.

---

## 7. Hard failure and invalidity conditions

### 7.1 Fidelity failures

Subject to a valid attributable audit, the following are sufficient for `FIDELITY_FAIL`:

- an adjudicator-to-selector side channel;
- null-package construction that depends on \(D\);
- candidate-set generation after direction information becomes available;
- treatment assignment influenced by evidence content, adjudicator output, candidate identity, expected outcome, or other forbidden input;
- unmodeled cross-unit state or memory carry-over;
- a demonstrated undocumented transformation that injects directional information;
- leakage of arm identity or \(D\) through metadata, timing, filenames, permissions, history, routing, evaluator state, tools, or persistence;
- mutable or falsified randomization, ordering, or isolation records that establish a protocol violation;
- any other attributable violation of a necessary gate in §§4–6.

### 7.2 Invalid / unresolved states

The following yield `INVALID/UNRESOLVED` when they prevent attribution of a pass or fail:

- a potentially consequential selector-facing channel cannot be inspected or independently excluded;
- required provenance is missing;
- randomization, ordering, transformation, or isolation records are unavailable or cannot be bound to the concrete apparatus;
- the apparatus differs materially from the prospectively bound referent;
- a relied-upon guarantee does not cover the exact implementation/domain being audited;
- a necessary fidelity component cannot be adjudicated and no independently attributable failure has already falsified the conjunction.

Unknown is not pass.

---

## 8. Concrete apparatus audit states

After an apparatus is instantiated and audited, assign exactly one result:

### `FIDELITY_PASS`

All required gates and realized-interface fidelity requirements are attributable, auditable, and satisfied for the bound apparatus referent and validation domain.

### `FIDELITY_FAIL`

At least one necessary requirement has an attributable, conclusive violation under an otherwise valid audit.

### `INVALID/UNRESOLVED`

The audit cannot validly determine fidelity because a load-bearing referent, observation, provenance, guarantee, or potentially consequential channel remains unresolved.

Only `FIDELITY_PASS` removes the `apparatus untested` blocker.

It does **not** grant execution authority.

---

## 9. Minimum audit evidence for a future concrete apparatus

Before a concrete apparatus can receive `FIDELITY_PASS`, the audit must include at minimum:

1. a bound apparatus/revision/configuration manifest;
2. candidate-set generation records demonstrating temporal precedence;
3. authenticated randomization records for \(T_E\);
4. the frozen independent reference criterion and evidence that it preceded experimental units;
5. mechanical evidence of adjudicator-selector-outcome isolation;
6. the null-package generator specification and prospectively declared validation cases;
7. a complete declared transformation graph to the selector-facing boundary;
8. selector-facing captures or independently sufficient guarantees covering the final boundary;
9. reset/isolation evidence for every controlled or selector-accessible persistence path;
10. a procedure for classifying attributable failures separately from `INVALID/UNRESOLVED` observations;
11. evidence that the concrete apparatus and audit correspond to the frozen referent rather than a post-result substitute.

The future audit may add apparatus-specific observations needed to instantiate these obligations, but it may not weaken them after outcome data are observed.

---

## 10. Reopening triggers

This contract may be reopened only by discriminating evidence that reaches a frozen requirement, including:

- discovery of a side channel or realized-interface failure not protected by the current requirements;
- failure of a previously relied-upon apparatus guarantee;
- evidence that a listed constraint is insufficient to preserve a frozen G1 design assumption; or
- a concrete apparatus failure showing that the current fidelity object cannot distinguish pass, fail, and unresolved status as intended.

Implementation inconvenience, compute cost, engineering difficulty, or desire to execute sooner are not reopening triggers.

No conceptual v3 is authorized merely to elaborate the checklist.

---

## 11. Relationship to execution authority

Even after all three conditions hold:

1. the G1 Measurement + Treatment Design Contract is frozen;
2. this G1 Apparatus Fidelity Contract is frozen; and
3. a concrete apparatus receives `FIDELITY_PASS`;

execution authority remains a separate decision.

\[
\boxed{
\mathrm{FIDELITY\_PASS}
\not\Rightarrow
\mathrm{AUTH(execution)}
\not\Rightarrow
G_1\ \mathrm{tested}.
}
\]

No fidelity result establishes a treatment effect.

The next admissible transition after this contract is therefore:

\[
\boxed{
\text{frozen apparatus contract}
\rightarrow
\text{instantiate concrete apparatus}
\rightarrow
\text{fidelity audit}
\rightarrow
\{\mathrm{FIDELITY\_PASS},\mathrm{FIDELITY\_FAIL},\mathrm{INVALID/UNRESOLVED}\}
\rightarrow
\text{separate execution-authorization decision}.
}
\]

---

## 12. Frozen authority summary

```text
G1 MEASUREMENT + TREATMENT DESIGN CONTRACT
  MEASUREMENT_AND_TREATMENT_VALID_IN_DESIGN

G1 APPARATUS FIDELITY CONTRACT
  APPARATUS_FIDELITY_CONTRACT_VALID_IN_DESIGN

CONCRETE G1 APPARATUS
  UNTESTED

APPARATUS IMPLEMENTATION
  NOT AUTHORIZED BY THIS CONTRACT

EXECUTION AUTHORITY
  FALSE

G1 EMPIRICAL RESULT
  UNTESTED

DOWNSTREAM AUTHORITY
  NONE
```

This is the stopping point for contract elaboration. The next failure, if any, must come from apparatus realization or fidelity audit rather than an unforced expansion of the design ontology.
