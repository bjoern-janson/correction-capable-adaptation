# G1 Apparatus Fidelity Audit Protocol

## Status

**FROZEN AUDIT DESIGN — AUDIT PROTOCOL VALID IN DESIGN — CONCRETE APPARATUS UNTESTED — NO IMPLEMENTATION OR EXECUTION AUTHORIZED — G1 UNTESTED**

This protocol defines how a future concrete apparatus is audited against the frozen G1 Apparatus Fidelity Contract.

It does **not** instantiate an apparatus, execute a G1 experiment, estimate a treatment effect, or move empirical G1 authority.

\[
\boxed{
D_{\mathrm{G1\ fidelity\ audit\ protocol}}
=
\mathrm{AUDIT\_PROTOCOL\_VALID\_IN\_DESIGN}
}
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

The audit produces an evidence-based record assigning every required gate a verdict in:

\[
\{\mathrm{PASS},\ \mathrm{FAIL},\ \mathrm{INVALID/UNRESOLVED}\}.
\]

Prose assertions without supporting artifacts are insufficient.

The protocol answers only:

> Does the bound concrete apparatus satisfy the frozen G1 Apparatus Fidelity Contract under an attributable and valid audit?

Protocol validity, apparatus fidelity, execution authority, and a G1 empirical result are distinct objects.

---

## 2. Apparatus referent binding

Before any audit observations are collected, the exact apparatus under test is frozen as:

\[
\boxed{
\mathfrak a_A=(I,V,C,\Gamma,B,Q,R,E,\Omega,P)
}
\]

covering at minimum:

- apparatus and code revision identity;
- configuration;
- renderer and serializer chain;
- selector and adjudicator identities;
- assignment/randomization mechanism;
- reset/isolation regime;
- selector-facing boundary declaration;
- validation domain; and
- provenance scheme.

Every audit artifact and verdict must be attributable to this referent.

\[
\boxed{
\text{load-bearing referent drift}
\Rightarrow
\text{new audit}
}
\]

A `FIDELITY_PASS` does not migrate to a modified apparatus.

Administrative renaming that leaves the complete load-bearing referent unchanged does not by itself constitute drift.

---

## 3. Global attribution gate \(G_0\)

Define:

\[
G_0
=
\text{referent validity}
+
\text{provenance integrity}
+
\text{audit-procedure validity}.
\]

`G_0` passes only if:

1. the observed apparatus matches the prospectively bound referent;
2. required artifacts are authenticated and attributable to that referent;
3. the audit procedure and verdict rules used are the frozen ones; and
4. no post-observation substitution, scope contraction, or provenance break defeats attribution.

Overall aggregation is noncompensatory:

\[
\boxed{
\begin{cases}
G_0\text{ fails}
&\Rightarrow \mathrm{INVALID/UNRESOLVED},\\
G_0\text{ passes and any }A_i=\mathrm{FAIL}
&\Rightarrow \mathrm{FIDELITY\_FAIL},\\
G_0\text{ passes, no FAIL, any unresolved}
&\Rightarrow \mathrm{INVALID/UNRESOLVED},\\
G_0\text{ passes and all }A_i=\mathrm{PASS}
&\Rightarrow \mathrm{FIDELITY\_PASS}.
\end{cases}}
\]

Once `G_0` has passed, a known attributable failure dominates an unrelated unresolved gate. If `G_0` itself fails, apparent component failures are not automatically attributable to the bound apparatus.

---

## 4. Firewall from G1 execution

Audit units and future G1 experimental units are disjoint:

\[
\boxed{
U_{\rm audit}\cap U_{G1}=\varnothing.
}
\]

The following are frozen:

- audit units are designated prospectively as fidelity-validation units only;
- their selections never enter a G1 effect estimate;
- information from audit-unit selections may not be used to tune the treatment, candidate set, null construction, thresholds, selection mechanism, or apparatus;
- audit units cannot later be reclassified as experimental observations; and
- a fidelity audit does not constitute G1 execution.

The apparatus may be exercised as needed to audit the full selector-facing path, but those exercises remain fidelity-validation observations only.

---

## 5. Required audit output

For each audited apparatus referent, the audit produces one structured report:

\[
R_A=
\bigl(
\mathfrak a_A,
\text{artifact hashes},
\text{execution traces},
\text{randomization records},
\text{candidate-set records},
\text{adjudicator isolation evidence},
\text{selector-input captures},
\text{state-reset evidence},
\text{null/evidence pair checks},
\text{gate verdicts}
\bigr).
\]

At minimum, `R_A` must include:

- identities and hashes for every load-bearing static artifact;
- provenance binding the evidence to \(\mathfrak a_A\);
- explicit `G_0` verdict and rationale;
- explicit verdict for every gate \(A_1\) through \(A_7\);
- component-level evidence references;
- unresolved observations retained rather than collapsed; and
- the final apparatus verdict.

The report must be reproducible from the retained evidence package without consulting G1 outcomes.

---

## 6. Gate-by-gate audit rules

### \(A_1\) — Source/interface chain

Required evidence includes:

- frozen specification of \(O_C(X)\rightarrow E\);
- hash or immutable identity of transformation code/configuration; and
- inspectable evidence that no undocumented preprocessing can inject direction information.

`PASS` only if the chain is fully specified, attributable, inspectable, and conforms to the frozen design.

A demonstrated unlicensed directional transformation is `FAIL`. Missing load-bearing transformation evidence is `INVALID/UNRESOLVED` unless an independently sufficient guarantee covers it.

### \(A_{2a}\) — Adjudicator isolation

Required evidence includes process, parameter, prompt, memory, store, and communication-boundary evidence.

`PASS` only if no unlicensed shared parameters, prompts, mutable state, memory, or selector-reachable side channel exists and the isolation claim is mechanically demonstrable.

A demonstrated adjudicator-to-selector side channel is `FAIL`. A potentially consequential path that cannot be resolved is `INVALID/UNRESOLVED`.

### \(A_{2b}\) — Direction validity

`PASS` requires:

\[
\boxed{
\widehat{\mathrm{Agree}}(D_{\rm ind},D_{\rm ref})
\geq
\gamma_{\rm frozen}
}
\]

under a prospectively frozen independent reference criterion.

The following must be frozen before audit outcomes are inspected:

- \(\gamma_{\rm frozen}\);
- sample construction;
- tie/ambiguity/abstention handling; and
- agreement estimator.

The reference criterion must predate the audited units and must not be updated on them.

### \(A_3\) — Candidate-set precedence

`PASS` only if attributable immutable or append-only ordering evidence establishes that \(C\) was locked before any direction information for the unit was available.

Acceptable evidence may include hash chaining, signed event records, monotonic event IDs, or an equivalent prospectively bound mechanism.

Timestamps alone are insufficient.

### \(A_4\) — Mechanical separability

The audit must enumerate all decision-relevant inputs and their assignment rules.

`PASS` only if the variation structure is fully documented and only \(T_E\) varies systematically between arms under the frozen prospective design.

“Balanced” refers to the assignment/randomization mechanism, not realized finite-sample equality.

An undocumented arm-dependent decision input is `FAIL`. A potentially consequential unknown decision input is `INVALID/UNRESOLVED`.

### \(A_5\) — Null package

The audit must apply a **frozen comparison rule** specifying matched coordinates and tolerances prospectively.

`PASS` requires evidence that the null generator preserves the licensed representational structure, format, length, complexity, and exposure burden while remaining independent of \(D\).

The comparison rule may not be weakened after observing audit outputs.

A demonstrated \(D\)-dependent null construction is `FAIL`; inability to adjudicate a load-bearing match coordinate is `INVALID/UNRESOLVED`.

### \(A_6\) — Prospective randomization

Let:

\[
\boxed{
T_E=f(U_{\rm rng},\ \text{licensed randomizer inputs})
}
\]

where \(U_{\rm rng}\) is the exogenous randomizer draw.

`PASS` requires auditing the assignment mechanism and establishing that forbidden inputs cannot reach \(f\), including:

- evidence content \(E\);
- direction \(D\);
- candidate identity/set information not licensed by the assignment design;
- selector prediction;
- expected outcome; and
- outcome-analysis state.

Realized balance is diagnostic, not proof of randomization validity.

### \(A_7\) — Realized-exposure fidelity

Fidelity evidence is split into:

\[
\boxed{F_{\rm static}+F_{\rm per\text{-}episode}.}
\]

#### Static fidelity \(F_{\rm static}\)

Includes at minimum:

- frozen code/configuration;
- process and parameter boundaries;
- complete transformation graph;
- randomizer implementation;
- null generator;
- selector/adjudicator permissions;
- routing configuration; and
- declared selector-facing boundary.

#### Per-episode fidelity \(F_{\rm per\text{-}episode}\)

Includes at minimum:

- candidate-lock ordering;
- assignment provenance;
- reset/isolation completion;
- actual \(S_{\rm realized}\);
- routing/request metadata visible to the selector;
- filenames/identifiers where visible;
- timing class where decision-relevant;
- tool/retrieval/file permissions;
- history/session state; and
- other episode-specific selector-accessible channels.

For \(S_{\rm realized}\), the audit requires capture of the **complete declared selector-accessible boundary**, or an independently sufficient guarantee covering the exact referent and validation domain under the frozen licensed equivalence relation.

Exact byte identity is required only where the frozen equivalence relation makes every byte load-bearing. Licensed transformations may vary only within their prospectively specified equivalence class.

`PASS` requires both:

1. the bound apparatus satisfies the static fidelity requirements; and
2. a prospectively specified per-episode fidelity enforcement/capture mechanism exists for any later G1 execution.

A demonstrated independent treatment/direction cue is `FAIL`.

Any potentially consequential opaque path that cannot be inspected or independently excluded is `INVALID/UNRESOLVED`.

---

## 7. Non-degeneracy record

The audit records the prospective regime-level justification:

\[
\boxed{
0<P(Y_{\rm dir}=1\mid do(T_E=0))<1.
}
\]

The justification must be independent of experimental outcomes.

Finite samples that happen to realize only one outcome do not fail fidelity merely for that reason. Conditioning audit or experimental inclusion on realized or anticipated outcomes is forbidden.

---

## 8. Minimum evidence package

Before a concrete apparatus may receive `FIDELITY_PASS`, the retained audit package must include at minimum:

1. the bound apparatus/revision/configuration manifest;
2. hashes or immutable identities for load-bearing static artifacts;
3. candidate-set ordering records;
4. authenticated randomization records;
5. the frozen independent reference criterion and agreement computation;
6. mechanical adjudicator-selector-outcome isolation evidence;
7. the frozen null comparison rule and validation evidence;
8. the complete declared transformation graph;
9. selector-facing captures or independently sufficient guarantees;
10. reset/isolation evidence;
11. evidence for the per-episode fidelity capture/enforcement mechanism;
12. explicit `G_0` adjudication;
13. explicit \(A_1\)–\(A_7\) verdicts; and
14. a content-hashed final report \(R_A\).

Missing evidence does not default to pass.

---

## 9. Audit procedure

For a future concrete apparatus:

1. freeze \(\mathfrak a_A\) and the audit validation domain before collecting audit observations;
2. prospectively designate \(U_{\rm audit}\);
3. collect the required static and audit-unit evidence without using G1 experimental units;
4. validate `G_0`;
5. adjudicate \(A_1\) through \(A_7\) from retained artifacts only;
6. compute the overall apparatus result using the frozen noncompensatory rule;
7. content-hash and publish/retain \(R_A\) and its provenance package; and
8. stop at the fidelity result.

No successful audit automatically advances to G1 execution.

---

## 10. Concrete apparatus audit states

### `FIDELITY_PASS`

`G_0` passes and every required gate \(A_1\)–\(A_7\) passes for the bound referent and declared validation domain.

This removes the `apparatus untested` blocker only for that referent.

### `FIDELITY_FAIL`

`G_0` passes and at least one necessary gate has an attributable conclusive violation.

### `INVALID/UNRESOLVED`

`G_0` fails, or `G_0` passes but no attributable failure has been established and at least one necessary gate cannot be adjudicated.

Unknown is not pass.

---

## 11. Authority consequences

A `FIDELITY_PASS` licenses only:

> The bound apparatus referent satisfied the frozen G1 apparatus-fidelity requirements over the declared audit domain under the frozen audit protocol.

It does **not** establish:

- that G1 has been executed;
- that a treatment effect exists;
- implementation or execution authority by implication;
- PMC, JT, repeated correction, learning, residual capacity, \(C_{\rm improve}\), or downstream CCA authority.

\[
\boxed{
\mathrm{FIDELITY\_PASS}
\not\Rightarrow
\mathrm{AUTH(execution)}
\not\Rightarrow
G_1\ \mathrm{tested}.
}
\]

Execution authority remains a separate decision after a successful fidelity audit.

---

## 12. Frozen authority stack

\[
\boxed{
\begin{aligned}
D_{\mathrm{G1\ design}}
&=\mathrm{MEASUREMENT\_AND\_TREATMENT\_VALID\_IN\_DESIGN},\\
D_{\mathrm{G1\ apparatus\ contract}}
&=\mathrm{APPARATUS\_FIDELITY\_CONTRACT\_VALID\_IN\_DESIGN},\\
D_{\mathrm{G1\ fidelity\ audit\ protocol}}
&=\mathrm{AUDIT\_PROTOCOL\_VALID\_IN\_DESIGN},\\
D_{\mathrm{G1\ apparatus}}
&=\mathrm{UNTESTED},\\
\mathrm{AUTH(execution)}
&=\mathrm{FALSE},\\
G_1
&=\mathrm{UNTESTED}.
\end{aligned}}
\]

Empirical authority movement from freezing this protocol is zero.

---

## 13. Reopening triggers and stop rule

This protocol may be reopened only by discriminating evidence reaching a frozen requirement, including:

- discovery of a selector-facing channel or artifact class not covered by the protocol;
- a load-bearing referent-drift mode not captured by the binding rule;
- failure of a previously relied-upon guarantee;
- an audit fixture or concrete apparatus showing that the protocol cannot correctly distinguish pass, fail, and unresolved status; or
- evidence that a frozen audit rule systematically misclassifies a scientifically relevant condition.

Implementation inconvenience, compute cost, engineering difficulty, or desire to execute sooner are not reopening triggers.

No conceptual v3 is authorized merely to elaborate the checklist.

The next admissible object is a **concrete apparatus referent and fidelity audit**, not another contract layer.
