def g(oc_entry: dict) -> dict:
    """Deterministic evidence constructor."""
    return {
        "signal": oc_entry["signal"],
        "noise": oc_entry["noise"],
        "format": "structured_v0",
    }
