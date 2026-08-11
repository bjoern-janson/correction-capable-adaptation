# G1 Evidence-Object Constitution Attack

## Status and boundary

**LEVEL 0 CANDIDATE CONSTRUCTION / ADVERSARIAL REVIEW — \(X\rightarrow\mathcal R\) ONLY — NO G1 EMPIRICAL RESULT — CONTRACT UNFROZEN — NO IMPLEMENTATION OR EXECUTION AUTHORIZED**

This artifact constitutes and attacks one synthetic candidate evidence object. It asks only:

\[
\boxed{
\text{Can one exact }X\text{ support two independently warranted, system-facing,}
\text{ non-instructional, non-coded evidence regimes?}
}
\]

It does not ask whether a system responds to either regime. In particular, it does not open:

\[
\mathcal R\rightarrow D.
\]

The terminal adjudication is:

```text
CANDIDATE TREATMENT OBJECT:
  SURVIVED LEVEL-0 CONSTITUTION ATTACK

LIFECYCLE STATE:
  ADVERSARIAL_REVIEW

LOCAL ADJUDICATION:
  CANDIDATE SURVIVED THE DECLARED LEVEL-0 ATTACKS

MEASUREMENT_VALID:
  NO
```

## A. Exact candidate object

### A.1 Fixed synthetic world

Let the persistent registers be:

\[
S=\{s_1,s_2\},
\]

and let each register display one glyph from:

\[
V=\{0,1\}.
\]

The exact state space is the set of total register assignments:

\[
X=V^S.
\]

There is no hidden physical state behind this object. The displayed register assignment is the synthetic task state.

### A.2 Persistent decision referents

Before any evidence exposure, fix the candidate propositions:

\[
C_\alpha(x):=\bigl[x(s_1)=x(s_2)\bigr],
\]

\[
C_\beta(x):=\bigl[x(s_1)\neq x(s_2)\bigr].
\]

The persistent separable decision coordinate is:

\[
D\in\{\alpha,\beta,\bot\},
\]

where:

```text
alpha = select candidate proposition C-alpha
beta  = select candidate proposition C-beta
bottom = abstain
```

The meanings of \(\alpha\), \(\beta\), and \(\bot\) do not vary with the evidence regime. \(C_\alpha\) and \(C_\beta\) are mutually exclusive and exhaustive on \(X\). Consequently, \(\bot\) is not warranted by either of the two candidate regimes; it remains a persistent decision value rather than a third arm.

### A.3 State partition

Partition \(X\) prospectively by the fixed propositions:

\[
X_\alpha
=
\{x\in X:x(s_1)=x(s_2)\}
=
\{(0,0),(1,1)\},
\]

\[
X_\beta
=
\{x\in X:x(s_1)\neq x(s_2)\}
=
\{(0,1),(1,0)\}.
\]

The subscripts record which already-fixed proposition the state entails. They are not answer fields and are not system-facing.

### A.4 System-facing evidence contents

An evidence realization is a lossless record of the two register observations:

```text
register s1 displays <0 or 1>
register s2 displays <0 or 1>
```

The two records may be presented in either order. Let \(O=S_2\) be the two possible record-order permutations and let \(e_o(x)\) be the ordered serialization of the same labeled register assignment under \(o\in O\). The lossless decoder \(\delta\) satisfies:

\[
\delta(e_o(x))=x.
\]

The candidate regimes are the families:

\[
\mathcal R_\alpha
=
\{e_o(x):x\in X_\alpha,\ o\in O\},
\]

\[
\mathcal R_\beta
=
\{e_o(x):x\in X_\beta,\ o\in O\}.
\]

Thus \(\mathcal R_\alpha\) contains the visible states `00` and `11`, in both labeled-record orders. \(\mathcal R_\beta\) contains `01` and `10`, also in both orders.

Every realization uses the same:

- two persistent register identities;
- glyph alphabet;
- record count;
- field names;
- serialization family;
- source class;
- candidate meanings;
- absence of recommendation, answer, validity, and regime-label fields.

`R-alpha`, `R-beta`, the partition name, and any expected decision are evaluator-side bookkeeping only. They are not members of a system-facing realization.

### A.5 Declared pre-treatment boundary

The pre-treatment boundary contains only:

```text
register identities: s1, s2
glyph alphabet:      0, 1
candidate meanings: alpha, beta, abstention
record schema:       two labeled register observations
licensed order set:  both record orders
state space:         all four register assignments remain possible
```

It excludes the realized register values, any regime identifier, any answer label, any state-correlated case identifier, and any prior or schedule information correlated with the realized equality relation.

The boundary is therefore identical for \(X_\alpha\) and \(X_\beta\). The abstract construction does not require the target relation to be available before the two register values are exposed. An actual apparatus that leaks the realized partition through metadata, history, source, or ordering would not instantiate this candidate.

## B. Independent warrant argument

For every \(r\in\mathcal R_\alpha\), the prospective definitions close the entailment:

\[
r\in\mathcal R_\alpha
\Rightarrow
\delta(r)\in X_\alpha
\Rightarrow
C_\alpha(\delta(r)),
\]

and therefore \(r\) supports \(\alpha\).

For every \(r\in\mathcal R_\beta\), analogously:

\[
r\in\mathcal R_\beta
\Rightarrow
\delta(r)\in X_\beta
\Rightarrow
C_\beta(\delta(r)),
\]

and therefore \(r\) supports \(\beta\).

This is a deductive entailment internal to the stipulated synthetic object. It is not evidence about an external world and it is not a proof of system capability.

The warrant mapping exists before any tested system is selected. If a system ignores the record, chooses the opposite referent, abstains, or emits nonsense, the equalities above remain unchanged. System behavior therefore has no validating or corrective role in the warrant.

## C. System-accessibility argument

Everything required to determine the directional warrant is system-facing within the object:

1. the identities of \(s_1\) and \(s_2\);
2. the observed glyph at each register;
3. the fixed meanings of \(\alpha\) and \(\beta\).

Nothing required for the warrant is reserved to an evaluator. In particular, the object excludes:

- a hidden true register assignment different from the displayed assignment;
- a private generator label;
- an evaluator-only regime identifier;
- a scoring-only expected answer;
- inaccessible metadata needed to interpret the glyphs.

Two evaluator worlds that deliver the same complete labeled record must therefore assign the same warrant under this object. If an evaluator demands different directions while holding the entire system-facing object fixed, the evaluator has changed or supplemented the object outside the declared boundary.

This is a constitution claim about available information. It is not evidence that any future apparatus faithfully exposes that information to a tested system.

## D. Anti-instruction argument

Neither regime contains an imperative, recommendation, correctness label, or action value. A realization says only what each persistent register displays.

The fixed pre-treatment candidate definitions state what \(\alpha\) and \(\beta\) mean; they do not state which proposition holds in the realized state. Stable decision semantics are required for a common decision object and are not a treatment-specific recommendation.

The warrant is carried by a relation between two observations:

\[
x(s_1)=x(s_2)
\quad\text{or}\quad
x(s_1)\neq x(s_2),
\]

not by text of the form `choose alpha` or `choose beta`.

## E. Anti-codebook attack

### E.1 Strongest simple nuisance-code explanation

The strongest simple attack is that a token, register, position, source, or latest record might act as an arbitrary answer code.

The candidate blocks those explanations at the object level:

- each glyph occurs at each register in both regime families;
- each register can appear first or last in both families;
- each possible final atomic observation—`s1=0`, `s1=1`, `s2=0`, `s2=1`—occurs in both families;
- both regimes use the same source, record count, labels, fields, and serialization class;
- globally exchanging glyph names `0` and `1` preserves regime membership;
- exchanging record order preserves regime membership.

No individual glyph, register identity, record position, source, format, or latest atomic assertion identifies the warranted direction.

Only the joint equality relation separates \(\mathcal R_\alpha\) from \(\mathcal R_\beta\). That relation is the prospectively fixed proposition under evaluation, not an accidental nuisance code.

This is a set-level symmetry statement, not a probability or weighting claim. No realization-frequency law is constituted here. Unequal frequencies in a future apparatus could make a nuisance feature predict direction even when both supports contain that feature; that possibility belongs to later treatment and inference constitution.

### E.2 Authority ceiling

A finite policy could memorize all four complete labeled records or compute an extensionally equivalent feature such as the parity of the glyph sum. That does not make the evidence object arbitrary: those policies key on the complete warrant-bearing state relation.

Level 0 neither identifies nor requires an internal mechanism of evidence use. Consequently, this artifact does not establish semantic understanding, relational reasoning, generalization, representation invariance, or immunity to complete-pattern lookup.

## F. Matched countermodels

### F.1 Direct recommendation

**COUNTERMODEL**

Either add `choose alpha`, `choose beta`, `correct answer`, or a recommendation field to the otherwise valid record, or argue that a complete equality/inequality record is already recommendation-equivalent because the fixed candidate definitions make its consequence decisive.

**WHAT IT HOLDS FIXED**

The register assignment, candidate meanings, and equality relation.

**WHAT IT VARIES**

It introduces a treatment-dependent action command.

**WHAT FAILURE IT WOULD ESTABLISH**

Any later directional response could be instruction following rather than control by evidence about the task state.

**WHETHER THE CANDIDATE SURVIVES**

**SURVIVES.** The constituted realization contains no command or recommendation field. Adding one creates a malformed descendant treatment, not a realization of \(\mathcal R_\alpha\) or \(\mathcal R_\beta\). The stronger equivalence attack also fails: the records state task facts, not an imperative or answer field, and their entailment remains fixed under arbitrary system behavior. Decisive evidence is not thereby an instruction.

### F.2 Arbitrary codebook

**COUNTERMODEL**

Attach `U` to every \(\alpha\)-warranting record and `V` to every \(\beta\)-warranting record, or use a source, format, or fixed record position as the regime key.

**WHAT IT HOLDS FIXED**

The warrant-bearing register values and persistent candidate meanings.

**WHAT IT VARIES**

It adds an arm-correlated nuisance feature with no task-state semantics.

**WHAT FAILURE IT WOULD ESTABLISH**

The directional identity would be available from an arbitrary answer code independently of the constituted evidence relation.

**WHETHER THE CANDIDATE SURVIVES**

**SURVIVES THE ENUMERATED DETERMINISTIC CODE FAMILY.** Such fields are excluded, and the allowed glyph, register, position, and order nuisances have matched support across the two regime families. A full-record lookup remains possible but is not a nuisance-only codebook attack. No probabilistic nuisance-balance claim is made.

### F.3 Latest-assertion compliance

**COUNTERMODEL**

Use the rule `select the candidate associated with the last register assertion`, without comparing the two observations.

**WHAT IT HOLDS FIXED**

The two labeled register facts and their equality relation.

**WHAT IT VARIES**

It changes which labeled observation is presented last.

**WHAT FAILURE IT WOULD ESTABLISH**

A fixed order could make recency, rather than the evidence relation, predict the warranted direction.

**WHETHER THE CANDIDATE SURVIVES**

**SURVIVES.** Both record orders occur in both regimes, and every possible last atomic observation occurs in each regime family. Latest-assertion identity alone cannot determine equality versus inequality.

### F.4 Evaluator-only truth

**COUNTERMODEL**

Hold the complete system-facing record fixed while an evaluator privately declares opposite register values or an opposite expected candidate.

**WHAT IT HOLDS FIXED**

Everything available to the system, including both labeled glyph observations and candidate meanings.

**WHAT IT VARIES**

It changes only evaluator-private state or scoring preference.

**WHAT FAILURE IT WOULD ESTABLISH**

If the expected direction changed, the alleged warrant would depend on information outside the evidence boundary.

**WHETHER THE CANDIDATE SURVIVES**

**SURVIVES.** In the constituted synthetic object, the displayed assignment is the task state. Evaluator-private contradiction has no authority. A task with a hidden state behind the display would be a different object requiring a separate evidence-fidelity argument.

### F.5 Pre-treatment leakage

**COUNTERMODEL**

Reveal the realized partition through a task identifier, filename, source, candidate order, prior message, schedule, or other assignment-correlated context before the register record arrives.

**WHAT IT HOLDS FIXED**

The later valid register record and warrant mapping.

**WHAT IT VARIES**

It makes the target distinction causally available before the intended evidence exposure.

**WHAT FAILURE IT WOULD ESTABLISH**

The acquisition interpretation would be unidentified even if a later response matched the warrant.

**WHETHER THE CANDIDATE SURVIVES**

**SURVIVES PROSPECTIVE CONSTITUTION.** The declared abstract pre-treatment boundary is identical across the state partition and contains no realized-state correlate. This establishes only that the object does not require pre-treatment leakage. Whether an apparatus actually preserves that boundary belongs to system-facing exposure integrity, not this artifact.

### F.6 Outcome-defined warrant

**COUNTERMODEL**

Call whichever proposition the system later selects `warranted`, or retain only states on which its response appears correct.

**WHAT IT HOLDS FIXED**

The observed register record.

**WHAT IT VARIES**

It changes the warrant or task inclusion rule after observing system behavior.

**WHAT FAILURE IT WOULD ESTABLISH**

The evidence object would be circular and could not support G1.

**WHETHER THE CANDIDATE SURVIVES**

**SURVIVES.** The partition of all four states and the candidate meanings are fixed without reference to any system, output, or outcome.

### F.7 Persistent-referent failure

**COUNTERMODEL**

Redefine \(\alpha\) to select \(C_\alpha\) in one regime and \(C_\beta\) in the other, redefine \(\bot\) between regimes, or make the same decision value select a different proposition under each regime.

**WHAT IT HOLDS FIXED**

The visible symbols.

**WHAT IT VARIES**

It changes the decision ontology across regimes.

**WHAT FAILURE IT WOULD ESTABLISH**

The comparison would contain two different scientific objects rather than one persistent decision object under different evidence.

**WHETHER THE CANDIDATE SURVIVES**

**SURVIVES.** Candidate and abstention meanings are global, fixed before exposure, and not regime-relative. Any such semantic change is outside \(X\) and outside both candidate regimes.

## G. Authority gained if the object survives

The maximum conclusion is:

> **A candidate bidirectional G1 evidence treatment can be prospectively constituted such that its directional warrant is independently established, system-facing, and not reducible under the tested countermodels to direct action recommendation, arbitrary nuisance coding, latest-assertion compliance, evaluator-only truth, pre-treatment leakage, or outcome-defined warrant.**

More narrowly, this construction supplies an existence witness at the exact synthetic-object level. It preserves one nonempty route from the canonical G1 role toward a future treatment constitution.

The scientific burden moves from:

```text
Can any exact bidirectional object deserve to be called evidence?
```

to, only if separately opened:

```text
Can an apparatus faithfully and exclusively expose this object to a system?
```

## H. Authority not gained

This artifact establishes none of the following:

```text
no G1 empirical result
no evidence that any model uses either regime
no treatment-assignment result
no system-facing exposure-integrity result
no pre-treatment-closure result in an implemented apparatus
no response-capture result
no causal estimand or estimator
no effect-size or success threshold
no sample-size, randomization, or uncertainty procedure
no frozen measurement or experiment contract
no benchmark, dataset, model, or prompt
no representation-invariance or generalization result
no internal-mechanism or semantic-understanding result
no implementation or execution authorization
no G2 or causal-composition result
no PMC
no repeated-correction evidence
no JT
no C_improve result, measurement, or authority movement
no viability
no AGI, recursive-improvement, or ASI authority
```

Object validity does not imply system capability, and a future system response cannot retrospectively validate this object.

## I. Death condition

The candidate must be recorded as:

```text
CANDIDATE G1 INSTANTIATION:
  FAILED LEVEL-0 OBJECT CONSTITUTION
```

if any future inspection shows that the exact candidate necessarily requires:

- a treatment-dependent recommendation or action field;
- an arbitrary nuisance code to identify the directional regime;
- evaluator-only information to determine the warrant;
- unstable register, candidate, or abstention meanings;
- pre-treatment availability of the realized directional distinction;
- system behavior or downstream outcomes to define warrant;
- a non-system-facing hidden state that the visible record does not independently warrant.

Such a failure may not be rescued by a successful model response. A revised object would require an explicit successor or amendment preserving this failed construction.

## Provenance and preserved authority

The lineage seam is:

```text
G1 role decision
+ closed G1 adversarial lineage
+ relational-codebook feasibility and impossibility witnesses
→ one scoped X-to-R candidate construction and attack
```

Immediate scientific ancestors:

- [`../lineage/decisions/G1_LEVEL0_ROLE.md`](../lineage/decisions/G1_LEVEL0_ROLE.md) — fixes the scoped G1 role and preserves semantic constitution as an upstream layer;
- [`README.md`](README.md) — records the current measurement frontier and semantic-validity priority;
- [`regression-cases/RELATIONAL_CODEBOOK_WITNESSES.md`](regression-cases/RELATIONAL_CODEBOOK_WITNESSES.md) — establishes that universal relational codebooks fail while ontology-conditional constructions can exist;
- [`../lineage/EVIDENCE_LEDGER.md`](../lineage/EVIDENCE_LEDGER.md) — preserves G1-A3 through G1-A8 and the current G1 role;
- [`../lineage/evidence-ledger.yaml`](../lineage/evidence-ledger.yaml) — preserves the historical broad-versus-relational blocker and mirrors the current machine-readable G1 role and status.

Governing methodological authority:

- [`../CARS.md`](../CARS.md);
- [`../methodology/RESEARCH_STATE_MACHINE.md`](../methodology/RESEARCH_STATE_MACHINE.md);
- [`../lineage/decisions/RESEARCH_RETURNABILITY_RULE.md`](../lineage/decisions/RESEARCH_RETURNABILITY_RULE.md);
- [`../KINTSUGI.md`](../KINTSUGI.md).

No ancestor's scientific authority is rewritten. `research_state.json`, the G1 role decision, both evidence ledgers, and every empirical result remain unchanged. The only ancestor-file edit is the non-authority navigation link in the measurement README.

## Terminal report and stopping rule

```text
OBJECT CONSTITUTION:
  SURVIVED

AUTHORITY GAINED:
  ONE EXACT SYNTHETIC BIDIRECTIONAL X-TO-R CANDIDATE
  SURVIVED THE DECLARED LEVEL-0 OBJECT ATTACKS

AUTHORITY NOT GAINED:
  NO G1 CAPABILITY, MEASUREMENT-VALID, CONTRACT, IMPLEMENTATION,
  EXECUTION, OR DOWNSTREAM AUTHORITY

LIVE RESIDUAL:
  ACTUAL EXPOSURE MAY INTRODUCE METADATA, SERIALIZATION,
  APPARATUS, OR PRE-TREATMENT LEAKAGE; NO SUCH CLAIM IS OPEN HERE

NEXT BOUNDARY IF SURVIVED:
  SYSTEM-FACING EXPOSURE INTEGRITY

REPOSITORY CHANGES:
  THIS CANDIDATE / ATTACK ARTIFACT ONLY,
  PLUS ONE NON-AUTHORITY NAVIGATION LINK

EMPIRICAL AUTHORITY MOVEMENT:
  0
```

At this exact abstract-object boundary and relative to the declared countermodels, the attacks leave no further discriminating residual. Realization frequency, composite apparatus nuisances, fidelity, metadata, and actual pre-treatment closure remain deliberately unopened at the next boundary:

\[
\boxed{r=0\Rightarrow\text{STOP THIS ATTACK}.}
\]

The next boundary must be opened separately.
