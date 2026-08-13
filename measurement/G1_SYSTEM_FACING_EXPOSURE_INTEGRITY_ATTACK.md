# G1 System-Facing Exposure Integrity Attack

## Status and boundary

**LEVEL 0 CANDIDATE EXPOSURE CONSTITUTION / ADVERSARIAL REVIEW — \(\mathcal R\rightarrow S\) ONLY — UPSTREAM \(X\rightarrow\mathcal R\) PRESERVED — \(S\rightarrow D\) UNOPENED — NO G1 EMPIRICAL RESULT — CONTRACT UNFROZEN — NO IMPLEMENTATION OR EXECUTION AUTHORIZED**

This artifact attacks exactly one successor boundary:

\[
\boxed{
\mathcal R_{\mathrm{intended}}
\longrightarrow
S_{\mathrm{system-facing}}
}
\]

It asks whether one prospective apparatus specification can expose the already constituted equality-versus-inequality evidence object without exposing another route to regime identity, warranted direction, or the target decision.

The current chain is:

```text
X → R    object constitution      SURVIVED CANDIDATE ATTACK
R → S    exposure integrity       THIS ARTIFACT
S → D    G1 causal response       NOT OPEN
```

Exposure fidelity and behavioral response remain distinct:

\[
\text{clean }\mathcal R\rightarrow S
\not\Rightarrow
\text{positive }S\rightarrow D,
\]

\[
\text{positive }S\rightarrow D
\not\Rightarrow
\text{clean }\mathcal R\rightarrow S.
\]

No system is selected or queried here. No response, decision, causal effect, success condition, or inferential procedure is defined.

The terminal candidate adjudication is:

```text
CANDIDATE EXPOSURE OBJECT:
  SURVIVED DECLARED INTEGRITY ATTACKS

LIFECYCLE STATE:
  ADVERSARIAL_REVIEW

MEASUREMENT_VALID:
  NO
```

## A. Scientific boundary

### A.1 Preserved upstream object

The protected ancestor constitutes the persistent registers \(s_1,s_2\), their binary values, the equality and inequality propositions, and the evidence regimes:

\[
\mathcal R_\alpha=\{00,11\},
\qquad
\mathcal R_\beta=\{01,10\},
\]

with both labeled record orders admitted. The persistent decision referents remain:

\[
D\in\{\alpha,\beta,\bot\}.
\]

No regime name, expected answer, recommendation, or evaluator-only truth belongs to either evidence regime. This artifact neither revises that object nor repeats its warrant proof.

### A.2 Successor question

The successor question is:

\[
\boxed{
\text{Can the complete pre-decision exposure preserve that object while every}
\text{ other treatment-dependent system-facing path is closed?}
}
\]

The target is an exposure constitution, not a claim that any system detects equality, follows a warrant, or changes a decision.

## B. Exact system-facing state

The word “prompt” is too narrow. Let \(c(r)\) denote the canonical labeled record derived from an admitted realization \(r\). Define the complete system-facing state as:

\[
S(r)=(K_{\mathrm{sci}},K_{\mathrm{app}},H_{\mathrm{pre}},c(r)),
\qquad r\in\mathcal R_\alpha\cup\mathcal R_\beta.
\]

The coordinates are:

- \(K_{\mathrm{sci}}\): the fixed objective, persistent register referents, equality/inequality propositions, candidate meanings, abstention meaning, and action-coordinate meanings;
- \(K_{\mathrm{app}}\): the complete fixed apparatus envelope, including message roles and ordering, scaffolding, wrapper text, serialization convention, whitespace, punctuation, source identity, candidate order, available interface affordances, and any tool or context envelope;
- \(H_{\mathrm{pre}}\): all system-accessible pre-exposure history, memory, cache, conversation, batch, schedule, prior-task, and persistent state;
- \(c(r)\): the canonical, labeled, lossless exposure of the two intended register observations.

For this minimal candidate:

```text
K_sci   is identical across every exposure;
K_app   is identical across every exposure;
H_pre   is empty at the scientific boundary because each exposure uses a fresh,
        causally isolated instance;
c(r)    is the only treatment-dependent coordinate of S.
```

The complete evaluator state is a separate object:

\[
M_{\mathrm{eval}}
=
(A,B,\text{warranted direction},\text{randomization state},\text{audit identity},\ldots).
\]

Evaluator-side fields, encodings, randomization artifacts, audit identifiers, and scoring state are excluded from \(S\). Deriving \(A\), \(B\), or the warranted direction solely from the licensed labeled register pair is intended and is not leakage. Any separate route through which the tested system can read, infer, inherit, or query those values outside \(c(r)\) places that route in \(S\) and invalidates the exclusion.

This is a boundary-relative constitution. It does not assert metaphysical knowledge of every hidden platform state. An eventual apparatus would have to expose a finite, auditable system boundary matching these coordinates; that validation is not performed here.

## C. Candidate exposure law

### C.1 Assignment and state realization

Let \(A\in\{\alpha,\beta\}\) be the current evidence-regime assignment, and let \(\mathcal F_{\mathrm{pre}}\) contain every fact available to the fresh system instance before exposure. Require:

\[
P(A=\alpha\mid\mathcal F_{\mathrm{pre}})
=
P(A=\beta\mid\mathcal F_{\mathrm{pre}})
=\frac12.
\]

The realized assignment and randomization state remain evaluator-private until the evidence itself crosses the boundary.

Independently draw a nuisance bit \(B\in\{0,1\}\) with:

\[
P(B=0\mid A,\mathcal F_{\mathrm{pre}})
=
P(B=1\mid A,\mathcal F_{\mathrm{pre}})
=\frac12.
\]

Construct the labeled register state:

\[
x(A,B)=
\begin{cases}
(B,B), & A=\alpha,\\
(B,1-B), & A=\beta.
\end{cases}
\]

Therefore:

\[
P(00\mid\mathcal R_\alpha)
=P(11\mid\mathcal R_\alpha)
=\frac12,
\]

\[
P(01\mid\mathcal R_\beta)
=P(10\mid\mathcal R_\beta)
=\frac12,
\]

and all four labeled states have unconditional probability \(1/4\).

This exact uniformity is not imposed for visual neatness. Write:

\[
a=P(00\mid\mathcal R_\alpha),
\qquad
b=P(01\mid\mathcal R_\beta).
\]

Neutrality of the \(s_1\) value requires \(a=b\); neutrality of the \(s_2\) value requires \(a=1-b\). Hence \(a=b=1/2\). Together with a neutral arm prior, the four-state law is forced if no single register-coordinate glyph value may predict direction.

This is an exposure law, not a finite-sample balance guarantee, sample-size rule, or statistical procedure. Chance empirical imbalance does not change the law, and empirical balance alone does not prove the law was followed.

### C.2 Presentation and serialization

Every state is canonicalized into the same fixed labeled order:

```text
Register s1 displays: <0 or 1>
Register s2 displays: <0 or 1>
```

The fixed order \(s_1\) then \(s_2\) is treatment- and state-independent. Equal random use of both orders is not logically necessary for exposure integrity. If a later object retains both orders in realized support, the weaker sufficient condition is one common order kernel:

\[
P(O=o\mid A,x,\mathcal F_{\mathrm{pre}})=q_o
\]

for every arm and state, with the same positive \(q_o\) for each retained order. No equal-order requirement follows merely from symmetry.

Canonicalization selects one realization from the upstream order-equivalence class; it does not alter the labeled register assignment or the upstream warrant.

### C.3 Fixed exposure envelope

Across arms and states, the candidate fixes:

- one task statement and one scientific objective;
- one register naming convention and one candidate/action dictionary;
- candidate order \([\alpha,\beta,\bot]\);
- one wrapper, message-role sequence, punctuation, whitespace, and serialization convention;
- one source identity and one interface/tool envelope;
- no case ID, filename, path, timestamp, regime label, answer field, expected decision, seed, or arm-relative schema;
- no prior conversation, trial, cache, memory, batch position, schedule, or tool state;
- no treatment-dependent retry, routing, truncation, salience, affordance, or hidden instruction.

Differences in the two register values are licensed because they are the constituted evidence. The equality/inequality relation of the complete labeled pair is intended to predict direction; removing that relation would remove the evidence object itself.

## D. Fidelity mapping

Let \(\operatorname{state}(r)\) recover the persistent labeled assignment from an admitted upstream realization \(r\), independent of its record order. Let \(\operatorname{canon}\) encode that assignment in the fixed order above, so that:

\[
c(r)=\operatorname{canon}(\operatorname{state}(r)).
\]

Define the exposure mapping \(g:\mathcal R\rightarrow S\) by:

\[
g(r)=S(r)=
\bigl(K_{\mathrm{sci}},K_{\mathrm{app}},\varnothing,c(r)\bigr).
\]

The required fidelity properties are:

1. **Labeled-state preservation:** a fixed projection \(\pi_X\) satisfies
   \[
   \pi_X(g(r))=\operatorname{state}(r).
   \]
2. **Persistent referents:** \(s_1,s_2,\alpha,\beta,\bot\) retain the same meanings and availability under every realization.
3. **Order normalization only:** two upstream records with the same labeled assignment may map to the same canonical exposure; distinct labeled assignments do not.
4. **No added direction field:** every treatment-dependent coordinate of \(g(r)\) is part of the labeled register assignment.
5. **No interpretation claim:** fidelity concerns exposed scientific content and apparatus paths, not the system's internal representation or reasoning.

The local transformation chain is:

\[
r
\longrightarrow
\text{decoded labeled assignment}
\longrightarrow
\text{canonical record}
\longrightarrow
\text{fixed envelope}
\longrightarrow
S.
\]

Each arrow must be deterministic or governed by the same arm-independent prospective law, must preserve the labeled assignment, and must add no independent direction cue. A downstream platform transformation not represented by this chain remains outside the candidate's declared authority; a positive response could not validate it retrospectively.

## E. Pre-treatment boundary

Consider matched worlds:

```text
WORLD ALPHA: upcoming assignment A = alpha
WORLD BETA:  upcoming assignment A = beta
```

Before evidence exposure, both worlds contain the same \(K_{\mathrm{sci}}\), the same \(K_{\mathrm{app}}\), and an empty \(H_{\mathrm{pre}}\). The current fair assignment draw and its state are inside \(M_{\mathrm{eval}}\), not the system boundary. No arm-dependent unit creation, routing, role, wrapper, candidate order, source, permission, schedule, or prior state is available.

Thus the candidate imposes the structural condition:

\[
S_{\mathrm{pre}}^{\alpha}=S_{\mathrm{pre}}^{\beta}
\]

at the declared boundary. This is the operative closure claim. No information-theoretic estimator or threshold is selected.

Fresh isolation matters. A superficially balanced without-replacement block can leak its final assignment to a persistent system that observes earlier arms. Marginal 50/50 assignment is insufficient; the fair-current-arm condition must hold conditional on all accessible pre-treatment history. The minimal candidate removes that history rather than introducing sequential adaptation for realism.

## F. Nuisance audit

| Channel | Can it predict regime direction? | Prospective constraint and adjudication |
|---|---|---|
| One glyph at a fixed register/position | No under the law | Each fixed-coordinate glyph value is marginally fair in both arms. |
| Register-specific value | No under the law | Both \(s_1\) and \(s_2\) are individually fair conditional on either arm. |
| Complete labeled pair | Yes | Equality versus inequality is the constituted evidence relation, not nuisance leakage. Pair-wide glyph counts or presence features may also predict direction when they are extensionally equivalent to that licensed relation. |
| Display position | No | Register labels and the fixed \(s_1,s_2\) positions never change. |
| Record order | No | One common fixed order is used for every arm and state. |
| Template / wrapper | No | Exact wrapper, roles, punctuation, whitespace, and schema are fixed. |
| Source identity | No | One source/interface identity is fixed and carries no arm field. |
| Metadata | No within the candidate | IDs, paths, timestamps, seeds, regime and answer fields are absent from \(S\). |
| Candidate order | No | \([\alpha,\beta,\bot]\), meanings, and availability are fixed. |
| Case identity | No | There is no system-facing case or task-instance identifier. |
| Schedule | No | Current assignment is fair conditional on the complete accessible baseline and is evaluator-private. |
| History / persistent state | No | Each exposure begins in a fresh causally isolated instance with empty \(H_{\mathrm{pre}}\). |
| Realization frequency | No at the constituted law | Fair arms plus the forced within-arm laws make all single-coordinate atomic value features direction-neutral. |
| Randomization artifacts | No within the candidate | Randomization seed, scheduler/block state, audit identifiers, and expected-answer fields remain evaluator-only; realized register values cross only through \(c(r)\). |
| Hidden transformation | No within the stated chain | Every treatment-dependent transformation is explicit, fidelity-preserving, and arm-independent except for intended values. Actual platform conformance remains a residual. |

Set-level support alone would not establish these results. They follow from the prospective exposure law and fixed boundary. Conversely, an observed balanced table would not establish that the structural exclusions held.

## G. Countermodel table

| Countermodel | Held fixed | Varied | Failure established | Survives / fails | Required repair if local |
|---|---|---|---|---|---|
| `case_alpha_001` versus `case_beta_001`, an answer field, filename, or source tag exposes the arm | Intended register state and warrant | System-facing metadata | An alternate direction path bypasses the evidence relation | Candidate **survives** only because all such fields are excluded from \(S\); any occurrence **fails** the realization | Exclude the field before exposure and re-audit the complete boundary; never relabel it as evidence after a response |
| Alpha uses \(s_1\)-first while beta uses \(s_2\)-first | Register values and task | Serialization order | Order directly identifies arm | Candidate **survives** through one common fixed order | Use one prospectively common order law; outcome-dependent normalization is forbidden |
| Alpha uses one wording, role, punctuation, or schema and beta another | Scientific propositions | Wrapper or template | Pragmatic or structural direction cue enters \(S\) | Candidate **survives** through one fixed envelope | Restore one arm-independent envelope before any run |
| \(.99/.01\) within-arm state frequencies | Valid four-state support | Realization law | Single-coordinate register values predict arm despite support symmetry | Candidate **survives** because the conditional laws are each \(.5/.5\) | Reject the asymmetric exposure law; observed responses cannot repair it |
| Alternating arms or a public blocked schedule | Intended current record | Schedule | Arm is inferable before treatment | Candidate **survives** through conditional fair assignment and no accessible schedule | Remove the schedule path or the affected realization from authority before exposure |
| **False-clean balanced block:** a persistent system sees earlier draws from an exactly balanced without-replacement block and infers the final arm | Marginal arm counts, state counts, wrapper, order, metadata | Conditional assignment given history | Visible and marginal checks pass while pre-treatment closure fails | This alternative **fails**; exact balance is not sufficient | Require fresh isolation and a fair current draw conditional on every accessible pre-state |
| Candidate order follows warranted direction | Evidence and candidate labels | Candidate placement or availability | Position/default supplies the target action | Candidate **survives** through fixed order and common availability | Fix the action coordinate prospectively; arm-relative mapping kills the comparison |
| The visible record is faithful, but a template engine adds a hidden arm key | Intended visible content | Intermediate transformation | Unaudited \(\mathcal R\rightarrow T_i\rightarrow S\) arrow adds a bypass | Candidate **survives** only for its explicit chain; such an actual transform **fails** conformance | Bring the transform into the finite boundary and validate it independently before exposure |
| Prior conversation, cache, memory, or tool state encodes the last arm and schedule | Current intended state | Persistent state | Current exposure is not the sole treatment-dependent input | Candidate **survives** through fresh isolated instances | Reset or exclude the affected apparatus before acquiring data; do not filter afterward |
| Evaluator randomization, expected direction, or audit ID leaks through a message name, tool schema, environment, or inherited state | Scientific record and scoring need | Evaluator/system separation | \(M_{\mathrm{eval}}\) becomes causally available in \(S\) | Candidate **survives** only under causal inaccessibility; leakage **fails** it | Separate the boundary prospectively and verify every crossing interface |
| A renderer truncates, swaps, or duplicates one register value | Upstream object and assignment | Exposure fidelity | The system does not receive the constituted labeled state | Candidate mapping rejects it | Correct and revalidate the transformation before use; never infer fidelity from behavior |
| Candidate semantics or action tokens change meaning across arms | Surface tokens and perhaps responses | Persistent scientific referents | The two arms no longer expose one common decision object | Candidate **fails** | Restore one arm-independent ontology before any exposure; no positive response rescues it |
| The platform routes arms through different permissions, tools, latency classes, or hidden runtime state | Intended record and nominal wrapper | Complete system-facing apparatus | A treatment-dependent non-evidence path remains | Outside candidate authority and therefore **fails** as an instantiation | Either hold it fixed inside a validated boundary or exclude the resulting apparatus from the claim |

The strongest false-clean construction is the balanced without-replacement block. It can satisfy equal counts, all four state frequencies, fixed presentation, and visible metadata checks while history makes the upcoming arm predictable. The candidate survives that attack only because it requires a fresh causal instance and conditional, not merely marginal, assignment neutrality.

Shallow use of an intended glyph-pair relation is not an exposure-integrity failure. The question of how a system uses \(S\) belongs to the unopened \(S\rightarrow D\) boundary.

## H. Authority gained if survived

The maximum allowed conclusion is:

> One prospective system-facing exposure specification can instantiate the already constituted G1 evidence object while excluding the declared alternative exposure channels and preserving the intended pre-treatment information boundary.

More exactly, the candidate shows conceptual existence of one direct, fixed-envelope, fresh-instance exposure law in which the only treatment-dependent system-facing content is the licensed labeled register state. This is candidate apparatus constitution, not apparatus implementation or empirical validation.

Record the result as:

```text
CANDIDATE EXPOSURE OBJECT SURVIVED DECLARED INTEGRITY ATTACKS
```

## I. Authority not gained

The candidate supplies:

```text
no system response result
no G1 causal effect
no estimator
no effect threshold
no sample-size rule
no statistical test or success criterion
no selected model or API
no benchmark or dataset
no prompt-performance claim
no response parser
no implementation validation
no empirical execution
no frozen G1 contract
no representation-invariance or transport claim
no internal-mechanism or semantic-understanding claim
no G2
no PMC
no repeated-correction evidence
no JT
no viability
no AGI or ASI authority
```

The candidate does not turn a clean exposure into evidence that a system uses it. Nor could future correct behavior authorize an exposure that violated this constitution.

## J. Death conditions

The candidate must be recorded as:

```text
CANDIDATE G1 EXPOSURE INSTANTIATION:
  FAILED EXPOSURE-INTEGRITY CONSTITUTION
```

if any inspection establishes that:

- regime direction is available before the intended evidence exposure;
- metadata, source, wrapper, serialization, layout, candidate order, or action availability supplies an uncontrolled direction cue;
- realization frequencies make a single-coordinate nuisance feature direction-predictive outside the declared law;
- candidate, register, action, or abstention semantics drift across arms;
- an apparatus transformation loses, swaps, fabricates, or supplements the constituted evidence object;
- evaluator-only fields or encodings become system-facing directly or through an unlicensed path other than the constituted register evidence, including tools, routing, or persistence;
- accessible history or a schedule predicts the current assignment;
- the complete exposure boundary cannot be stated and audited sufficiently to distinguish intended acquisition from a bypass.

No model response, downstream success, balanced realized table, or post hoc exclusion can rescue one of these failures. A changed exposure would be an explicit successor or amendment, not a reinterpretation of this candidate.

## Provenance and preserved ancestor

The protected lineage is:

```text
0ffdf60   canonical authority baseline
    ↓
d9639d3 / PR #19   X→R candidate ancestor
    ↓
this artifact      R→S exposure-integrity successor
```

Immediate scientific ancestry:

- [`G1_EVIDENCE_OBJECT_CONSTITUTION_ATTACK.md`](G1_EVIDENCE_OBJECT_CONSTITUTION_ATTACK.md) — the exact protected \(X\rightarrow\mathcal R\) parent and source of the live frequency, fidelity, metadata, and pre-treatment residual;
- [`../lineage/decisions/G1_LEVEL0_ROLE.md`](../lineage/decisions/G1_LEVEL0_ROLE.md) — the scoped G1 role and authority ceiling;
- [`../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md) — local authority to inspect each separable \(\mathcal R\rightarrow T_1\rightarrow\cdots\rightarrow S\) arrow;
- [`README.md`](README.md) — measurement navigation and the current empirical blocker.

Governing method, not scientific parentage:

- [`../CARS.md`](../CARS.md);
- [`../KINTSUGI.md`](../KINTSUGI.md);
- [`../lineage/decisions/RESEARCH_RETURNABILITY_RULE.md`](../lineage/decisions/RESEARCH_RETURNABILITY_RULE.md).

The ancestor is not rewritten to make these exposure constraints appear earlier than they did. Canonical `main`, PR #19, `research_state.json`, both evidence ledgers, all decision records, and every empirical or execution flag remain unchanged.

## Terminal report and stopping rule

```text
EXPOSURE INTEGRITY:
  SURVIVED

UPSTREAM OBJECT:
  X→R PRESERVED

AUTHORITY GAINED:
  ONE PROSPECTIVE SYSTEM-FACING EXPOSURE SPECIFICATION CAN INSTANTIATE
  THE CONSTITUTED EVIDENCE OBJECT WHILE EXCLUDING THE DECLARED ALTERNATIVE
  EXPOSURE CHANNELS AND PRESERVING THE PRE-TREATMENT INFORMATION BOUNDARY

AUTHORITY NOT GAINED:
  NO SYSTEM RESPONSE, G1 EFFECT, MEASUREMENT-VALID, CONTRACT, MODEL,
  ESTIMATOR, THRESHOLD, IMPLEMENTATION, EXECUTION, OR DOWNSTREAM AUTHORITY

EXPOSURE LAW:
  FAIR CURRENT ARM CONDITIONAL ON THE COMPLETE ACCESSIBLE PRE-STATE;
  FAIR WITHIN-ARM NUISANCE BIT; FOUR STATES UNCONDITIONALLY 1/4 EACH;
  ONE FIXED ARM-INDEPENDENT LABELED ORDER AND EXPOSURE ENVELOPE

PRE-TREATMENT CLOSURE:
  FRESH ISOLATED INSTANCE; MATCHED ARM WORLDS HAVE IDENTICAL SYSTEM-FACING
  PRE-STATE; ASSIGNMENT AND EVALUATOR STATE REMAIN CAUSALLY INACCESSIBLE

NUISANCE CHANNELS CLOSED:
  SINGLE-COORDINATE GLYPH AND REGISTER MARGINALS, ORDER, POSITION, TEMPLATE, SOURCE,
  METADATA, CANDIDATE ORDER, CASE IDENTITY, SCHEDULE, HISTORY, FREQUENCY,
  EVALUATOR FIELDS, AND DECLARED TRANSFORMATIONS

LIVE RESIDUAL:
  AN ACTUAL PLATFORM MUST STILL ESTABLISH COMPLETE BOUNDARY COVERAGE,
  RESET/ISOLATION, TRANSFORMATION FIDELITY, AND EVALUATOR SEPARATION;
  NONE IS EMPIRICALLY VALIDATED HERE

NEXT BOUNDARY IF SURVIVED:
  S→D causal response constitution

EMPIRICAL AUTHORITY MOVEMENT:
  0

CANONICAL MAIN:
  UNCHANGED

PR #19:
  UNMERGED
```

The candidate resolves the conceptual exposure-integrity question relative to its declared finite boundary. The actual-platform residual is deliberately not converted into implementation work. The next causal boundary remains unopened:

\[
\boxed{S\rightarrow D\text{ is out of scope}.}
\]

Therefore:

\[
\boxed{r=0\Rightarrow\text{STOP THIS ATTACK}.}
\]

Do not test a system. Do not merge anything. Preserve this candidate exposure specification as the next inspectable ancestor.
