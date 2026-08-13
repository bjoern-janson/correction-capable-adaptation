"""Deterministic AUDIT -> CHALLENGE -> RETURN worked example."""

from __future__ import annotations

import json
from typing import Any, Dict

from tevpp import (
    Lineage,
    LineageEdge,
    OperatorRef,
    audit,
    canonical_deserialize,
    canonical_serialize,
    challenge,
    return_successor,
)


def realized_edge(
    input_state: str,
    operator_name: str,
    output_state: str,
    version: int,
) -> LineageEdge:
    return LineageEdge.create(
        input_state,
        OperatorRef.create(operator_name, {"version": version}),
        output_state,
        constraints={"admissible": True},
        provenance={"example": "tev-return-minimal", "version": version},
        evidence={"realized": True},
    )


def build_example() -> Dict[str, Any]:
    normalize = realized_edge("R0", "normalize", "R1", 1)
    lossy_reduce = realized_edge("R1", "lossy_reduce", "Y", 1)
    l0 = Lineage.root((normalize, lossy_reduce))
    l0_before = canonical_serialize(l0)

    c1 = challenge(
        l0,
        lossy_reduce.edge_id,
        evidence={
            "evidence_id": "E_challenge",
            "reason": "lossy_reduce discarded a distinction required downstream",
        },
        created_provenance={"actor": "example-auditor", "sequence": 1},
    )

    preserve = realized_edge("R1", "preserve_distinctions", "R2_prime", 2)
    derive = realized_edge("R2_prime", "derive_output", "Y_prime", 1)
    l1 = return_successor(l0, c1, (preserve, derive))

    assert canonical_serialize(l0) == l0_before
    return {
        "challenge": canonical_deserialize(canonical_serialize(c1)),
        "l0": canonical_deserialize(l0_before),
        "l0_audit": audit(l0),
        "l0_canonical_hash": l0.canonical_hash,
        "l0_lineage_id": l0.lineage_id,
        "l1": canonical_deserialize(canonical_serialize(l1)),
        "l1_audit": audit(l1),
        "l1_canonical_hash": l1.canonical_hash,
        "l1_lineage_id": l1.lineage_id,
        "l1_parent_lineage_id": l1.parent_lineage_id,
    }


def main() -> None:
    print(json.dumps(build_example(), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
