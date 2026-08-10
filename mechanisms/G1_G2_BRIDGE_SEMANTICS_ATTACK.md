# Attack: What Would Make the G1-to-G2 Bridge a Coherent Causal Object?

## Status

**ADVERSARIAL SCIENTIFIC ANALYSIS — NO STATE TRANSITION — NO IMPLEMENTATION**

This document attacks the next scientific-design boundary in Correction-Capable Adaptation (CCA):

> **When does a warranted selected decision constitute a legitimate causal precursor to an independently effective modification?**

The analysis is deliberately upstream of ontology, benchmark, model, prompt, estimator, threshold, and implementation choices.

It does **not**:

- freeze a G1 experiment;
- freeze a G2 experiment;
- select an ontology;
- select a candidate or modification language;
- select a model or prompt;
- construct a benchmark;
- choose statistical thresholds;
- modify `research_state.json`;
- authorize ECIM implementation;
- authorize empirical execution.

The purpose is destructive:

> **Try to show that independently successful G1 and G2 assays do not establish an evidence-to-modification pathway unless an additional causal bridge is itself well defined and identified.**

---

# 1. Canonical starting point

CCA has provisionally fixed the scientific role of G1 as:

\[
\boxed{
G_1
=
\text{warranted evidence acquiring causal control over a separable adaptive decision}
}
\]

with candidate selection as the current operational instantiation:

\[
E\rightarrow C_{\mathrm{selected}}.
\]

G2 remains independently identified through direct intervention on modification:

\[
\boxed{
do(M=m)\rightarrow(Y_T,Y_P)
}
\]

where \(Y_T\) represents target efficacy and \(Y_P\) protected-behavior consequences.

The hard separation is:

\[
\boxed{
G_1\not\Rightarrow G_2.
}
\]

The current question is what, if anything, legitimately connects them.

---

# 2. First attack: `G1 -> G2` is not literally a causal graph

A category error appears if the notation

\[
G_1\rightarrow G_2
\]

is read literally.

`G1` and `G2` are **properties / identified gates**, not object-level causal variables.

A causal graph must instead contain variables such as:

```text
E        evidence assignment
C        selected adaptive decision / candidate
D        adoption / deployment state
M        modification actually assigned or instantiated
Y_T      target outcome
Y_P      protected outcome
```

A candidate object-level pathway is:

\[
E\rightarrow C\rightarrow D\rightarrow M\rightarrow(Y_T,Y_P).
\]

Then:

- `G1` is a property of the \(E\rightarrow C\) relation;
- `G2` is a property of the \(M\rightarrow(Y_T,Y_P)\) relation under direct \(do(M=m)\);
- the missing scientific object concerns the middle relation \(C\rightarrow D\rightarrow M\).

Therefore:

\[
\boxed{
\text{the G1-to-G2 bridge, if real, must be identified at the variable level.}
}
\]

This is the first central result of the attack.

---

# 3. Selection, adoption, and modification are not interchangeable

The minimal decomposition should distinguish:

\[
\boxed{
\text{selection}\neq\text{adoption}\neq\text{modification}.
}
\]

## 3.1 Selection

A candidate identity or adaptive decision is chosen:

\[
C=c.
\]

This is an epistemic / decision-level event.

## 3.2 Adoption or deployment

Some process decides whether and how the selected candidate is accepted, translated, scheduled, gated, or deployed:

\[
D=d.
\]

Possible values can include:

```text
accept
reject
no-op
defer
translate
partial application
fallback
```

The exact state space is not frozen here.

## 3.3 Modification

A concrete intervention reaches the adaptive system:

\[
M=m.
\]

This is the object on which G2 requires direct causal intervention.

A system can therefore select the right candidate and still fail to modify.

It can also modify successfully for reasons unrelated to the selected candidate.

---

# 4. The strongest naive composition fails

A tempting inference is:

\[
G_1>0
\land
G_2>0
\Rightarrow
E\rightarrow C\rightarrow M\rightarrow Y.
\]

This is invalid.

The two component assays can both be positive while the middle path is absent.

## Counterexample A — independent successful assays

Suppose evidence assignment controls candidate selection:

\[
E\rightarrow C
\]

with a valid positive G1 result.

Separately, direct modification assignment demonstrates:

\[
do(M=m)\rightarrow Y
\]

with a valid positive G2 result.

But in the deployed system, modification is chosen by an independent process \(U\):

\[
U\rightarrow M
\]

and

\[
C\not\rightarrow M.
\]

Then:

\[
G_1>0,\qquad G_2>0,
\]

while there is no evidence that selection participates in modification.

Therefore:

\[
\boxed{
G_1>0\land G_2>0
\not\Rightarrow
\text{evidence-controlled modification}.
}
\]

This counterexample succeeds.

---

# 5. Counterexample B — adoption gate blocks all selected changes

Suppose G1 succeeds:

\[
E\rightarrow C^*(E).
\]

Suppose the modification family is independently efficacious under direct assignment:

\[
do(M=m)\rightarrow Y_T
\]

with acceptable protected effects.

But the deployment rule is:

\[
D=\mathrm{reject}
\]

for every selected candidate.

Then the realized pathway is:

\[
E\rightarrow C
\rightarrow D=\mathrm{reject}
\rightarrow M=\varnothing.
\]

Both component competencies exist, but the bridge has zero throughput.

This is not a G1 failure and not a G2 failure.

It is a distinct bridge/adoption failure.

Thus:

\[
\boxed{
\text{bridge failure is not reducible to selection failure or modification efficacy failure.}
}
\]

---

# 6. Counterexample C — selected identity is translated into the wrong modification

Let there be a prospectively intended mapping:

\[
\phi:C\rightarrow\mathcal M
\]

where \(\phi(c_i)=m_i\) denotes the modification that operationally instantiates candidate \(c_i\).

Suppose G1 correctly selects \(c_i\), and G2 shows that direct \(do(M=m_i)\) produces the desired effect.

But the bridge translator implements:

\[
\tilde\phi(c_i)=m_j,\qquad j\neq i.
\]

Then selection is warranted and the intended modification is efficacious, but the deployed mapping is wrong.

The failure locus is neither G1 nor G2.

It is translation / bridge identity.

This yields another required distinction:

\[
\boxed{
\text{candidate identity}\neq\text{modification identity}.
}
\]

A prospective mapping between them must exist if the decomposition uses both nodes.

---

# 7. Counterexample D — modification bypasses selection

Suppose evidence has two effects:

\[
E\rightarrow C
\]

and independently

\[
E\rightarrow M.
\]

The first gives positive G1.

The second causes modification directly.

If the selected candidate is merely correlated with the modification because both respond to evidence, then observing

\[
C\approx M
\]

does not establish

\[
C\rightarrow M.
\]

The causal structure may be:

\[
E\rightarrow C,
\qquad
E\rightarrow M,
\]

rather than

\[
E\rightarrow C\rightarrow M.
\]

Therefore conditioning on selected candidates or observing selected/deployed agreement is insufficient to identify the bridge.

This is the same attribution discipline already imposed elsewhere in CCA:

\[
\boxed{
\text{association between selected and deployed modifications}
\neq
\text{causal control of deployment by selection}.
}
\]

---

# 8. Counterexample E — hidden adoption variable

A more realistic structure is:

\[
E\rightarrow C\rightarrow D\rightarrow M.
\]

But \(D\) may also depend on evidence, resources, safety rules, or state:

\[
E\rightarrow D,
\qquad
R\rightarrow D,
\qquad
X\rightarrow D.
\]

Then the question

> Does selection cause modification?

is underspecified.

There may be a legitimate adoption mechanism that conditions selected candidates before deployment.

The correct bridge object may concern whether **selected candidate identity has warranted causal authority within the adoption process**, not whether deployment copies selection deterministically.

Thus exact one-to-one selection/deployment identity is too strong as a universal bridge requirement.

---

# 9. Counterexample F — candidate selection and modification are physically inseparable

Some architectures may not contain a separable adoption stage.

For example, the act of selecting a continuous control update may itself instantiate the update.

Then:

\[
C\equiv M
\]

operationally.

In that architecture the current selection/adoption/modification decomposition may be inappropriate.

This does **not** invalidate CCA.

It limits the scope of the current empirical pathway.

Therefore:

\[
\boxed{
\text{a separable bridge is a property of the chosen decomposition, not a universal theorem of adaptation.}
}
\]

This mirrors the scoped role already adopted for candidate-selection G1.

---

# 10. What would a bridge assay need to identify?

If the current pathway retains separable \(C\) and \(M\), then a bridge assay must establish more than correlation.

A candidate bridge question is:

> **Does intervention on the selected adaptive decision causally control which modification is assigned, under a prospectively fixed adoption / translation regime?**

Schematically:

\[
\boxed{
do(C=c)\rightarrow M}
\]

or, if adoption is explicit:

\[
\boxed{
do(C=c)\rightarrow D\rightarrow M}.
\]

This is not frozen as a new named gate here.

It is a candidate identification structure to attack.

---

# 11. A bridge response matrix

As with G1, raw agreement can be misleading.

Suppose candidate identities are

\[
\mathcal C=\{c_1,\ldots,c_K\}
\]

and intended modification identities are

\[
\mathcal M=\{m_1,\ldots,m_K\}
\]

under a prospective mapping

\[
\phi(c_i)=m_i.
\]

A bridge response matrix could be represented as:

\[
B_{ij}
=
P(M=m_j\mid do(C=c_i),\mathcal D),
\]

where \(\mathcal D\) denotes the prospectively fixed adoption/translation regime.

The warrant mapping for the bridge is then not an evidence oracle but an implementation mapping:

\[
\phi:C\rightarrow M.
\]

The desired property is movement toward the mapped modification when candidate identity is intervened upon.

No scalar estimand, threshold, weighting rule, or intervention protocol is frozen here.

---

# 12. Why `do(C=c)` may be necessary

If the bridge is estimated only from naturally selected candidates, then evidence, internal state, and candidate identity can remain entangled.

Observed data of the form

\[
P(M\mid C,E)
\]

may not identify the effect of selection on modification.

A direct bridge intervention would conceptually break the upstream dependence:

\[
do(C=c).
\]

This mirrors the logic behind G2's hard requirement:

\[
do(M=m).
\]

The two interventions answer different questions:

```text
do(C=c)  -> does candidate identity causally control deployment?
do(M=m)  -> does the modification causally produce target/protected outcomes?
```

The bridge cannot borrow causal authority from G2.

---

# 13. But `do(C=c)` is not automatically coherent

Intervening on candidate identity may itself create a malformed state if the adoption process expects provenance, evidence, confidence, or other metadata coupled to selection.

For example, an adoption system may legitimately require:

\[
D=f(C,E,Q,X).
\]

If `do(C=c)` creates candidate/evidence combinations that could never arise under the declared pathway, the bridge assay may test an artificial regime.

Therefore a bridge intervention needs its own prospective consistency conditions.

Possible objects include:

1. **candidate-only intervention** — set candidate identity while leaving evidence fixed;
2. **candidate-package intervention** — set candidate plus prospectively defined metadata;
3. **adoption-decision intervention** — intervene directly on adoption;
4. **translation intervention** — intervene on the candidate-to-modification mapping.

This analysis does not select among them.

It establishes that the bridge's intervention semantics must be defined independently rather than inherited automatically from G1 or G2.

---

# 14. Positive component assays still do not establish mediation

Even if all three relations are individually demonstrated:

\[
E\rightarrow C,
\]

\[
C\rightarrow M,
\]

and

\[
M\rightarrow Y,
\]

one must still be careful about claiming that the end-to-end effect of evidence on outcome is mediated through exactly this chain.

Path-specific mediation claims can require additional assumptions about interactions, cross-world counterfactuals, or separability.

CCA does not need to earn such a strong claim merely to establish modular causal competencies.

Therefore the program should distinguish:

```text
component causal gates
bridge causal gate
end-to-end evidence-attributed outcome effect
path-specific mediation claim
```

These are not interchangeable authority levels.

---

# 15. Three levels of bridge authority

A useful provisional distinction is:

## 15.1 Mapping validity

Is there a prospectively defined semantic / operational mapping

\[
\phi:C\rightarrow M
\]

such that each candidate has a reconstructible intended modification identity?

Without this, candidate-to-modification fidelity is undefined.

## 15.2 Bridge causal control

Does assigned candidate identity causally influence deployed modification identity under the frozen adoption regime?

Schematically:

\[
do(C=c)\rightarrow M.
\]

Without this, G1 and G2 remain disconnected component assays.

## 15.3 End-to-end composition

Does evidence assignment, through the actual selection/adoption/deployment pathway, produce the warranted effective modification?

Schematically:

\[
E\rightarrow C\rightarrow D\rightarrow M\rightarrow Y.
\]

This is stronger than either component gate.

The present analysis does not freeze these as named maturity levels.

---

# 16. Requested three-state asymmetry

The user-proposed cases have different meanings.

## Case 1

\[
G_1>0,\qquad G_2=0.
\]

Interpretation:

The system/pathway can allocate warranted adaptive decision authority from evidence, but the tested modification family lacks demonstrated causal efficacy/isolation.

This is an epistemic/selection capability without established implementation competence.

It does not authorize modification repair under the same object.

## Case 2

\[
G_1=0,\qquad G_2>0.
\]

Interpretation within the current decomposition:

The tested modifications can work when directly imposed, but evidence does not demonstrably govern the separable selection decision.

This fails the current CCA evidence-controlled pathway.

It does **not** prove the system lacks all possible correction architectures.

A different prospective pathway could exist, for example direct evidence-to-modification control, but it would be a different scientific object.

## Case 3

\[
G_1>0,\qquad G_2>0.
\]

Interpretation:

Two component competencies exist.

Nothing follows about their composition until the bridge is identified.

Thus:

\[
\boxed{
(G_1>0,G_2>0)
\text{ is necessary for the current two-endpoint architecture, but not sufficient for a connected correction pathway.}
}
\]

Even the word “necessary” is scoped to the chosen decomposition, not universal CCA.

---

# 17. A bridge can fail even with perfect selection fidelity

Suppose:

\[
P(C=C^*(E)\mid do(E))=1.
\]

This is idealized selection fidelity.

But if:

\[
P(M=\phi(C)\mid do(C))=0,
\]

then no selected candidate reaches its intended modification.

The end-to-end system has perfect epistemic selection and zero implementation linkage.

Therefore:

\[
\boxed{
\text{selection fidelity is not deployment fidelity.}
}
\]

---

# 18. A bridge can be deterministic and still scientifically wrong

Suppose the deployment system deterministically maps every selected candidate to a modification:

\[
P(M=\tilde\phi(C)\mid do(C))=1.
\]

But \(\tilde\phi\neq\phi\).

Then bridge causal control is strong, but bridge **warrant fidelity** is wrong.

So the bridge needs the same general discipline already learned for G1:

\[
\boxed{
\text{causal responsiveness}\neq\text{warranted causal responsiveness}.
}
\]

For the bridge, the warrant-like object is the prospectively justified candidate-to-modification mapping.

---

# 19. Adoption may legitimately reject a selected candidate

A high-quality adaptive system may select a candidate and then reject deployment because a downstream safety, resource, consistency, or protected-structure gate fails.

Therefore a bridge cannot necessarily be defined as:

\[
C=c_i\Rightarrow M=m_i.
\]

A legitimate adoption policy might instead implement:

\[
(C,Z)\rightarrow D\in\{\mathrm{accept},\mathrm{reject}\}
\]

where \(Z\) is prospectively authorized adoption evidence.

Then a correct bridge claim may need to distinguish:

- whether candidate identity causally enters adoption;
- whether the adoption decision is itself warranted;
- whether accepted candidates map faithfully to modification identity;
- whether rejection produces a no-op rather than an uncontrolled alternative modification.

This suggests that `adoption` is not merely plumbing.

It may be a distinct scientific object if the current CCA pathway includes it.

The present analysis does not freeze such an object.

---

# 20. The no-op has to be represented explicitly

A deployment mechanism that rejects a candidate often induces:

\[
M=\varnothing.
\]

If no-op is omitted from the modification state space, observed deployment fidelity can be distorted.

For bridge analysis, the modification space may need to include:

\[
\mathcal M^+=\mathcal M\cup\{\varnothing\}.
\]

This allows the analysis to distinguish:

```text
selected candidate -> intended modification
selected candidate -> wrong modification
selected candidate -> no-op
```

These are scientifically different bridge outcomes.

Again, this is conceptual structure only, not a frozen contract.

---

# 21. Why the bridge cannot be inferred from deployment logs

Suppose observed logs show:

\[
C=c_i,\qquad M=m_i
\]

for nearly every case.

This can still arise because both are driven by a common upstream variable:

\[
U\rightarrow C,
\qquad
U\rightarrow M.
\]

Without an intervention that changes candidate identity independently of the common causes, the bridge remains causally ambiguous.

Thus:

\[
\boxed{
\text{observed candidate/modification agreement}\neq\text{identified candidate-to-modification control}.
}
\]

This is the bridge analogue of the outcome/mechanism separation established earlier for G1.

---

# 22. Bridge identification must not condition on successful modification

A particularly dangerous analysis would estimate the bridge only among cases where modification succeeded or passed a downstream gate.

That creates post-selection:

\[
C\rightarrow M\rightarrow\text{success}
\]

and then conditions on success.

The resulting selected subset can destroy the intended policy-level interpretation.

Therefore the bridge, like earlier CCA gates, should be analyzed at the assignment/policy level rather than only among successful deployments.

No exact estimand is frozen here.

---

# 23. G2 must remain downstream-independent

Nothing in bridge analysis modifies the hard G2 rule:

\[
\boxed{
G_2\text{ is identified only by direct }do(M=m).
}
\]

Even if candidate-to-modification control is perfect, modification efficacy and protected interference still require independent direct assignment.

Thus:

\[
\boxed{
\text{bridge success}\not\Rightarrow G_2.
}
\]

Likewise:

\[
\boxed{
G_2\not\Rightarrow\text{bridge success}.
}
\]

The two gates identify different relations.

---

# 24. Candidate causal graph surviving the attack

The strongest candidate variable-level structure is now:

```text
E   admissible evidence regime
│
▼
C   separable adaptive decision / selected candidate
│
▼
D   adoption / deployment process
│
▼
M   concrete modification
│
├──────────────► Y_T  target effect
└──────────────► Y_P  protected effect
```

with separate causal questions:

```text
G1       do(E) -> C
BRIDGE   do(C) -> D -> M       [candidate object only; not yet named/frozen]
G2       do(M) -> (Y_T,Y_P)
```

and later:

```text
JOINT    does the actual E -> C -> D -> M pathway
         produce warranted effective isolated change?
```

This decomposition is **not canonicalized** by this attack.

---

# 25. Does the bridge need its own gate?

The attack strongly suggests yes **for the current separable candidate-selection architecture**.

Why?

Because there are worlds in which:

\[
G_1>0,
\qquad
G_2>0,
\]

but

\[
C\not\rightarrow M.
\]

Therefore no conjunction of G1 and G2 alone identifies end-to-end evidence-controlled modification.

A bridge object is needed if C and M are genuinely separate variables.

However the attack does **not** establish:

- what that gate should be called;
- whether adoption and translation are one gate or multiple gates;
- whether direct \(do(C=c)\) is the final identification strategy;
- whether every CCA architecture needs this gate;
- what estimator or criterion it should use.

The earned statement is only:

\[
\boxed{
\text{separable }C\text{ and }M
\Rightarrow
\text{their causal linkage requires separate identification.}
}
\]

---

# 26. The bridge is not “does selection cause modification?” in the abstract

That wording is too weak because a selected candidate could causally influence some modification while still mapping to the wrong one.

The stronger candidate question is:

> **Does intervention on a prospectively defined adaptive decision causally control deployment toward the modification that operationally instantiates that decision under the frozen adoption/translation regime?**

This includes both:

1. causal influence;
2. identity/warrant fidelity.

That is structurally analogous to G1, where evidence must move the decision in the independently warranted direction rather than merely perturb it.

---

# 27. Relation to authority

CCA's deeper language is authority allocation.

At G1:

\[
E\rightarrow C
\]

asks whether evidence acquires warranted causal authority over a separable adaptive decision.

At the bridge:

\[
C\rightarrow M
\]

asks whether that warranted adaptive decision acquires legitimate causal authority over what is actually instantiated.

At G2:

\[
do(M=m)\rightarrow Y
\]

asks whether the instantiated modification has the intended causal consequences while preserving protected structure.

This yields a candidate authority chain:

\[
\boxed{
\text{evidence authority}
\rightarrow
\text{decision authority}
\rightarrow
\text{deployment authority}
\rightarrow
\text{causal modification efficacy}
}
\]

The present attack establishes only that the middle authority transfer cannot be assumed.

---

# 28. Relation to CCA's non-compensatory ladder

A bridge gate would preserve the program's asymmetry:

```text
G1 success cannot compensate for bridge failure.
Bridge success cannot compensate for G2 failure.
G2 success cannot compensate for G1 failure.
```

Large target efficacy should not rescue evidence-insensitive selection.

Perfect warranted selection should not rescue zero deployment throughput.

Perfect deployment fidelity should not rescue harmful or ineffective modification.

This makes the decomposition diagnostically useful.

---

# 29. Relation to repeated correction

Even if G1, bridge linkage, and G2 all succeed once, repeated correction remains unestablished.

A system may lose:

- evidence sensitivity after modification;
- adoption capacity;
- candidate-to-modification mapping validity;
- protected structure;
- future access to the same interface;
- ability to reverse or revise prior changes.

Therefore:

\[
\boxed{
G_1+\text{bridge}+G_2
\not\Rightarrow
\text{repeated correction}.
}
\]

The later dynamic gate remains scientifically necessary.

---

# 30. Relation to alternative CCA pathways

The current pathway is not claimed to be universal.

Alternative architectures could include:

```text
E -> M directly
E -> constraint set -> M
E -> policy parameter update
E -> continuous controller state
external authority -> M
```

If an alternative pathway omits separable candidate selection, then the current G1/bridge decomposition may not apply.

That does not authorize retroactively redefining G1.

It means the alternative pathway would require a new prospective decomposition under the same CCA program.

This preserves:

\[
\boxed{
\text{program unity}\neq\text{architectural uniformity}.
}
\]

---

# 31. Refuted propositions

The attack refutes the following general claims.

## R1

\[
G_1>0\land G_2>0
\Rightarrow
\text{connected evidence-to-modification pathway}.
\]

False.

## R2

Observed candidate/deployment agreement identifies the causal bridge.

False.

## R3

Selection and adoption can be treated as the same event by default.

False for separable architectures.

## R4

Selection and modification identity are automatically the same.

False unless the architecture is explicitly constituted that way.

## R5

A deterministic bridge is necessarily a correct bridge.

False; it can deterministically map to the wrong modification.

## R6

Direct G2 intervention identifies the candidate-to-modification bridge.

False.

## R7

Bridge success establishes repeated correction.

False.

## R8

Every CCA architecture must contain an explicit bridge from candidate selection to modification.

Not established; alternative architectures remain admissible.

---

# 32. Surviving candidate distinctions

The attack supports the following distinctions for the **current separable empirical pathway**:

\[
\boxed{
\text{selection}
\neq
\text{adoption/deployment}
\neq
\text{modification}
\neq
\text{modification outcome}.
}
\]

And therefore:

\[
\boxed{
G_1
\neq
\text{bridge identification}
\neq
G_2.
}
\]

The bridge, if adopted, must itself have:

- a prospectively defined candidate-to-modification mapping;
- a prospectively defined adoption/translation regime;
- an intervention or identification strategy that can separate candidate causal authority from common upstream causes;
- explicit representation of rejection/no-op where relevant;
- no conditioning on successful downstream modification;
- no substitution for direct G2 assignment.

---

# 33. Strongest result of the attack

The proposed design boundary was written informally as:

\[
G_1\stackrel{?}{\longrightarrow}G_2.
\]

The attack replaces that shorthand with a more precise statement:

\[
\boxed{
G_1\text{ and }G_2\text{ are component properties; their composition requires a separately identified object-level bridge.}
}
\]

For the current candidate-selection decomposition, the missing causal relation is approximately:

\[
\boxed{
C_{\mathrm{selected}}
\rightarrow
D_{\mathrm{adopt}}
\rightarrow
M
}
\]

with direct G2 identification still downstream:

\[
\boxed{
do(M=m)\rightarrow(Y_T,Y_P).}
\]

The bridge is not yet a canonical gate, and no specific intervention has been frozen.

---

# 34. What the attack does not authorize

This analysis does not authorize:

- naming or freezing a bridge gate;
- choosing whether adoption and translation are separate scientific objects;
- freezing \(do(C=c)\) as the bridge intervention;
- choosing a candidate ontology;
- choosing a modification language;
- choosing an evidence set;
- choosing a model or prompt;
- building ECIM;
- selecting thresholds or estimators;
- running G1;
- running a bridge assay;
- running G2;
- changing the canonical research state.

---

# 35. Next decision boundary

If this attack survives review, the next scientific-object question is:

> **Should the current CCA pathway explicitly introduce a separate bridge/adoption gate between G1 and G2, and if so, what causal claim must that gate make?**

The strongest candidate claim is not merely:

> selected candidates correlate with deployed modifications.

It is closer to:

> **Under a prospectively defined adoption/translation regime, intervention on the separable adaptive decision causally controls deployment toward the modification that operationally instantiates that decision.**

That claim remains provisional and uncanonicalized.

No implementation follows from this document.
