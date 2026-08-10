# Measurement Layer

The current research frontier is measurement, not model execution.

The central unresolved choice is what **evidence use** is intended to mean.

## Broad evidence use

\[
G_1^{\mathrm{broad}}:E\rightarrow C_{\mathrm{selected}}.
\]

Under this object, any independently warranted information legitimately carried by the evidence may support candidate selection.

## Relational evidence use

\[
G_1^{\mathrm{relational}}:(X,Y,\mathrm{pairing})\rightarrow C_{\mathrm{selected}}.
\]

This is stronger. The intended claim would be that selection depends on the demonstrated input-output relation **beyond a prospectively licensed class of non-relational information channels**.

A candidate's output marginal is not automatically a “bad shortcut”: it may be a legitimate semantic consequence of the function. The scientific object must therefore be specified before nuisance features are declared.

## Evidence-codebook feasibility result

A proposed construction uses a shared probe set \(X\) and candidate functions \(f_c\):

\[
e_c=\{(x,f_c(x)):x\in X\}.
\]

The destructive analysis established:

\[
\boxed{\text{universal relational-codebook construction}=\mathrm{REFUTED}}
\]

and

\[
\boxed{\text{ontology-conditional relational construction}=\mathrm{FEASIBLE\ IN\ PRINCIPLE}}.
\]

Relational evidence use therefore cannot be demanded independently of the candidate ontology.

## Ontology admissibility if relational G1 is chosen

A future relational ontology class would have the form:

\[
\mathfrak C_{\mathrm{relational}}
=
\left\{
\mathcal C:
\exists X\text{ satisfying the frozen relational-identification contract}
\right\}.
\]

The exact contract is deliberately not frozen yet.

The key order is:

```text
scientific object
    ↓
ontology
    ↓
semantics
    ↓
measurement construction
    ↓
adversarial admissibility
    ↓
only then freeze E
```

## Semantic validity dominates nuisance balancing

If achieving nuisance balance requires altering the demonstrated candidate functions, reject the construction rather than recoding the evidence.

```text
semantic validity
> identifiability
> redundancy
> nuisance control
```

A lower-level balancing objective may not change the higher-level scientific object.

## Permanent design regression cases

See [`regression-cases/RELATIONAL_CODEBOOK_WITNESSES.md`](regression-cases/RELATIONAL_CODEBOOK_WITNESSES.md).

Any future relational-codebook validator must distinguish:

```text
constant-function ontology        -> UNSAT
balanced relational ontology      -> SAT in principle
```

without querying a tested model.
