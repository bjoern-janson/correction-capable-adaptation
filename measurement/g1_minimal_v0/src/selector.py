def pi(s_selector: dict) -> str:
    """Intentionally trivial deterministic selector."""
    direction = s_selector.get("direction")
    if direction == "c_A":
        return "c_A"
    if direction == "c_B":
        return "c_B"
    return "c_A"
