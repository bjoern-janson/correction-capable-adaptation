def q(evidence: dict) -> set[str]:
    """Adjudicator (intentionally imperfect)."""
    sig = evidence["signal"]
    if sig.endswith("_A"):
        return {"c_A"}
    if sig.endswith("_B"):
        return {"c_B"}
    return {"c_A"}
