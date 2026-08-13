"""Minimal immutable lineage and successor-construction primitives."""

from .lineage import (
    CanonicalizationError,
    Challenge,
    IdentityMismatch,
    InvalidLineage,
    InvalidReturn,
    Lineage,
    LineageEdge,
    LineageError,
    OperatorRef,
    ReturnRecord,
    TargetNotFound,
    audit,
    canonical_deserialize,
    canonical_serialize,
    challenge,
    return_successor,
)

__all__ = [
    "CanonicalizationError",
    "Challenge",
    "IdentityMismatch",
    "InvalidLineage",
    "InvalidReturn",
    "Lineage",
    "LineageEdge",
    "LineageError",
    "OperatorRef",
    "ReturnRecord",
    "TargetNotFound",
    "audit",
    "canonical_deserialize",
    "canonical_serialize",
    "challenge",
    "return_successor",
]
