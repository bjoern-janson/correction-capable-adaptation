# Minimal executable AUDIT → CHALLENGE → RETURN

## Status and authority ceiling

This implementation demonstrates executable lineage preservation and successor
construction. It does not establish novelty, causal authority, or superiority
over existing provenance systems.

It is a dependency-free engineering primitive. It does not add a CCA formal
primitive, encode CCA, expand an ontology, alter research authority, or infer a
policy from provenance. The challenge record is an explicit engineering input;
its existence does not prove that its evidence is scientifically warranted.

## Scope

The module implements one linear-lineage property:

> A challenged transformation can be superseded by an explicit successor path
> without rewriting or destroying the historical lineage that produced the old
> result.

It provides four deeply immutable value objects:

- `LineageEdge` preserves the six roles `(R_in, O, R_out, C, P, E)`;
- `Lineage` holds one ordered continuous path;
- `Challenge` targets one exact edge in one exact lineage; and
- `ReturnRecord` makes ancestor, challenge, challenged edge, anchor, preserved
  prefix, and successor identities explicit.

The six edge roles are:

| Role | Concrete field | Meaning |
| --- | --- | --- |
| `R_in` | `input_state` | Input representation/state identifier |
| `O` | `operator` | Operator identifier and realization metadata |
| `R_out` | `output_state` | Output representation/state identifier |
| `C` | `constraints` | Constraints/admissibility attached to the edge |
| `P` | `provenance` | Information needed to identify/reproduce the edge |
| `E` | `evidence` | Evidence attached to this realization |

No RETURN ancestry or challenge relationship is inferred only from array
position. A successor record stores
stable identifiers for the ancestor lineage, exact challenge and challenge
evidence, challenged edge, return anchor, preserved prefix, and new path.

## Stable identity and immutability

Each value snapshots its nested payload into a restricted canonical JSON domain.
The serializer:

- accepts only `null`, booleans, integers, strings, arrays, and string-keyed
  objects;
- normalizes strings to Unicode NFC;
- sorts object keys and uses fixed UTF-8 JSON separators;
- rejects floats, non-finite values, sets, bytes, custom objects, non-string
  keys, and duplicate JSON keys; and
- domain-separates and versions SHA-256 content identifiers.

An edge identifier covers all six semantic roles. Supplying an old identifier
with changed content fails reconstruction. Frozen dataclasses do not retain
caller-owned dictionaries or lists, so later mutation of an input object cannot
change an edge, lineage, canonical serialization, or identity.

This is deliberately not a generalized content-addressed store.

## Executable example

The example creates:

```text
L0:
R0 --normalize--> R1 --lossy_reduce--> Y
```

It audits `L0`, creates an immutable challenge to `lossy_reduce`, returns to
`R1`, and constructs:

```text
L1:
R0 --normalize--> R1 --preserve_distinctions--> R2_prime
   --derive_output--> Y_prime
```

`L0` is serialized before RETURN and asserted byte-identical afterward. `L1`
references `L0`, the challenge, its evidence, the old challenged edge, and `R1`
through stable identifiers. The original challenged edge remains in `L0`.

Run from the repository root:

```text
python -m examples.tev_return_minimal
```

The deterministic JSON output contains canonical records, lineage IDs, content
hashes, and structured audits for both histories.

## Tests

Run:

```text
python -m unittest discover -s tests -p "test_lineage_return.py" -v
```

The tests cover:

- canonical byte/hash preservation of `L0` across RETURN;
- explicit parent, challenge, evidence, challenged-edge, anchor, prefix, and
  successor linkage;
- distinct replacement operator/edge realizations;
- continued audit visibility of both histories;
- deep immutability and deterministic serialization;
- round-trip identity validation; and
- unknown/mismatched challenges, wrong anchors, empty or discontinuous paths,
  ancestor-edge reuse, operator-realization reuse, malformed lineages, spoofed
  IDs, and noncanonical payloads.

## Deliberate limits

The implementation is a linear path primitive, not a database, DAG framework,
distributed event system, workflow engine, rollback mechanism, or policy engine.
It stores no objects and performs no scientific adjudication. Broader persistence,
branch merging, access control, signatures, distributed consistency, and domain
semantics remain outside this demonstration.
