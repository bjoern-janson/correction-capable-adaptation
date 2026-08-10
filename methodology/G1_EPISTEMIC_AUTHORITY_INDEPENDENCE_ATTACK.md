# Attack: Epistemic-Authority Independence Against G1

## Status

**ADVERSARIAL METHODOLOGICAL ANALYSIS — NO CANONICAL PRINCIPLE — NO G1 STATE CHANGE — NO METRIC — NO IMPLEMENTATION — NO EXECUTION**

This document attacks a candidate meta-principle exposed by the Justified Transformability work:

\[
\boxed{
\text{authority independence}
\neq
\text{statistical independence}
}
\]

and, more strongly, the proposed asymmetry:

\[
\boxed{
\text{downstream evidence may challenge upstream authority}
}
\]

but

\[
\boxed{
\text{downstream success may not retroactively manufacture upstream authority}.
}
\]

The purpose of this PR is to test whether that principle survives outside JT against the substantially more mature G1 measurement constitution.

It does **not**:

- alter the canonical G1 role;
- alter the CCA Causal Composition Principle;
- change `research_state.json`;
- canonize an epistemic-authority-independence law;
- freeze any G1 ontology, evidence set, interface, realization policy, estimand, threshold, model, benchmark, or protocol;
- authorize implementation or execution.

---

# 1. Canonical G1 starting point

CCA currently fixes only the scientific role:

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

The mature G1 analysis already distinguishes:

```text
0A-S  semantic evidence constitution
0A-I  interface contract
0A-R  realization policy
0B    total causal warranted-evidence control
0B-R  realization/access heterogeneity
0C    mechanism/channel attribution
```

and already rejects the substitutions:

```text
codebook construction          != G1
relational sensitivity         != G1
representation invariance      != G1
access robustness              != G1
candidate accuracy             != G1
mechanism/channel attribution  != G1
```

The question here is not whether those distinctions are correct.

The question is whether they instantiate a more general rule governing **how constitutive authority may flow through a scientific object**.

---

# 2. Candidate principle under attack

A strong version would say:

> **Every constitutive object must receive its authority independently of the empirical outcome it constrains.**

For an object \(X\) and tested outcome \(Y\), this might be read as:

\[
Y\not\rightarrow X.
\]

That formulation is appealing but potentially too strong.

Scientific measurement objects are often empirically discovered, calibrated, refined, or adaptively constituted.

The attack therefore asks:

1. Does G1 already obey the strong rule?
2. Are there legitimate G1 constructions in which empirical data influence upstream constitution?
3. If so, what narrower anti-circularity rule actually survives?
4. What distinguishes legitimate revision from retroactive rescue?

---

# 3. G1 authority map

A prospective G1 claim can be schematized as:

\[
\text{scientific question}
\rightarrow
\text{evidence constitution}
\rightarrow
\text{warrant relation}
\rightarrow
\text{interface / realization regime}
\rightarrow
\text{causal assignment}
\rightarrow
\text{adaptive decision}
\rightarrow
\text{estimand / decision rule}.
\]

The layers may legitimately depend on one another.

For example:

- a realization policy may depend on the semantic evidence state;
- an interface contract may depend on the declared system class;
- a warranted candidate may depend on the evidence condition;
- a causal estimand may aggregate candidate-specific effects using a prospectively specified target distribution.

Thus the principle cannot mean ordinary independence.

The issue is **where the authority to define each layer comes from**.

---

# 4. Attack A — outcome-defined evidence semantics

Suppose a researcher begins with raw stimuli \(Z\), tests a system, observes which stimuli produce the desired candidate selections, and only then partitions the stimuli into semantic evidence states:

\[
Z
\xrightarrow{\text{tested behavior}}
E_{\mathrm{posthoc}}.
\]

The new evidence labels are chosen so that the observed behavior appears evidence-sensitive.

Then the same behavioral outcome both:

1. defines the treatment identity; and
2. serves as evidence that the treatment caused the desired decision.

This is a self-authorizing loop.

\[
\boxed{
\text{tested G1 behavior}
\rightarrow
\text{evidence-state definition}
\rightarrow
\text{claim of G1 behavior}
}
\]

is invalid as confirmatory evidence under one unchanged object identity.

### Result

G1 strongly supports the anti-rescue intuition:

\[
\boxed{
\text{observed decision response}
\not\Rightarrow
\text{retrospective constitution of the evidence treatment used to credit that response}.
}
\]

But this does not yet establish that empirical observations can never help constitute future evidence states.

---

# 5. Attack B — outcome-defined warrant

Let \(C^*(e)\) denote the independently warranted decision under evidence condition \(e\).

Suppose instead that the researcher observes the selected candidate first and then defines:

\[
C^*(e)=C_{\mathrm{selected}}(e).
\]

Then every stable selector becomes perfectly warranted by construction.

This collapses:

\[
\text{causal responsiveness}
\]

into:

\[
\text{warranted causal responsiveness}.
\]

The loop is:

\[
C_{\mathrm{selected}}
\rightarrow
C^*
\rightarrow
\text{credit for selecting }C^*.
\]

### Result

G1 already contains a strong version of epistemic-authority separation:

\[
\boxed{
\text{the tested system's decision cannot define the warrant used to evaluate that decision}.
}
\]

The warrant source may depend on evidence and domain semantics, but its **evaluative authority** cannot be borrowed from the tested decision itself.

---

# 6. Attack C — behavior-relative interface and realization rescue

The G1 attacks established that prospective does not mean system-blind.

An interface contract may legitimately be designed for a declared system class.

A realization policy may legitimately condition on semantic evidence state:

\[
R\sim Q_R(\cdot\mid s,K).
\]

So consider two superficially similar procedures.

## Procedure C1 — legitimate prospective system-aware design

Before the confirmatory outcome is observed, the researcher specifies:

- the system class;
- interface requirements;
- admissible realization families;
- a sampling policy over those realizations;
- invalidity criteria.

The resulting treatment regime may be highly system-aware.

This does not violate authority independence merely because the interface was designed using scientific knowledge about the system class.

## Procedure C2 — retrospective competence filtering

The researcher tests many realizations, observes which ones the tested system handles well, discards the difficult ones, and calls the surviving subset the admissible interface:

\[
R
\xrightarrow{\text{observed competence}}
R_{\mathrm{admissible}}.
\]

The realized behavior now defines the envelope under which the same behavior is evaluated.

This is an authority leak.

### Result

The attack refutes a simplistic equation:

\[
\boxed{
\text{authority independence}
\neq
\text{system blindness}.
}
\]

What matters is not whether constitution uses system-relevant knowledge.

What matters is whether **the outcome-bearing evidence under evaluation is allowed to select the conditions under which it counts**.

---

# 7. Attack D — treatment repair after the outcome

Suppose a frozen semantic-assignment regime is:

\[
G_s:
S\leftarrow s,
\qquad
R\sim Q_R(\cdot\mid s,K),
\qquad
E_{\mathrm{raw}}=h(s,R;K).
\]

The experiment is run and the primary result is negative.

Post-outcome diagnosis reveals that one component of \(Q_R\) made access difficult.

Three different reactions are possible.

## D1 — prospective descendant

Record the original result unchanged.

Use the diagnosis to define a new realization policy \(Q'_R\), create a new prospective object/version, freeze it, and test it later.

This is legitimate correction.

## D2 — prospective narrowing

Record that the original broad claim failed or was invalid over its original scope.

Define a narrower future claim with a new prospective scope and new identity.

This is legitimate scope correction.

## D3 — retroactive rescue

Replace \(Q_R\) with \(Q'_R\) after observing the outcome, then reinterpret the already observed responses as though they had been generated under the repaired object.

This is not revision of the original scientific object.

It is replacement of the object while attempting to retain the original evidential identity.

### Result

G1 strongly supports:

\[
\boxed{
\text{revision}
\neq
\text{retroactive rescue}.
}
\]

But the exact identity rule needs care: not every post-outcome edit creates a new scientific object.

Purely documentary or provenance-preserving corrections that do not change treatment identity, estimand, decision boundary, or interpretation can remain within the same object.

---

# 8. Attack E — post-hoc estimand selection

Suppose the causal response matrix is:

\[
M_{ij}
=
P(C_{\mathrm{selected}}=c_j\mid do(G_{s_i})).
\]

A candidate-specific lift might eventually take a form such as:

\[
\Delta_i
=
M_{ii}
-
\sum_{\ell\neq i}\omega_{i\ell}M_{\ell i}.
\]

The weights \(\omega_{i\ell}\) are not currently frozen.

That is appropriate before a contract exists.

But after observing \(M\), choosing \(\omega\) specifically to maximize \(\Delta_i\), then presenting that quantity as the prospectively intended G1 estimand, would create another authority loop:

\[
M
\rightarrow
\omega_{\mathrm{posthoc}}
\rightarrow
\Delta(M,\omega_{\mathrm{posthoc}})
\rightarrow
\text{G1 claim}.
\]

### Result

The anti-rescue principle applies not only to ontology and treatment constitution but also to the **decision functional applied to the observed causal response**.

A post-outcome exploratory estimand may be scientifically useful.

It does not inherit confirmatory authority merely because it is computed from valid data.

---

# 9. Attack F — mechanism feedback into the parent object

G1 deliberately separates:

```text
0B  total warranted evidence control
0C  mechanism/channel attribution
```

Suppose a total G1 effect is weak or absent, but a mechanism analysis discovers a strong relational sensitivity in a subset of cases.

If the researcher then redefines G1 as “relational sensitivity” and treats the original experiment as positive evidence for the newly narrowed mechanism object, authority has leaked upward from a diagnostic descendant into the parent claim.

A legitimate path is:

```text
negative or weak parent result
→ mechanism diagnosis
→ new prospective mechanism object
→ separate future test
```

not:

```text
negative parent result
→ find surviving mechanism signal
→ rename parent object
→ count original test as success
```

### Result

The existing outcome/mechanism separation is already an instance of the candidate authority rule.

---

# 10. Counterexample to the strong principle — empirical calibration can be legitimate

The strong statement

\[
Y\not\rightarrow X
\]

is too crude.

Consider a separate calibration study \(D_{\mathrm{cal}}\) used to determine which textual realizations satisfy a prospective interface-access criterion.

The resulting admissible set is then frozen before the confirmatory G1 test \(D_{\mathrm{test}}\):

\[
D_{\mathrm{cal}}
\rightarrow
Q_R^{\mathrm{frozen}}
\rightarrow
D_{\mathrm{test}}.
\]

Empirical outcomes helped constitute the measurement object.

That is not circular if the confirmatory authority is carried by evidence not used to manufacture the tested criterion, or if the inferential procedure properly accounts for the construction step.

Therefore:

\[
\boxed{
\text{empirical influence on constitution}
\not\Rightarrow
\text{authority leak}.
}
\]

The relevant distinction is evidential role, not merely chronology.

---

# 11. Counterexample — prospectively licensed adaptive constitution

A second counterexample is even stronger.

Suppose before execution CCA freezes an update operator:

\[
X_{t+1}=U(X_t,D_t),
\]

where \(U\) specifies exactly how an interface, sampling allocation, or measurement representation may adapt to incoming data.

If the adaptation rule is prospectively part of the contract and the final inference accounts for the adaptive process, then downstream data can causally change an upstream measurement component without automatically creating retroactive rescue.

The authority for the change comes from the pre-authorized update rule, not from post-hoc preference for the observed outcome.

Thus:

\[
\boxed{
\text{data-dependent revision}
\not\Rightarrow
\text{retroactive rescue}.
}
\]

This refutes any meta-principle that requires all constitutive objects to remain literally static after data collection begins.

---

# 12. Counterexample — same data can have multiple roles if authority is accounted for

A categorical rule that the same dataset may never participate in both construction and evaluation would also be too strong.

Legitimate procedures can include:

- sample splitting;
- cross-fitting;
- selective-inference corrections;
- nested validation;
- prospectively specified sequential adaptation;
- other procedures that explicitly account for data-dependent construction.

The scientific issue is not physical reuse of bytes.

It is whether the claimed uncertainty, error control, and evidential authority correctly account for the fact that the object or decision rule was data-dependent.

Therefore:

\[
\boxed{
\text{data reuse}
\neq
\text{authority reuse without accounting}.
}
\]

CCA should not replace ordinary inferential discipline with a blanket no-reuse rule.

---

# 13. Strongest surviving rule — no evidential self-authorization

The attack therefore rejects the strongest static formulation of authority independence.

The better surviving candidate is:

> **Evidence may revise or help constitute a scientific object, but the evidence carrying a claim's confirmatory authority may not retroactively define or alter the constitutive conditions under which that same evidential claim counts as success, unless the data-dependent update and its inferential consequences were prospectively authorized and accounted for.**

Compactly:

\[
\boxed{
\text{no evidential self-authorization within one unchanged claim identity}.
}
\]

This is narrower than:

\[
\text{outcomes never influence constitution}.
\]

It allows:

```text
outcome
→ criticism
→ new prospective object
```

and, when prospectively licensed:

```text
data
→ frozen update operator U
→ updated object/version
→ inference accounting for U
```

while forbidding:

```text
outcome
→ redefine tested object
→ reinterpret same outcome
→ call original claim successful
```

---

# 14. Object identity and versioning

The attack suggests that authority independence requires an explicit identity rule.

Let \(X^{(0)}\) be the object under which outcome \(Y^{(0)}\) was generated.

If contradiction causes a scientifically substantive revision:

\[
X^{(0)}\rightarrow X^{(1)},
\]

then the original claim remains attached to \(X^{(0)}\).

The new object \(X^{(1)}\) may be motivated by \(Y^{(0)}\), but \(Y^{(0)}\) does not automatically become confirmatory evidence for \(X^{(1)}\).

This preserves:

\[
\boxed{
\text{revision provenance}
\neq
\text{evidential inheritance}.
}
\]

However, the following need not force new scientific identity if they are genuinely interpretation-invariant:

- typo correction;
- broken link repair;
- clearer prose;
- provenance metadata repair;
- implementation repair that occurred before any outcome-bearing instantiation and does not alter the frozen scientific object.

The identity boundary should therefore track **scientifically consequential change**, not file edits.

---

# 15. G1-specific unit tests for authority leakage

A future G1 contract could be attacked with the following questions.

## 15.1 Semantic constitution

> Could the observed candidate responses be used to redraw the evidence-state partition and then make those same responses look warranted?

If yes: leak.

## 15.2 Warrant

> Could the selected candidates or downstream performance be used to redefine which candidate was independently warranted?

If yes: leak.

## 15.3 Interface

> Could tested-system competence be used after observation to redefine which interface conditions count as admissible?

If yes: leak unless a prospective adaptive rule and valid inference authorize it.

## 15.4 Realization policy

> Could realized representation sensitivity be used to discard difficult realizations and then treat the surviving subset as the original treatment envelope?

If yes: leak.

## 15.5 Treatment identity

> Could observed effects be used to repackage the treatment regime so that the successful causal contrast becomes the intended evidence contrast after the fact?

If yes: leak.

## 15.6 Estimand

> Could outcome-dependent weights, subsets, thresholds, or contrast choices replace the prospective estimand while retaining its confirmatory status?

If yes: leak.

## 15.7 Failure diagnosis

> Could a post-outcome mechanism signal be promoted to the parent G1 object and thereby convert a negative parent result into a positive one?

If yes: leak.

---

# 16. Revision test

The candidate four-part methodological requirement from PR #14 can now be sharpened for G1.

For every scientifically constitutive component \(X\), require some prospective account of:

```text
AUTHORITY SOURCE
Why is X licensed to define or constrain the claim?

BOUNDARY
Over what systems, evidence states, interfaces, realizations, and time does X apply?

DISCONFIRMATION
What observation would show X is invalid, insufficient, or out of scope?

REVISION RULE
What changes after contradiction, and what happens to the identity and evidential status of the original object?
```

The fourth item is not simply “X may be revised.”

It must distinguish:

```text
contradiction
→ prospective descendant
→ legitimate correction
```

from:

```text
contradiction
→ post-hoc redefinition
→ same outcome relabeled as success
```

---

# 17. Reopenability without slipperiness

The attack supports a useful methodological target:

\[
\boxed{
\text{scientifically reopenable}
\neq
\text{scientifically slippery}.
}
\]

A scientific object is reopenable when contradiction can legitimately reduce its authority, motivate revision, narrow scope, or generate a descendant.

It becomes slippery when every contradiction is absorbable by changing the object while preserving the evidential status of the original test.

Thus:

\[
\boxed{
\text{corrigibility}
\neq
\text{unbounded redefinability}.
}
\]

G1's existing governance appears substantially aligned with this distinction.

---

# 18. Relation to the CCA Causal Composition Principle

The candidate epistemic rule is related to, but distinct from, the existing CCA Causal Composition Principle.

The composition principle says:

> validated endpoint relations do not authorize an unvalidated separable causal transformation between them.

The present candidate says, approximately:

> a tested outcome does not authorize retrospective reconstruction of the constitutive premises under which that same outcome receives scientific meaning.

One governs **authority across causal edges**.

The other would govern **authority across epistemic/constitutive layers**.

They should not be collapsed without further attack.

---

# 19. Main adversarial result

The G1 attack produces a mixed result.

## The naïve principle is too strong

The following is refuted:

\[
\boxed{
\text{empirical outcomes may never influence upstream scientific constitution}.
}
\]

Legitimate calibration, prospectively licensed adaptive rules, discovery/confirmation separation, and inference that accounts for data-dependent construction are counterexamples.

## The anti-self-authorization principle survives

The following survives substantially better:

\[
\boxed{
\text{the evidence that carries a claim's authority may not retroactively manufacture the conditions under which that same evidence counts as success}.
}
\]

with an explicit exception for data-dependent transformations that were **prospectively authorized and inferentially accounted for**.

## G1 independently supports the pattern

The mature G1 decomposition already instantiates this discipline across:

- semantic evidence constitution;
- independent warrant;
- interface and realization scope;
- treatment identity;
- causal estimand;
- parent-versus-mechanism claims;
- failure and descendant-object handling.

Therefore the candidate principle is not merely an artifact of JT's unusual semantics.

But one G1 stress test is still not enough to canonize a universal CCA law.

---

# 20. Authority boundary

```text
EMPIRICAL AUTHORITY CHANGE                         NONE
G1 SCIENTIFIC ROLE                                 UNCHANGED
G1 MEASUREMENT CONTRACT                            UNFROZEN
JT SCIENTIFIC ROLE                                 UNCHANGED
EPISTEMIC-AUTHORITY-INDEPENDENCE PRINCIPLE         NOT CANONICAL
NO-EVIDENTIAL-SELF-AUTHORIZATION RULE              CANDIDATE ONLY
OBJECT VERSIONING RULE                             CANDIDATE ONLY
ADAPTIVE-CONSTITUTION RULE                         CANDIDATE ONLY
C_improve                                           NOT CANONICALIZED
RESEARCH STATE                                      UNCHANGED
IMPLEMENTATION / EXECUTION                          NOT AUTHORIZED
```

---

# 21. Next decision boundary

If this attack survives review, the next question is not yet “canonize authority independence.”

A stronger next attack would ask whether the surviving rule can be broken in a different CCA object where **the measured scientific object itself changes over time**, such as PMC or repeated correction, or in a deliberately adaptive measurement design.

The key candidate to carry forward is:

> **No evidential self-authorization within one unchanged claim identity: contradiction may revise or replace an object prospectively, and prospectively licensed data-dependent updates may be valid, but outcome-bearing evidence may not retroactively redefine the premises that give that same outcome confirmatory authority.**

No empirical work follows automatically from this attack.
