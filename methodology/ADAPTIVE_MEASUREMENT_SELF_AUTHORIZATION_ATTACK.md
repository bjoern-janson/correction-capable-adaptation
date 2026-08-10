# Attack: Adaptive Measurement and Evidential Self-Authorization

## Status

**ADVERSARIAL METHODOLOGICAL ANALYSIS — NO CANONICAL STATE TRANSITION — NO METRIC — NO IMPLEMENTATION — NO EXECUTION**

This document stress-tests the candidate methodological rule surviving PR #15:

> **No evidential self-authorization within one unchanged claim identity.**

The attack deliberately moves to a harder setting than static measurement.

The scientific system is allowed to update its measurement object, scope, representation, or inferential procedure over time using earlier observations from the same ongoing process.

The central question is:

> **Can CCA distinguish legitimate adaptive measurement from retroactive self-authorization when the measurement architecture itself evolves during an ongoing evidence stream?**

This attack does **not**:

- canonize an epistemic constitution law;
- freeze a universal object-versioning rule;
- require holdout data in every adaptive design;
- prohibit data-dependent scientific objects;
- define a G1, PMC, JT, or `C_improve` metric;
- change `research_state.json`;
- authorize implementation or execution.

---

# 1. Starting point from PR #15

PR #15 refuted the overly strong rule:

\[
\boxed{
\text{empirical outcomes may never influence upstream scientific constitution}
}
\]

because legitimate science can use:

- calibration data;
- discovery/confirmation splits;
- sample splitting;
- prospectively specified adaptive update rules;
- inferential procedures that explicitly account for data-dependent selection or construction.

The narrower candidate rule was:

\[
\boxed{
\text{No evidential self-authorization within one unchanged claim identity.}
}
\]

The present attack asks whether that rule survives when both the **system** and the **measurement architecture** evolve over time.

---

# 2. Time-indexed claim identity

A static symbol \(X\) is too crude for adaptive measurement.

Let the scientific claim at time \(t\) be represented schematically as:

\[
Q_t
=
(O_t, W_t, B_t, T_t, \psi_t, I_t),
\]

where, illustratively:

- \(O_t\): scientific object / ontology / distinction structure;
- \(W_t\): warrant semantics;
- \(B_t\): system / apparatus / scope boundary;
- \(T_t\): treatment or causal regime;
- \(\psi_t\): estimand / success proposition;
- \(I_t\): inferential procedure.

This tuple is not canonical CCA notation.

Its purpose is to make claim identity explicit enough to ask what changed.

Let the evidence history through time \(t\) be:

\[
H_t=(D_1,\ldots,D_t).
\]

An adaptive research program may update:

\[
Q_{t+1}=U_t(Q_t,H_t),
\]

for some update operator \(U_t\).

The existence of this dependence is not itself an authority leak.

The scientific problem is whether the evidence used to **construct** or **revise** \(Q\) is also allowed to carry confirmatory authority for a claim whose interpretation was changed because of that same evidence.

---

# 3. Attack A — the fresh-holdout rule is too strong

A tempting repair to self-authorization is:

> Every change to the scientific object requires completely fresh independent data.

That rule is safe in some settings but cannot be universal.

## 3.1 Sequentially valid inference

Suppose an inferential procedure is prospectively designed for an ongoing stream and remains valid under optional continuation, predictable adaptation, or another explicitly modeled sequential regime.

Then the same stream may legitimately contribute to both:

1. updating a state estimate or decision rule; and
2. accumulating evidence for a prospectively specified sequential claim.

The scientific authority can remain valid because adaptivity is part of the design rather than an unaccounted post-hoc intervention.

Therefore:

\[
\boxed{
\text{same data stream}
\not\Rightarrow
\text{self-authorization}.
}
\]

## 3.2 Selection-aware inference

A hypothesis, model component, or comparison may sometimes be data-dependent while the inferential procedure explicitly accounts for that dependence.

Thus:

\[
\boxed{
\text{data-dependent construction}
\not\Rightarrow
\text{invalid confirmation by definition}.
}
\]

The key issue is whether the inferential consequences of adaptation were prospectively licensed and correctly incorporated.

### Result of Attack A

A universal rule requiring disjoint discovery and confirmation samples is too strong.

The anti-self-authorization principle must be stated in terms of **claim identity and inferential authority**, not merely physical data reuse.

---

# 4. Attack B — predictability is sufficient but not necessary

A particularly clean adaptive design is:

\[
Q_t = f_t(H_{t-1}),
\]

followed by testing with new evidence \(D_t\).

In that case, the claim tested at time \(t\) is fixed relative to the incoming observation.

This resembles a predictable or prequential structure:

```text
past evidence
    ↓
construct Q_t
    ↓
new evidence D_t
    ↓
test Q_t
```

This structure strongly resists same-step self-authorization.

But it is not universally necessary.

A prospectively specified joint procedure might legitimately use \(D_t\) both to select a component and to form a corrected inference about that selected component.

Therefore:

\[
\boxed{
Q_t\text{ determined before }D_t
}
\]

is a strong sufficient condition for clean temporal authority separation, but not a universal constitutive law.

### Result of Attack B

The surviving principle cannot collapse into “all claims must be predictable one step in advance.”

It must permit prospectively governed adaptive inference.

---

# 5. Attack C — parameter learning is not necessarily object replacement

Suppose the scientific object and estimand are frozen but an unknown parameter is updated as evidence arrives:

\[
\theta_t\rightarrow\theta_{t+1}.
\]

That does not automatically imply:

\[
Q_t\neq Q_{t+1}.
\]

The scientific object may be unchanged while knowledge about it improves.

Examples in principle include:

- posterior or likelihood updating under a fixed model class;
- updated nuisance estimates;
- improved variance estimates;
- accumulated evidence about a fixed causal effect;
- calibration of a prospectively declared measurement model.

If every numerical update created a new scientific identity, the versioning rule would become unusably brittle.

Therefore:

\[
\boxed{
\text{updated estimate}
\neq
\text{new scientific object by default}.
}
\]

What threatens claim identity is a consequential change in the **interpretive contract**—for example treatment identity, warrant semantics, scientific distinction structure, estimand, success criterion, or inferential meaning.

### Result of Attack C

Object identity should track scientifically consequential changes to what the claim means, not every change in knowledge about a fixed object.

---

# 6. Attack D — evolving system state does not automatically imply goalpost movement

CCA studies adaptive systems, so the tested system itself may evolve:

\[
S_t\rightarrow S_{t+1}.
\]

A measurement object may need to be indexed to that changing state.

For example, a correction-path question at \(S_t\) may differ legitimately from the corresponding question at \(S_{t+1}\).

The fact that:

\[
Q(S_t)\neq Q(S_{t+1})
\]

need not imply retrospective rescue.

The scientific claim may simply be state-indexed.

The problem occurs when failure at \(S_t\) is reinterpreted using the later state-indexed object for \(S_{t+1}\) and then credited back to the earlier claim.

Therefore:

\[
\boxed{
\text{evolving object across evolving states}
\neq
\text{retroactive redefinition}
}
\]

provided the temporal/state indexing is explicit.

But:

\[
\boxed{
Q_{t+1}\text{ cannot retroactively authorize }Q_t.
}
\]

### Result of Attack D

Adaptive systems require **temporal claim indexing**. Otherwise legitimate state dependence and illegitimate goalpost movement become observationally confounded in the methodology.

---

# 7. Attack E — adaptive stopping can launder evidence without changing the object

Self-authorization does not require changing the scientific object.

Suppose \(Q\) is fixed, but the researcher repeatedly evaluates evidence and stops only when the desired threshold is crossed, while using an inferential method that assumes a fixed stopping rule.

Then the claim identity is unchanged, yet evidential authority can still be inflated.

Therefore:

\[
\boxed{
\text{unchanged claim identity}
\not\Rightarrow
\text{valid evidential authority}.
}
\]

This attacks an overly narrow reading of the candidate rule.

A complete anti-self-authorization principle must govern not only object revision but also **adaptation in evidence acquisition, stopping, selection, and analysis** when those adaptations affect inferential validity.

Conversely, if the stopping/adaptation rule is prospectively authorized and the inference remains valid under it, adaptive stopping need not be illegitimate.

### Result of Attack E

The principle must cover **evidential protocol identity**, not only scientific-object identity.

---

# 8. Attack F — adaptive success criteria are especially dangerous

Suppose the object and treatment remain fixed, but after observing results the success criterion changes:

\[
\psi^{(0)}\rightarrow\psi^{(1)}.
\]

Example structure:

```text
prospective claim: positive effect on outcome A
        ↓
A fails, B looks favorable
        ↓
new interpretation: success means A or B
        ↓
same evidence called positive
```

Even if the scientific phenomenon is unchanged, the **claim identity** has changed because the proposition receiving authority changed.

The correct structure is:

\[
D\text{ refutes or fails to establish }\psi^{(0)},
\]

then motivates a prospective \(\psi^{(1)}\) for future evidence.

It does not become confirmatory evidence that \(\psi^{(0)}\) succeeded.

Thus:

\[
\boxed{
\text{revision provenance}
\neq
\text{evidential inheritance}.
}
\]

### Result of Attack F

Claim identity must include the success proposition and inferential interpretation, not merely the named phenomenon.

---

# 9. Attack G — prospectively adaptive rules can still be too permissive

Suppose the protocol says in advance:

> After observing the data, redefine the scientific object however needed to maximize the reported evidence, and then report the best result.

This rule is technically prospective.

But prospectivity alone cannot rescue it.

The update operator \(U\) can itself encode self-authorization.

Therefore:

\[
\boxed{
\text{prospectively specified adaptation}
\not\Rightarrow
\text{scientifically legitimate adaptation}.
}
\]

A valid update rule must constrain the adaptive degrees of freedom strongly enough that the resulting evidential interpretation remains identified and falsifiable.

The rule cannot merely prospectively authorize arbitrary post-hoc optimization of the claim.

### Result of Attack G

“Prospective” is necessary in many cases but not sufficient.

The update operator itself becomes part of the scientific object/protocol and must have a valid inferential interpretation.

---

# 10. Attack H — same-data revision can be legitimate under a new claim, but authority must be reallocated

Suppose evidence \(D_t\) reveals that the current measurement object \(Q_t\) is malformed.

The program uses \(D_t\) to construct:

\[
Q_{t+1}=U(Q_t,D_t).
\]

This can be legitimate scientific progress.

What authority does \(D_t\) have afterward?

At minimum, \(D_t\) can serve as:

- provenance for why \(Q_t\) was revised;
- diagnostic evidence about the failure mode of \(Q_t\);
- discovery evidence motivating \(Q_{t+1}\).

But unless a prospectively valid inferential design explicitly licenses the reuse, \(D_t\) does not automatically become confirmatory evidence for \(Q_{t+1}\).

Therefore:

\[
\boxed{
\text{diagnostic authority}
\neq
\text{confirmatory authority}.
}
\]

This mirrors CCA's broader rule that validated consequence grants only the authority the evidence can identify.

### Result of Attack H

Evidence can legitimately change **role** after contradiction—diagnostic, discovery, calibration, confirmation—but those roles must not be conflated.

---

# 11. Attack I — rolling adaptation creates overlapping evidential ancestry

In an ongoing adaptive system, clean generations may not exist.

Suppose:

\[
Q_{t+1}=U(Q_t,D_t)
\]

and then:

\[
Q_{t+2}=U(Q_{t+1},D_{t+1}).
\]

After many rounds, current scientific objects inherit a long ancestry of evidence:

\[
D_1, D_2, \ldots, D_t.
\]

A simplistic rule requiring “independent evidence for every new version” may become impossible or wasteful.

The scientific requirement is instead to preserve **provenance and valid authority accounting** across the adaptive chain.

One must be able to answer:

1. Which evidence influenced construction of the current object?
2. Which evidence is being used to test it?
3. Which reuse was prospectively allowed?
4. What inferential correction accounts for that reuse?
5. Which claims remain open, failed, superseded, or untested?

### Result of Attack I

Adaptive CCA methodology may require an **authority ledger over evidence roles**, not merely binary labels of “used” versus “unused” data.

No such ledger schema is frozen here.

---

# 12. Attack J — a measurement object can track reality and still become unfalsifiable

Consider an adaptive measurement procedure that continually revises itself after every mismatch with the world.

That can look maximally corrigible.

But if every mismatch triggers a revision that is immediately treated as having explained the mismatch, the procedure can absorb every possible observation.

Then:

\[
\boxed{
\text{rapid revision}
\not\Rightarrow
\text{scientific corrigibility}.
}
\]

A scientifically corrigible adaptive measurement architecture must preserve some **pre-revision claim identity** long enough for contradiction to count as contradiction.

Otherwise:

\[
\text{prediction}\rightarrow\text{outcome}\rightarrow\text{instant redefinition}
\]

contains no stable object that can fail.

### Result of Attack J

Corrigibility requires both:

- revision capacity; and
- identity persistence sufficient for disconfirmation.

Compactly:

\[
\boxed{
\text{scientifically reopenable}
\neq
\text{scientifically slippery}.
}
\]

---

# 13. Combined adversarial cases

## Case 1 — legitimate predictable adaptation

```text
H_{t-1}
  ↓
prospectively defined update U
  ↓
Q_t
  ↓
new D_t
  ↓
valid test
```

No self-authorization is apparent.

## Case 2 — legitimate selection-aware same-data analysis

```text
D_t
  ↓
selection rule specified in advance
  ↓
selected object
  ↓
inference explicitly valid after selection
```

Same-data use is not automatically invalid.

## Case 3 — illegitimate adaptive rescue

```text
D_t
  ↓
failure of Q_t
  ↓
change warrant / estimand / threshold
  ↓
reinterpret same D_t
  ↓
claim Q_t succeeded
```

This is evidential self-authorization.

## Case 4 — legitimate new object with inherited provenance

```text
D_t contradicts Q_t
  ↓
Q_t remains failed / unresolved
  ↓
D_t motivates Q_{t+1}
  ↓
Q_{t+1} gets a new prospective authority path
```

This is correction rather than rescue.

## Case 5 — prospectively authorized but scientifically vacuous adaptation

```text
pre-register: "after observing data, choose whichever claim looks best"
  ↓
D_t
  ↓
optimize claim
  ↓
naive evidence report
```

Prospectivity alone does not establish validity.

## Case 6 — unchanged object, invalid adaptive inference

```text
fixed Q
  ↓
repeated peeking / stopping / selection
  ↓
fixed-sample inference reported as if no adaptation occurred
```

No object revision occurred, yet evidential authority is invalid.

---

# 14. What survives the attack

The attack refutes several simple formulations:

\[
\boxed{
\text{adaptive measurement requires fresh independent data at every step}
}
\]

is too strong.

\[
\boxed{
\text{same data used for construction and inference is always invalid}
}
\]

is too strong.

\[
\boxed{
\text{prospective adaptation is always valid}
}
\]

is too weak.

\[
\boxed{
\text{unchanged scientific object guarantees evidential validity}
}
\]

is false.

The strongest surviving candidate rule is approximately:

> **Evidence may govern prospective or prospectively accounted revision of future claims, including within an adaptive data stream, but the evidential procedure must not allow that evidence to retroactively manufacture the scientific or inferential conditions under which the already-tested claim is credited as success.**

A more structural formulation is:

\[
\boxed{
\text{No unaccounted evidential self-authorization across claim or protocol adaptation.}
}
\]

This is still a candidate, not a canonical CCA law.

---

# 15. Claim identity and protocol identity must both be tracked

PR #15 focused strongly on claim identity.

The adaptive attack shows that this is insufficient.

CCA may need to track at least two kinds of identity:

```text
CLAIM IDENTITY
What scientific proposition is being granted authority?

EVIDENTIAL-PROTOCOL IDENTITY
Under what acquisition, adaptation, selection, stopping, and inferential rules
is the evidence allowed to support that proposition?
```

A claim can remain fixed while protocol drift invalidates its evidence.

A protocol can remain fixed while the scientific claim changes.

Both can change together.

Therefore:

\[
\boxed{
\text{claim validity}
\neq
\text{protocol validity}
}
\]

and neither can substitute for the other.

---

# 16. Candidate temporal authority contract

A future CCA methodological contract for adaptive measurement may need to declare, prospectively or through a prospectively specified adaptive rule:

```text
1. current claim identity Q_t
2. evidence history allowed to influence Q_t
3. update operator U_t
4. which parts of U_t are scientifically constitutive versus parameter-estimating
5. evidence roles: diagnostic / discovery / calibration / confirmation
6. acquisition / stopping / selection rules
7. inference valid under those adaptive rules
8. object-version transition rules
9. which prior claims remain failed, open, superseded, or untested
10. what evidence may or may not carry forward as confirmatory authority
```

No schema or implementation is frozen by this attack.

---

# 17. Relation to CCA's contradiction discipline

The adaptive case sharpens the existing contradiction procedure.

A contradiction may justify:

\[
Q_t\rightarrow Q_{t+1}.
\]

But the transition must preserve the status of the earlier claim:

\[
\boxed{
\text{failure of }Q_t
\not\Rightarrow
\text{success of }Q_t\text{ under }Q_{t+1}.
}
\]

The revised object may be better.

That does not retroactively change what the earlier evidence established.

Thus:

\[
\boxed{
\text{revision provenance}
\neq
\text{evidential inheritance}.
}
\]

The methodology remains corrigible because \(Q_{t+1}\) may improve on \(Q_t\).

It remains falsifiable because \(Q_t\)'s evidential identity is not erased.

---

# 18. Relation to adaptive systems

This methodological attack mirrors the CCA research object without identifying them.

CCA asks whether adaptive systems can change while preserving conditions for future warranted correction.

An adaptive scientific program faces an analogous methodological question:

> Can the measurement architecture change while preserving the conditions under which its future evidential claims remain interpretable and falsifiable?

This analogy is structurally useful but does **not** establish a new empirical gate or a methodological PMC.

It suggests only that CCA must avoid demanding corrigibility from systems while permitting its own scientific objects to become unfalsifiably plastic.

---

# 19. Main result

The candidate principle survives adaptive measurement only after another refinement.

The scientifically relevant prohibition is not:

\[
\text{data must not influence future claims},
\]

nor:

\[
\text{the same data may never be reused}.
\]

It is closer to:

\[
\boxed{
\begin{gathered}
\text{Adaptive revision is legitimate when the update and evidential interpretation}\
\text{are prospectively governed or inferentially accounted for;}\\
\text{it is illegitimate when adaptation retroactively changes the scientific or inferential}\
\text{conditions under which an already observed result is credited as confirmatory success.}
\end{gathered}
}
\]

Therefore the strongest surviving candidate compression is:

\[
\boxed{
\textbf{No unaccounted evidential self-authorization.}
}
\]

with a necessary temporal corollary:

\[
\boxed{
\textbf{Revision may change future claim identity without rewriting past evidential identity.}
}
\]

These remain adversarial results only.

---

# 20. Authority boundary

```text
EMPIRICAL AUTHORITY CHANGE                  NONE
RESEARCH STATE TRANSITION                   NONE
CCA EPISTEMIC CONSTITUTION LAW              NOT CANONICAL
NO-EVIDENTIAL-SELF-AUTHORIZATION RULE       REFINED CANDIDATE ONLY
ADAPTIVE MEASUREMENT CONTRACT               NOT FROZEN
CLAIM VERSIONING SCHEMA                      NOT FROZEN
EVIDENCE-ROLE LEDGER                         NOT FROZEN
SEQUENTIAL INFERENCE REQUIREMENT             NOT UNIVERSALLY FROZEN
FRESH-HOLDOUT REQUIREMENT                    REFUTED AS UNIVERSAL
SAME-DATA REUSE PROHIBITION                  REFUTED AS UNIVERSAL
C_improve                                    NOT CANONICALIZED
IMPLEMENTATION / EXECUTION                   NOT AUTHORIZED
```

---

# 21. Next decision boundary

If this attack survives review, CCA should still resist immediate canonization.

A stronger next test would ask whether the surviving rule can be made representation-invariant across different but inferentially equivalent adaptive protocols, or whether “claim identity” and “protocol identity” themselves depend on a prospectively licensed equivalence class.

That would test whether the methodology can distinguish scientifically consequential adaptation from mere implementation variation without recreating the same retrospective-identity problem one level higher.
