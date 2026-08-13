# Minimal G1 Apparatus Referent Specification

## Status

**FROZEN REFERENT SPECIFICATION — CONCRETE APPARATUS REFERENT NOT YET BOUND — NO FIDELITY AUDIT EXECUTED — NO IMPLEMENTATION OR EXECUTION AUTHORIZED — G1 UNTESTED**

\[
\boxed{
D_{\mathrm{g1\ minimal\ referent\ specification}}
=
\mathrm{REFERENT\_SPECIFICATION\_FROZEN}
}
\]

\[
\boxed{
D_{\mathrm{g1\ minimal\ referent}}
=
\mathrm{NOT\_YET\_BOUND}
}
\]

This artifact freezes the blueprint for the smallest concrete apparatus intended solely for fidelity-audit validation under the frozen G1 Apparatus Fidelity Audit Protocol.

It does **not** claim that the concrete apparatus referent has already been content-addressed or bound. Load-bearing implementation values, code/configuration hashes, synthetic-domain instances, exact transport implementation, and other concrete identities must still be instantiated and frozen before the apparatus can receive `CONCRETE_APPARATUS_REFERENT_FROZEN`.

No fidelity audit has been executed. No execution authority is granted. \(G_1\) remains untested.

---

## 1. Purpose and scope limitation

\[
\boxed{
\texttt{g1-minimal-v0}\ \text{is constituted for fidelity-audit validation only.}
}
\]

\[
\boxed{
\mathrm{FIDELITY\_PASS}
\not\Rightarrow
\text{this }\pi\text{ is scientifically authorized for a }G_1\text{ effect experiment.}
}
\]

A later execution-authority decision must separately determine whether any policy is scientifically worth testing.

---

## 2. Apparatus referent schema \(\mathfrak a_A\)

The future bound apparatus must instantiate the inherited referent tuple without coordinate redefinition:

\[
\mathfrak a_A=(I,V,C,\Gamma,B,Q,R,E,\Omega,P).
\]

| Coordinate | Frozen specification |
|---|---|
| \(I\) | Apparatus identity `g1-minimal-v0`; selector implementation identity; adjudicator implementation identity |
| \(V\) | Exact code and configuration revision hashes, to be instantiated and fixed at concrete referent binding |
| \(C\) | Fixed candidate set \(\{c_A,c_B\}\); process configuration; permissions |
| \(\Gamma\) | Concrete transport graph defined in §5; implementation details and hashes bound at realization |
| \(B\) | Complete declared selector-accessible state at decision time |
| \(Q\) | Prospective treatment-assignment mechanism |
| \(R\) | Per-unit reset / isolation regime |
| \(E\) | Adjudicator / evaluator / selector access-separation boundary |
| \(\Omega\) | Synthetic validation domain only |
| \(P\) | Provenance scheme with auditor-owned checkpoints |

Load-bearing referent drift after concrete binding requires a new audit.

The specification-to-binding boundary is explicit:

\[
\boxed{
\text{frozen referent specification}
\neq
\text{bound concrete referent}.
}
\]

---

## 3. Concrete synthetic source and direction objects

A future implementation must bind an exact finite synthetic domain:

\[
X=\{x_1,\ldots,x_k\},
\]

with all of the following concretely instantiated before referent binding:

- deterministic candidate-response object \(O_C(X)\);
- deterministic evidence constructor \(g:O_C(X)\mapsto E\);
- adjudicator \(q:E\mapsto D_{\rm ind}\);
- separate frozen independent reference \(r:E\mapsto D_{\rm ref}\);
- prospectively frozen agreement threshold \(\gamma_{\rm frozen}\), sample construction, tie handling, and estimator.

The validity requirement is:

\[
\widehat{\mathrm{Agree}}(q(E),r(E))\geq\gamma_{\rm frozen}.
\]

Self-agreement is forbidden:

\[
q\not\equiv r.
\]

The exact \(X\), \(k\), \(O_C(X)\), \(g\), \(q\), \(r\), and \(\gamma_{\rm frozen}\) are binding-time values, not yet supplied by this specification.

---

## 4. Package construction and treatment ordering

Both potential exposures must be constituted before treatment assignment:

\[
\begin{aligned}
&C\ \mathrm{locked}\\
&\rightarrow O_C(X)\\
&\rightarrow E_{\rm adm}\\
&\rightarrow D_{\rm ind}\\
&\rightarrow
\begin{cases}
S^{(1)}_{\rm specified}=(E,D),\\
S^{(0)}_{\rm specified}=N(E)
\end{cases}\\
&\rightarrow T_E=f(U_{\rm rng},\text{licensed randomizer inputs})\\
&\rightarrow S_{\rm realized}=S^{(T_E)}_{\rm specified}\\
&\rightarrow \text{transport }(\Gamma)\\
&\rightarrow S_{\rm selector}\\
&\rightarrow \pi\\
&\rightarrow C_{\rm selected}.
\end{aligned}
\]

Package construction may not become treatment-dependent.

The concrete null generator \(N(E)\), its matched coordinates, tolerances, and direction-independence rule are binding-time values and must be prospectively frozen before audit observations.

---

## 5. Transformation graph \(\Gamma\)

Because adjudicator and selector are separate processes, the apparatus must expose the actual inter-process transport rather than assume identity:

\[
\Gamma:
S_{\rm specified}
\xrightarrow{\mathrm{serialize}}
m
\xrightarrow{\mathrm{IPC}}
m'
\xrightarrow{\mathrm{deserialize}}
S_{\rm selector}.
\]

A prospectively licensed equivalence relation must be bound for the concrete implementation:

\[
S_{\rm selector}\equiv_{\Gamma}S_{\rm specified}.
\]

Identity mapping is not claimed unless the realized transport earns it.

The concrete serializer, IPC mechanism, deserializer, message schema, comparison relation, and associated hashes are binding-time values.

---

## 6. Selector-accessible boundary and audit capture

The selector-facing scientific object and auditor-side evidence are distinct.

### Selector-facing state

\[
S_{\rm selector}
=
\text{exact payload/state accessible to }\pi\text{ at decision time}.
\]

### Auditor-side evidence

\[
R_{\rm boundary}
=
\text{auditor capture/manifest describing }S_{\rm selector}.
\]

Hard separation:

\[
\boxed{R_{\rm boundary}\notin B.}
\]

Auditor checkpoints and logs are selector-inaccessible. The selector operates only on \(S_{\rm selector}\). The audit reconstructs the declared boundary using \(R_{\rm boundary}\) and independently sufficient guarantees where exact capture is not available.

The intended minimal selector environment is:

```text
network              disabled
tools                none
filesystem           read-denied except fixed executable
environment          frozen
argv                 frozen
cwd                  frozen
history              none
persistent memory    none
```

At concrete binding, each of these conditions must be implemented, inspectable, and included in the referent manifest. Any potentially consequential opaque path remains `INVALID/UNRESOLVED` under the frozen audit protocol.

---

## 7. Selection mechanism \(\pi\)

The intended selector is deterministic and deliberately trivial:

\[
\pi(S_{\rm selector})=
\begin{cases}
\text{direction contained in }S_{\rm selector}, & \text{if present},\\
c_A, & \text{default control action}.
\end{cases}
\]

Its purpose is inspectability of the fidelity apparatus only. It is not proposed as an informative scientific G1 target.

Consequently:

\[
\boxed{
\mathrm{FIDELITY\_PASS}
\not\Rightarrow
\mathrm{AUTH}(G_1\text{ execution with this }\pi).
}
\]

---

## 8. Isolation, reset, randomization, and provenance

The concrete realization must implement:

- full process separation between adjudicator and selector;
- no shared mutable state, parameters, prompt state, or unlicensed side channels;
- a clean selector process image per unit;
- a prospectively frozen treatment-assignment mechanism using \(U_{\rm rng}\) as the exogenous randomizer draw and only licensed inputs;
- a concrete PRNG/entropy source and seed or randomness-provenance policy bound in \(Q\);
- append-only hash chaining for audit records;
- auditor-owned receipt of each episode root hash or campaign checkpoint so the apparatus cannot unilaterally rewrite the full chain.

The exact randomizer implementation, randomness-provenance policy, process-reset mechanism, and provenance implementation are binding-time values.

---

## 9. Audit firewall

All units generated while this apparatus is being fidelity-audited belong prospectively to \(U_{\rm audit}\).

\[
\boxed{U_{\rm audit}\cap U_{G1}=\varnothing.}
\]

Audit units are permanently excluded from any future \(G_1\) effect estimate and cannot be reclassified.

No information from audit-unit selections may be used to tune the treatment package, candidate set, null generator, thresholds, selector, or apparatus and then count the same units as experimental evidence.

---

## 10. Binding checklist

The concrete referent may advance to

\[
D_{\mathrm{g1\ minimal\ referent}}
=
\mathrm{CONCRETE\_APPARATUS\_REFERENT\_FROZEN}
\]

only after all load-bearing values are instantiated and content-addressed, including at minimum:

1. exact apparatus, selector, and adjudicator implementation identities;
2. exact code/configuration hashes;
3. exact \(X\), \(k\), \(O_C(X)\), \(g\), \(q\), \(r\), and \(\gamma_{\rm frozen}\);
4. exact candidate representation and bindings;
5. exact null generator, comparison rule, matched coordinates, and tolerances;
6. exact randomizer/PRNG construction and randomness-provenance policy;
7. exact serializer, IPC mechanism, deserializer, schema, and \(\Gamma\)-equivalence rule;
8. exact selector-facing environment and permission manifest;
9. exact reset/isolation implementation;
10. exact provenance/hash-chain implementation and auditor-owned checkpoint mechanism;
11. one immutable referent manifest binding all of the above.

No fidelity observations may be used to choose these values retroactively.

---

## 11. Current authority state

\[
\boxed{
\begin{aligned}
D_{\mathrm{g1\ minimal\ referent\ specification}}
&=\mathrm{REFERENT\_SPECIFICATION\_FROZEN},\\
D_{\mathrm{g1\ minimal\ referent}}
&=\mathrm{NOT\_YET\_BOUND},\\
D_{\mathrm{G1\ apparatus}}
&=\mathrm{UNTESTED},\\
\text{Fidelity audit}
&=\mathrm{NOT\ EXECUTED},\\
\mathrm{AUTH(execution)}
&=\mathrm{FALSE},\\
G_1
&=\mathrm{UNTESTED}.
\end{aligned}
}
\]

This artifact creates no implementation authority and moves no empirical authority.

---

## 12. Next legitimate action

The next admissible transition is implementation and binding, not further conceptual expansion:

\[
\boxed{
\text{frozen specification}
\rightarrow
\text{implement exact apparatus}
\rightarrow
\text{bind concrete values + hashes}
\rightarrow
\mathrm{CONCRETE\_APPARATUS\_REFERENT\_FROZEN}
\rightarrow
\text{fidelity audit}.
}
\]

No conceptual v3 is authorized absent a realized implementation or audit failure that discriminates against this frozen specification.
