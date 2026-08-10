# Relational Codebook Regression Witnesses

These are **measurement-layer design tests**, not experimental conditions and not model benchmarks.

Any future validator for a relational evidence-codebook construction should classify these two cases differently.

---

## Witness 1 — relationally impossible

Let the candidate ontology be:

\[
\mathcal C=\{c_0,c_1\}
\]

with

\[
f_{c_0}(x)=0,
\qquad
f_{c_1}(x)=1
\]

for every admissible probe \(x\).

For any faithful shared probe set \(X\):

\[
e_{c_0}=\{(x_i,0)\}_{i=1}^n,
\qquad
 e_{c_1}=\{(x_i,1)\}_{i=1}^n.
\]

The warranted candidate is perfectly identifiable, but it is also perfectly recoverable from the output marginal alone. Destroying the input-output pairing changes nothing relevant.

Therefore the pairing relation contributes no separately identifiable candidate authority.

### Required validator result

```text
RELATIONAL G1: UNSAT
```

Trying to equalize the output marginals would require altering the demonstrated functions and therefore changing the scientific object.

---

## Witness 2 — relationally feasible in principle

Let candidates be:

\[
c\in\{0,1,2\}
\]

and define two semantic regions:

\[
\mathcal X=\{(A,u),(B,u):u\in\{0,1,2\}\}.
\]

Define:

\[
f_c(A,u)=\mathbf 1[u=c]
\]

and

\[
f_c(B,u)=\mathbf 1[u=c+1\pmod 3].
\]

Using the complete shared probe set gives:

| candidate | region A | region B |
| --- | --- | --- |
| 0 | `1,0,0` | `0,1,0` |
| 1 | `0,1,0` | `0,0,1` |
| 2 | `0,0,1` | `1,0,0` |

Every candidate has the same output multiset within each region:

```text
{1,0,0}
```

and the same global output multiset:

```text
{1,1,0,0,0,0}
```

Candidate identity is instead carried by which output is paired with which input.

Each semantic region independently identifies the candidate, so the construction also has multi-region redundancy rather than one distinguishing bit repeated many times.

Candidate-independent presentation randomization can remove list-position leakage without altering pair semantics.

### Required validator result

```text
RELATIONAL G1: SAT IN PRINCIPLE
```

---

## Structural conclusion

Together these witnesses establish:

\[
\boxed{\text{relational evidence use is ontology-dependent}.}
\]

A measurement system that classifies both cases as feasible, or both as impossible, is itself invalid before a tested model enters the experiment.
