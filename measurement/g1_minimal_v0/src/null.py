def N(evidence: dict) -> dict:
    """Direction-independent neutral evidence payload."""
    return {
        "signal": "NEUTRAL",
        "noise": evidence["noise"],
        "format": evidence["format"],
    }


NULL_MATCH_COORDINATES = ["noise", "format"]
NULL_TOLERANCES = {"noise": 0.0, "format": "exact"}
