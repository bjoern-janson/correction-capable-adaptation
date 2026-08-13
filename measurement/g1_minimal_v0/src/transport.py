import json


def serialize(package: dict) -> bytes:
    return json.dumps(
        package,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def deserialize(message: bytes) -> dict:
    return json.loads(message.decode("utf-8"))


def equivalent(s_spec: dict, s_sel: dict) -> bool:
    """Licensed Gamma-equivalence: exact structural equality after round-trip."""
    return s_spec == s_sel
