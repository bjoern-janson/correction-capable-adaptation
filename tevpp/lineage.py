"""A minimal immutable AUDIT -> CHALLENGE -> RETURN lineage primitive.

The module is deliberately a small provenance/versioning demonstration. It
does not encode CCA semantics, infer policy, or grant scientific authority.
"""

from __future__ import annotations

import hashlib
import json
import math
import unicodedata
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union


SCHEMA = "tevpp-lineage/v1"
JsonValue = Union[None, bool, int, str, List["JsonValue"], Dict[str, "JsonValue"]]


class LineageError(ValueError):
    """Base error for an invalid lineage operation."""


class CanonicalizationError(LineageError):
    """A value cannot be represented in the frozen canonical JSON domain."""


class IdentityMismatch(LineageError):
    """A supplied stable identifier does not match immutable content."""


class TargetNotFound(LineageError):
    """A challenge target is not present in the named lineage."""


class InvalidLineage(LineageError):
    """Edges or ancestry metadata do not form a valid linear lineage."""


class InvalidReturn(LineageError):
    """A requested successor does not satisfy RETURN invariants."""


def _normalized_string(value: str, path: str) -> str:
    if not isinstance(value, str):
        raise CanonicalizationError("%s must be a string" % path)
    normalized = unicodedata.normalize("NFC", value)
    if not normalized:
        raise CanonicalizationError("%s must not be empty" % path)
    return normalized


def _normalize_json(value: Any, path: str = "$") -> JsonValue:
    if value is None or isinstance(value, bool):
        return value
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise CanonicalizationError("%s contains a non-finite number" % path)
        raise CanonicalizationError(
            "%s contains a float; encode exact decimals as strings" % path
        )
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, (list, tuple)):
        return [
            _normalize_json(item, "%s[%d]" % (path, index))
            for index, item in enumerate(value)
        ]
    if isinstance(value, Mapping):
        normalized: Dict[str, JsonValue] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise CanonicalizationError("%s has a non-string object key" % path)
            normalized_key = unicodedata.normalize("NFC", key)
            if normalized_key in normalized:
                raise CanonicalizationError(
                    "%s has duplicate keys after Unicode normalization" % path
                )
            normalized[normalized_key] = _normalize_json(
                item, "%s.%s" % (path, normalized_key)
            )
        return normalized
    raise CanonicalizationError(
        "%s contains unsupported type %s" % (path, type(value).__name__)
    )


def _reject_duplicate_keys(pairs: Sequence[Tuple[str, Any]]) -> Dict[str, Any]:
    value: Dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise CanonicalizationError("duplicate JSON key: %s" % key)
        value[key] = item
    return value


def canonical_deserialize(data: Union[str, bytes]) -> JsonValue:
    """Parse JSON and return its normalized restricted-domain value."""

    text = data.decode("utf-8") if isinstance(data, bytes) else data
    try:
        parsed = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=lambda token: (_ for _ in ()).throw(
                CanonicalizationError("non-finite JSON constant: %s" % token)
            ),
        )
    except UnicodeDecodeError as error:
        raise CanonicalizationError("canonical JSON must be UTF-8") from error
    except json.JSONDecodeError as error:
        raise CanonicalizationError("invalid JSON: %s" % error.msg) from error
    return _normalize_json(parsed)


def _canonical_bytes(value: Any) -> bytes:
    normalized = _normalize_json(value)
    return json.dumps(
        normalized,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _content_id(kind: str, body: Mapping[str, Any]) -> str:
    envelope = {"body": body, "kind": kind, "schema": SCHEMA}
    digest = hashlib.sha256(_canonical_bytes(envelope)).hexdigest()
    return "%s:v1:sha256:%s" % (kind, digest)


def _record(kind: str, body: Mapping[str, Any]) -> Dict[str, JsonValue]:
    normalized_body = _normalize_json(body)
    assert isinstance(normalized_body, dict)
    return {
        "body": normalized_body,
        "id": _content_id(kind, normalized_body),
        "kind": kind,
        "schema": SCHEMA,
    }


def _verified_body(record: Mapping[str, Any], kind: str) -> Mapping[str, Any]:
    expected_keys = {"body", "id", "kind", "schema"}
    if set(record) != expected_keys:
        raise IdentityMismatch("%s record fields differ from schema" % kind)
    if record.get("schema") != SCHEMA or record.get("kind") != kind:
        raise IdentityMismatch("%s record kind/schema mismatch" % kind)
    body = record.get("body")
    if not isinstance(body, Mapping):
        raise IdentityMismatch("%s record body must be an object" % kind)
    expected_id = _content_id(kind, body)
    if record.get("id") != expected_id:
        raise IdentityMismatch("%s id does not match immutable content" % kind)
    return body


@dataclass(frozen=True, init=False)
class CanonicalPayload:
    """A deeply immutable snapshot of one restricted JSON value."""

    _json: str

    def __init__(self, value: Any) -> None:
        object.__setattr__(self, "_json", _canonical_bytes(value).decode("utf-8"))

    @property
    def value_id(self) -> str:
        return _content_id("payload", {"value": self.to_value()})

    def to_value(self) -> JsonValue:
        return canonical_deserialize(self._json)

    def to_record(self) -> Dict[str, JsonValue]:
        return _record("payload", {"value": self.to_value()})

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> "CanonicalPayload":
        body = _verified_body(record, "payload")
        if set(body) != {"value"}:
            raise IdentityMismatch("payload body fields differ from schema")
        return cls(body["value"])


@dataclass(frozen=True)
class OperatorRef:
    """An operator identifier and the metadata defining this realization."""

    identifier: str
    metadata: CanonicalPayload

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "identifier", _normalized_string(self.identifier, "operator.identifier")
        )
        if not isinstance(self.metadata, CanonicalPayload):
            raise CanonicalizationError("operator.metadata must be a CanonicalPayload")

    @classmethod
    def create(cls, identifier: str, metadata: Any) -> "OperatorRef":
        return cls(identifier, CanonicalPayload(metadata))

    def to_body(self) -> Dict[str, Any]:
        return {"identifier": self.identifier, "metadata": self.metadata.to_record()}

    @property
    def operator_id(self) -> str:
        return _content_id("operator", self.to_body())

    def to_record(self) -> Dict[str, JsonValue]:
        return _record("operator", self.to_body())

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> "OperatorRef":
        body = _verified_body(record, "operator")
        if set(body) != {"identifier", "metadata"}:
            raise IdentityMismatch("operator body fields differ from schema")
        metadata = body["metadata"]
        if not isinstance(metadata, Mapping):
            raise IdentityMismatch("operator metadata record must be an object")
        value = cls(str(body["identifier"]), CanonicalPayload.from_record(metadata))
        if value.operator_id != record["id"]:
            raise IdentityMismatch("operator id failed reconstruction")
        return value


@dataclass(frozen=True)
class LineageEdge:
    """One immutable (R_in, O, R_out, C, P, E) realization."""

    input_state: str
    operator: OperatorRef
    output_state: str
    constraints: CanonicalPayload
    provenance: CanonicalPayload
    evidence: CanonicalPayload

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "input_state", _normalized_string(self.input_state, "edge.R_in")
        )
        object.__setattr__(
            self, "output_state", _normalized_string(self.output_state, "edge.R_out")
        )
        if not isinstance(self.operator, OperatorRef):
            raise CanonicalizationError("edge.O must be an OperatorRef")
        for name in ("constraints", "provenance", "evidence"):
            if not isinstance(getattr(self, name), CanonicalPayload):
                raise CanonicalizationError("edge.%s must be a CanonicalPayload" % name)

    @classmethod
    def create(
        cls,
        input_state: str,
        operator: OperatorRef,
        output_state: str,
        constraints: Any,
        provenance: Any,
        evidence: Any,
    ) -> "LineageEdge":
        return cls(
            input_state,
            operator,
            output_state,
            CanonicalPayload(constraints),
            CanonicalPayload(provenance),
            CanonicalPayload(evidence),
        )

    def to_body(self) -> Dict[str, Any]:
        return {
            "C": self.constraints.to_record(),
            "E": self.evidence.to_record(),
            "O": self.operator.to_record(),
            "P": self.provenance.to_record(),
            "R_in": self.input_state,
            "R_out": self.output_state,
        }

    @property
    def edge_id(self) -> str:
        return _content_id("edge", self.to_body())

    def to_record(self) -> Dict[str, JsonValue]:
        return _record("edge", self.to_body())

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> "LineageEdge":
        body = _verified_body(record, "edge")
        if set(body) != {"R_in", "O", "R_out", "C", "P", "E"}:
            raise IdentityMismatch("edge body fields differ from six-role schema")
        nested = (body["O"], body["C"], body["P"], body["E"])
        if not all(isinstance(value, Mapping) for value in nested):
            raise IdentityMismatch("edge nested records must be objects")
        value = cls(
            str(body["R_in"]),
            OperatorRef.from_record(body["O"]),
            str(body["R_out"]),
            CanonicalPayload.from_record(body["C"]),
            CanonicalPayload.from_record(body["P"]),
            CanonicalPayload.from_record(body["E"]),
        )
        if value.edge_id != record["id"]:
            raise IdentityMismatch("edge id failed reconstruction")
        return value


@dataclass(frozen=True)
class Challenge:
    """An immutable challenge to one exact edge in one exact lineage."""

    target_lineage_id: str
    target_edge_id: str
    evidence: CanonicalPayload
    created_provenance: CanonicalPayload

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "target_lineage_id",
            _normalized_string(self.target_lineage_id, "challenge.target_lineage_id"),
        )
        object.__setattr__(
            self,
            "target_edge_id",
            _normalized_string(self.target_edge_id, "challenge.target_edge_id"),
        )
        if not isinstance(self.evidence, CanonicalPayload):
            raise CanonicalizationError("challenge.evidence must be a CanonicalPayload")
        if not isinstance(self.created_provenance, CanonicalPayload):
            raise CanonicalizationError(
                "challenge.created_provenance must be a CanonicalPayload"
            )

    @property
    def evidence_id(self) -> str:
        return self.evidence.value_id

    def to_body(self) -> Dict[str, Any]:
        return {
            "created_provenance": self.created_provenance.to_record(),
            "evidence": self.evidence.to_record(),
            "evidence_id": self.evidence_id,
            "target_edge_id": self.target_edge_id,
            "target_lineage_id": self.target_lineage_id,
        }

    @property
    def challenge_id(self) -> str:
        return _content_id("challenge", self.to_body())

    def to_record(self) -> Dict[str, JsonValue]:
        return _record("challenge", self.to_body())

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> "Challenge":
        body = _verified_body(record, "challenge")
        required = {
            "created_provenance",
            "evidence",
            "evidence_id",
            "target_edge_id",
            "target_lineage_id",
        }
        if set(body) != required:
            raise IdentityMismatch("challenge body fields differ from schema")
        if not isinstance(body["evidence"], Mapping) or not isinstance(
            body["created_provenance"], Mapping
        ):
            raise IdentityMismatch("challenge payload records must be objects")
        value = cls(
            str(body["target_lineage_id"]),
            str(body["target_edge_id"]),
            CanonicalPayload.from_record(body["evidence"]),
            CanonicalPayload.from_record(body["created_provenance"]),
        )
        if value.evidence_id != body["evidence_id"]:
            raise IdentityMismatch("challenge evidence id does not match evidence")
        if value.challenge_id != record["id"]:
            raise IdentityMismatch("challenge id failed reconstruction")
        return value


@dataclass(frozen=True)
class ReturnRecord:
    """Explicit ancestry and path metadata for one RETURN successor."""

    ancestor_lineage_id: str
    challenged_edge_id: str
    challenge_id: str
    challenge_evidence_id: str
    return_anchor: str
    preserved_prefix_edge_ids: Tuple[str, ...]
    successor_edge_ids: Tuple[str, ...]

    def __post_init__(self) -> None:
        for name in (
            "ancestor_lineage_id",
            "challenged_edge_id",
            "challenge_id",
            "challenge_evidence_id",
            "return_anchor",
        ):
            object.__setattr__(self, name, _normalized_string(getattr(self, name), name))
        object.__setattr__(
            self, "preserved_prefix_edge_ids", tuple(self.preserved_prefix_edge_ids)
        )
        object.__setattr__(self, "successor_edge_ids", tuple(self.successor_edge_ids))
        if not self.successor_edge_ids:
            raise InvalidReturn("successor path must not be empty")
        for edge_id in self.preserved_prefix_edge_ids + self.successor_edge_ids:
            _normalized_string(edge_id, "return.edge_id")
        if len(set(self.preserved_prefix_edge_ids + self.successor_edge_ids)) != len(
            self.preserved_prefix_edge_ids + self.successor_edge_ids
        ):
            raise InvalidReturn("return record contains duplicate edge ids")

    def to_body(self) -> Dict[str, Any]:
        return {
            "ancestor_lineage_id": self.ancestor_lineage_id,
            "challenge_evidence_id": self.challenge_evidence_id,
            "challenge_id": self.challenge_id,
            "challenged_edge_id": self.challenged_edge_id,
            "preserved_prefix_edge_ids": list(self.preserved_prefix_edge_ids),
            "return_anchor": self.return_anchor,
            "successor_edge_ids": list(self.successor_edge_ids),
        }

    @property
    def return_id(self) -> str:
        return _content_id("return", self.to_body())

    def to_record(self) -> Dict[str, JsonValue]:
        return _record("return", self.to_body())

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> "ReturnRecord":
        body = _verified_body(record, "return")
        required = {
            "ancestor_lineage_id",
            "challenge_evidence_id",
            "challenge_id",
            "challenged_edge_id",
            "preserved_prefix_edge_ids",
            "return_anchor",
            "successor_edge_ids",
        }
        if set(body) != required:
            raise IdentityMismatch("return body fields differ from schema")
        value = cls(
            str(body["ancestor_lineage_id"]),
            str(body["challenged_edge_id"]),
            str(body["challenge_id"]),
            str(body["challenge_evidence_id"]),
            str(body["return_anchor"]),
            tuple(str(item) for item in body["preserved_prefix_edge_ids"]),
            tuple(str(item) for item in body["successor_edge_ids"]),
        )
        if value.return_id != record["id"]:
            raise IdentityMismatch("return id failed reconstruction")
        return value


def _validate_edge_path(edges: Sequence[LineageEdge]) -> None:
    if not edges:
        raise InvalidLineage("a lineage must contain at least one edge")
    if not all(isinstance(edge, LineageEdge) for edge in edges):
        raise InvalidLineage("lineage edges must be LineageEdge values")
    ids = [edge.edge_id for edge in edges]
    if len(ids) != len(set(ids)):
        raise InvalidLineage("lineage contains duplicate edge ids")
    for left, right in zip(edges, edges[1:]):
        if left.output_state != right.input_state:
            raise InvalidLineage(
                "discontinuous path: %s != %s"
                % (left.output_state, right.input_state)
            )


@dataclass(frozen=True)
class Lineage:
    """An immutable ordered path with optional explicit RETURN ancestry."""

    edges: Tuple[LineageEdge, ...]
    parent_lineage_id: Optional[str] = None
    return_record: Optional[ReturnRecord] = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "edges", tuple(self.edges))
        _validate_edge_path(self.edges)
        if self.parent_lineage_id is None and self.return_record is not None:
            raise InvalidLineage("root lineage cannot contain a return record")
        if self.parent_lineage_id is not None and self.return_record is None:
            raise InvalidLineage("successor lineage requires a return record")
        if self.parent_lineage_id is None:
            return
        normalized_parent = _normalized_string(
            self.parent_lineage_id, "lineage.parent_lineage_id"
        )
        object.__setattr__(self, "parent_lineage_id", normalized_parent)
        assert self.return_record is not None
        if self.return_record.ancestor_lineage_id != normalized_parent:
            raise InvalidLineage("return ancestor does not match lineage parent")
        path_ids = tuple(edge.edge_id for edge in self.edges)
        recorded_ids = (
            self.return_record.preserved_prefix_edge_ids
            + self.return_record.successor_edge_ids
        )
        if path_ids != recorded_ids:
            raise InvalidLineage("return metadata does not match lineage edge path")
        prefix_length = len(self.return_record.preserved_prefix_edge_ids)
        if prefix_length >= len(self.edges):
            raise InvalidLineage("return metadata has no successor path")
        if self.edges[prefix_length].input_state != self.return_record.return_anchor:
            raise InvalidLineage("successor path does not begin at return anchor")
        if self.return_record.challenged_edge_id in self.return_record.successor_edge_ids:
            raise InvalidLineage("challenged edge cannot be reused as successor")

    @classmethod
    def root(cls, edges: Sequence[LineageEdge]) -> "Lineage":
        return cls(tuple(edges))

    def to_body(self) -> Dict[str, Any]:
        return {
            "edges": [edge.to_record() for edge in self.edges],
            "parent_lineage_id": self.parent_lineage_id,
            "return_record": (
                None if self.return_record is None else self.return_record.to_record()
            ),
        }

    @property
    def lineage_id(self) -> str:
        return _content_id("lineage", self.to_body())

    def to_record(self) -> Dict[str, JsonValue]:
        return _record("lineage", self.to_body())

    @property
    def canonical_hash(self) -> str:
        return hashlib.sha256(canonical_serialize(self)).hexdigest()

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> "Lineage":
        body = _verified_body(record, "lineage")
        if set(body) != {"edges", "parent_lineage_id", "return_record"}:
            raise IdentityMismatch("lineage body fields differ from schema")
        if not isinstance(body["edges"], list) or not all(
            isinstance(item, Mapping) for item in body["edges"]
        ):
            raise IdentityMismatch("lineage edges must be edge records")
        edges = tuple(LineageEdge.from_record(item) for item in body["edges"])
        return_record_value = body["return_record"]
        if return_record_value is not None and not isinstance(
            return_record_value, Mapping
        ):
            raise IdentityMismatch("lineage return record must be an object or null")
        value = cls(
            edges,
            (
                None
                if body["parent_lineage_id"] is None
                else str(body["parent_lineage_id"])
            ),
            (
                None
                if return_record_value is None
                else ReturnRecord.from_record(return_record_value)
            ),
        )
        if value.lineage_id != record["id"]:
            raise IdentityMismatch("lineage id failed reconstruction")
        return value


def canonical_serialize(value: Any) -> bytes:
    """Return deterministic UTF-8 JSON bytes for a lineage value or JSON value."""

    if hasattr(value, "to_record"):
        return _canonical_bytes(value.to_record())
    return _canonical_bytes(value)


def challenge(
    lineage: Lineage,
    target_edge_id: str,
    evidence: Any,
    created_provenance: Any,
) -> Challenge:
    """CHALLENGE one exact edge without mutating its lineage."""

    matches = [edge for edge in lineage.edges if edge.edge_id == target_edge_id]
    if len(matches) != 1:
        raise TargetNotFound("target edge is not uniquely present in target lineage")
    return Challenge(
        lineage.lineage_id,
        target_edge_id,
        CanonicalPayload(evidence),
        CanonicalPayload(created_provenance),
    )


def return_successor(
    ancestor: Lineage,
    challenge_record: Challenge,
    successor_path: Sequence[LineageEdge],
) -> Lineage:
    """RETURN to the challenged edge input and construct a new successor path."""

    if challenge_record.target_lineage_id != ancestor.lineage_id:
        raise InvalidReturn("challenge targets a different lineage")
    matching_indices = [
        index
        for index, edge in enumerate(ancestor.edges)
        if edge.edge_id == challenge_record.target_edge_id
    ]
    if len(matching_indices) != 1:
        raise InvalidReturn("challenge does not target one exact ancestor edge")
    challenged_index = matching_indices[0]
    challenged_edge = ancestor.edges[challenged_index]
    successor = tuple(successor_path)
    if not successor:
        raise InvalidReturn("successor path must not be empty")
    try:
        _validate_edge_path(successor)
    except InvalidLineage as error:
        raise InvalidReturn(str(error)) from error
    anchor = challenged_edge.input_state
    if successor[0].input_state != anchor:
        raise InvalidReturn("successor first input does not equal return anchor")
    ancestor_ids = {edge.edge_id for edge in ancestor.edges}
    collisions = ancestor_ids.intersection(edge.edge_id for edge in successor)
    if collisions:
        raise InvalidReturn("successor path reuses an immutable ancestor edge id")
    if successor[0].operator.operator_id == challenged_edge.operator.operator_id:
        raise InvalidReturn("first successor must use a new operator realization")

    prefix = ancestor.edges[:challenged_index]
    record = ReturnRecord(
        ancestor.lineage_id,
        challenged_edge.edge_id,
        challenge_record.challenge_id,
        challenge_record.evidence_id,
        anchor,
        tuple(edge.edge_id for edge in prefix),
        tuple(edge.edge_id for edge in successor),
    )
    return Lineage(prefix + successor, ancestor.lineage_id, record)


def audit(lineage: Lineage) -> Dict[str, Any]:
    """AUDIT a lineage as a detached structured view with explicit ancestry."""

    edge_views: List[Dict[str, Any]] = []
    for index, edge in enumerate(lineage.edges):
        edge_views.append(
            {
                "constraints": edge.constraints.to_value(),
                "constraints_id": edge.constraints.value_id,
                "edge_id": edge.edge_id,
                "evidence": edge.evidence.to_value(),
                "evidence_id": edge.evidence.value_id,
                "input_state": edge.input_state,
                "operator_identity": edge.operator.identifier,
                "operator_metadata": edge.operator.metadata.to_value(),
                "operator_realization_id": edge.operator.operator_id,
                "output_state": edge.output_state,
                "position": index,
                "predecessor_edge_id": (
                    None if index == 0 else lineage.edges[index - 1].edge_id
                ),
                "provenance": edge.provenance.to_value(),
                "provenance_id": edge.provenance.value_id,
                "successor_edge_id": (
                    None
                    if index + 1 == len(lineage.edges)
                    else lineage.edges[index + 1].edge_id
                ),
            }
        )

    ancestry: Optional[Dict[str, Any]] = None
    if lineage.return_record is not None:
        ancestry = {
            "ancestor_lineage_id": lineage.return_record.ancestor_lineage_id,
            "challenge_evidence_id": lineage.return_record.challenge_evidence_id,
            "challenge_id": lineage.return_record.challenge_id,
            "challenged_edge_id": lineage.return_record.challenged_edge_id,
            "preserved_prefix_edge_ids": list(
                lineage.return_record.preserved_prefix_edge_ids
            ),
            "return_anchor": lineage.return_record.return_anchor,
            "return_record_id": lineage.return_record.return_id,
            "successor_edge_ids": list(lineage.return_record.successor_edge_ids),
        }

    return {
        "ancestry": ancestry,
        "canonical_hash": lineage.canonical_hash,
        "lineage_id": lineage.lineage_id,
        "ordered_edges": edge_views,
        "parent_lineage_id": lineage.parent_lineage_id,
        "state_transitions": [
            {
                "edge_id": edge.edge_id,
                "from": edge.input_state,
                "operator_identity": edge.operator.identifier,
                "operator_realization_id": edge.operator.operator_id,
                "to": edge.output_state,
            }
            for edge in lineage.edges
        ],
    }
