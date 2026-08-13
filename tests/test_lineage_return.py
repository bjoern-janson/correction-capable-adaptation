from __future__ import annotations

import copy
import hashlib
import json
import unittest
from dataclasses import FrozenInstanceError

from tevpp import (
    CanonicalizationError,
    Challenge,
    IdentityMismatch,
    InvalidLineage,
    InvalidReturn,
    Lineage,
    LineageEdge,
    OperatorRef,
    TargetNotFound,
    audit,
    canonical_deserialize,
    canonical_serialize,
    challenge,
    return_successor,
)


def edge(
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
        provenance={"implementation": operator_name, "version": version},
        evidence={"realization": "fixture"},
    )


class LineageReturnTests(unittest.TestCase):
    def setUp(self) -> None:
        self.o1 = edge("R0", "normalize", "R1", 1)
        self.o2 = edge("R1", "lossy_reduce", "Y", 1)
        self.l0 = Lineage.root((self.o1, self.o2))
        self.c1 = challenge(
            self.l0,
            self.o2.edge_id,
            evidence={
                "evidence_id": "E_challenge",
                "reason": "lossy reduction discarded a required distinction",
            },
            created_provenance={"actor": "fixture-auditor", "sequence": 1},
        )
        self.o2_prime = edge("R1", "preserve_distinctions", "R2_prime", 2)
        self.o3_prime = edge("R2_prime", "derive_output", "Y_prime", 1)

    def make_l1(self) -> Lineage:
        return return_successor(self.l0, self.c1, (self.o2_prime, self.o3_prime))

    def test_end_to_end_audit_challenge_return(self) -> None:
        before = canonical_serialize(self.l0)
        before_hash = hashlib.sha256(before).hexdigest()
        l1 = self.make_l1()

        self.assertEqual(canonical_serialize(self.l0), before)
        self.assertEqual(hashlib.sha256(canonical_serialize(self.l0)).hexdigest(), before_hash)
        self.assertEqual(l1.parent_lineage_id, self.l0.lineage_id)
        self.assertEqual(l1.return_record.challenge_id, self.c1.challenge_id)
        self.assertEqual(l1.return_record.challenge_evidence_id, self.c1.evidence_id)
        self.assertEqual(l1.return_record.challenged_edge_id, self.o2.edge_id)
        self.assertEqual(l1.return_record.return_anchor, "R1")
        self.assertEqual(
            l1.return_record.preserved_prefix_edge_ids, (self.o1.edge_id,)
        )
        self.assertEqual(
            l1.return_record.successor_edge_ids,
            (self.o2_prime.edge_id, self.o3_prime.edge_id),
        )
        self.assertEqual(
            tuple(item.edge_id for item in l1.edges),
            (self.o1.edge_id, self.o2_prime.edge_id, self.o3_prime.edge_id),
        )

    def test_challenge_targets_exact_lineage_and_edge_without_mutation(self) -> None:
        before = canonical_serialize(self.l0)
        challenge_before = canonical_serialize(self.c1)
        self.make_l1()
        self.assertEqual(self.c1.target_lineage_id, self.l0.lineage_id)
        self.assertEqual(self.c1.target_edge_id, self.o2.edge_id)
        self.assertEqual(canonical_serialize(self.l0), before)
        self.assertEqual(canonical_serialize(self.c1), challenge_before)

    def test_prefix_is_preserved_by_stable_identity(self) -> None:
        l1 = self.make_l1()
        self.assertEqual(l1.edges[0].edge_id, self.l0.edges[0].edge_id)
        self.assertEqual(
            canonical_serialize(l1.edges[0]), canonical_serialize(self.l0.edges[0])
        )

    def test_successor_has_distinct_operator_and_edge_identities(self) -> None:
        l1 = self.make_l1()
        self.assertNotEqual(self.o2_prime.edge_id, self.o2.edge_id)
        self.assertNotEqual(
            self.o2_prime.operator.operator_id, self.o2.operator.operator_id
        )
        l0_ids = {item.edge_id for item in self.l0.edges}
        self.assertTrue(
            l0_ids.isdisjoint({self.o2_prime.edge_id, self.o3_prime.edge_id})
        )
        self.assertEqual(l1.lineage_id, Lineage.from_record(l1.to_record()).lineage_id)

    def test_audit_keeps_both_histories_visible(self) -> None:
        l1 = self.make_l1()
        audit_l0 = audit(self.l0)
        audit_l1 = audit(l1)
        self.assertEqual(
            [item["operator_identity"] for item in audit_l0["ordered_edges"]],
            ["normalize", "lossy_reduce"],
        )
        self.assertEqual(
            [item["operator_identity"] for item in audit_l1["ordered_edges"]],
            ["normalize", "preserve_distinctions", "derive_output"],
        )
        self.assertEqual(audit_l1["parent_lineage_id"], self.l0.lineage_id)
        self.assertEqual(audit_l1["ancestry"]["challenge_id"], self.c1.challenge_id)
        self.assertEqual(audit_l1["ancestry"]["challenged_edge_id"], self.o2.edge_id)
        self.assertEqual(audit_l1["ancestry"]["return_anchor"], "R1")
        self.assertIn(self.o2.edge_id, [item["edge_id"] for item in audit_l0["ordered_edges"]])
        self.assertNotIn(self.o2.edge_id, [item["edge_id"] for item in audit_l1["ordered_edges"]])

    def test_audit_contains_transitions_provenance_evidence_and_neighbors(self) -> None:
        view = audit(self.l0)
        first, second = view["ordered_edges"]
        self.assertEqual(first["successor_edge_id"], second["edge_id"])
        self.assertEqual(second["predecessor_edge_id"], first["edge_id"])
        self.assertIsNone(first["predecessor_edge_id"])
        self.assertIsNone(second["successor_edge_id"])
        self.assertEqual(view["state_transitions"][1]["from"], "R1")
        self.assertEqual(view["state_transitions"][1]["to"], "Y")
        self.assertIn("provenance_id", second)
        self.assertIn("evidence_id", second)

    def test_audit_is_detached_from_immutable_values(self) -> None:
        before = canonical_serialize(self.l0)
        view = audit(self.l0)
        view["ordered_edges"][0]["provenance"]["implementation"] = "tampered"
        self.assertEqual(canonical_serialize(self.l0), before)

    def test_nested_input_mutation_cannot_change_edge_or_lineage(self) -> None:
        metadata = {"version": 1, "options": ["stable"]}
        provenance = {"source": {"commit": "abc"}}
        local_edge = LineageEdge.create(
            "R0",
            OperatorRef.create("normalize", metadata),
            "R1",
            constraints={"allowed": ["x"]},
            provenance=provenance,
            evidence={"observed": True},
        )
        local_lineage = Lineage.root((local_edge,))
        before = canonical_serialize(local_lineage)
        metadata["options"].append("mutated")
        provenance["source"]["commit"] = "changed"
        self.assertEqual(canonical_serialize(local_lineage), before)
        with self.assertRaises(FrozenInstanceError):
            local_edge.input_state = "changed"

    def test_mapping_order_and_unicode_normalization_are_deterministic(self) -> None:
        composed = "caf\u00e9"
        decomposed = "cafe\u0301"
        first = LineageEdge.create(
            "R0",
            OperatorRef.create("normalize", {"b": 2, "a": decomposed}),
            "R1",
            constraints={"z": 0, "a": 1},
            provenance={"right": 2, "left": 1},
            evidence={"text": decomposed},
        )
        second = LineageEdge.create(
            "R0",
            OperatorRef.create("normalize", {"a": composed, "b": 2}),
            "R1",
            constraints={"a": 1, "z": 0},
            provenance={"left": 1, "right": 2},
            evidence={"text": composed},
        )
        self.assertEqual(canonical_serialize(first), canonical_serialize(second))
        self.assertEqual(first.edge_id, second.edge_id)

    def test_round_trip_serialization_is_byte_identical(self) -> None:
        original = canonical_serialize(self.l0)
        record = canonical_deserialize(original)
        self.assertIsInstance(record, dict)
        restored = Lineage.from_record(record)
        self.assertEqual(canonical_serialize(restored), original)
        self.assertEqual(restored.lineage_id, self.l0.lineage_id)

    def test_challenge_unknown_edge_fails(self) -> None:
        with self.assertRaisesRegex(TargetNotFound, "not uniquely present"):
            challenge(
                self.l0,
                "edge:v1:sha256:" + "0" * 64,
                evidence={"reason": "unknown"},
                created_provenance={"actor": "auditor"},
            )

    def test_challenge_for_different_lineage_fails_return(self) -> None:
        other = Lineage.root((edge("A", "other", "B", 1),))
        other_challenge = challenge(
            other,
            other.edges[0].edge_id,
            evidence={"reason": "other"},
            created_provenance={"actor": "auditor"},
        )
        with self.assertRaisesRegex(InvalidReturn, "different lineage"):
            return_successor(
                self.l0, other_challenge, (self.o2_prime, self.o3_prime)
            )

    def test_direct_challenge_with_different_edge_fails_return(self) -> None:
        unknown = Challenge(
            self.l0.lineage_id,
            "edge:v1:sha256:" + "f" * 64,
            self.c1.evidence,
            self.c1.created_provenance,
        )
        with self.assertRaisesRegex(InvalidReturn, "one exact ancestor edge"):
            return_successor(self.l0, unknown, (self.o2_prime, self.o3_prime))

    def test_successor_must_start_at_return_anchor(self) -> None:
        wrong = edge("R0", "replacement", "R2_prime", 2)
        with self.assertRaisesRegex(InvalidReturn, "return anchor"):
            return_successor(self.l0, self.c1, (wrong,))

    def test_successor_must_be_internally_continuous(self) -> None:
        disconnected = edge("somewhere_else", "derive_output", "Y_prime", 1)
        with self.assertRaisesRegex(InvalidReturn, "discontinuous path"):
            return_successor(self.l0, self.c1, (self.o2_prime, disconnected))

    def test_successor_cannot_be_empty(self) -> None:
        with self.assertRaisesRegex(InvalidReturn, "must not be empty"):
            return_successor(self.l0, self.c1, ())

    def test_successor_cannot_reuse_challenged_edge(self) -> None:
        with self.assertRaisesRegex(InvalidReturn, "reuses an immutable ancestor"):
            return_successor(self.l0, self.c1, (self.o2,))

    def test_successor_requires_new_operator_realization(self) -> None:
        same_operator_new_edge = LineageEdge.create(
            "R1",
            self.o2.operator,
            "Y_prime",
            constraints={"admissible": True},
            provenance={"implementation": "new wrapper"},
            evidence={"realization": "new"},
        )
        with self.assertRaisesRegex(InvalidReturn, "new operator realization"):
            return_successor(self.l0, self.c1, (same_operator_new_edge,))

    def test_changed_content_cannot_reuse_existing_edge_id(self) -> None:
        record = copy.deepcopy(self.o2.to_record())
        record["body"]["R_out"] = "forged-output"
        with self.assertRaisesRegex(IdentityMismatch, "id does not match"):
            LineageEdge.from_record(record)

    def test_changed_content_cannot_reuse_existing_challenge_id(self) -> None:
        record = copy.deepcopy(self.c1.to_record())
        record["body"]["target_edge_id"] = self.o1.edge_id
        with self.assertRaisesRegex(IdentityMismatch, "id does not match"):
            Challenge.from_record(record)

    def test_discontinuous_lineage_is_invalid(self) -> None:
        wrong = edge("X", "other", "Y", 1)
        with self.assertRaisesRegex(InvalidLineage, "discontinuous"):
            Lineage.root((self.o1, wrong))

    def test_duplicate_edge_identity_is_invalid(self) -> None:
        loop = edge("R", "identity", "R", 1)
        with self.assertRaisesRegex(InvalidLineage, "duplicate edge ids"):
            Lineage.root((loop, loop))

    def test_root_and_successor_ancestry_cannot_be_half_populated(self) -> None:
        with self.assertRaisesRegex(InvalidLineage, "requires a return record"):
            Lineage((self.o1,), parent_lineage_id=self.l0.lineage_id)

    def test_noncanonical_payloads_and_duplicate_json_keys_fail(self) -> None:
        invalid_values = [1.5, float("nan"), {"set": {1}}, {1: "bad"}, b"bytes"]
        for value in invalid_values:
            with self.subTest(value=repr(value)):
                with self.assertRaises(CanonicalizationError):
                    canonical_serialize(value)
        with self.assertRaisesRegex(CanonicalizationError, "duplicate JSON key"):
            canonical_deserialize('{"a":1,"a":2}')


if __name__ == "__main__":
    unittest.main()
