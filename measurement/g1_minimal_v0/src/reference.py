def r(evidence: dict) -> set[str]:
    """Independent frozen reference (slightly different rule)."""
    sig = evidence["signal"]
    if sig == "strong_A":
        return {"c_A"}
    if sig == "strong_B":
        return {"c_B"}
    return {"c_A"}
