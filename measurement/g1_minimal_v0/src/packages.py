from .null import N, NULL_MATCH_COORDINATES, NULL_TOLERANCES


def _singleton_direction(direction: set[str]) -> str:
    if direction not in ({"c_A"}, {"c_B"}):
        raise ValueError("direction must be exactly {'c_A'} or {'c_B'}")
    return next(iter(direction))


def treatment_package(evidence: dict, direction: set[str]) -> dict:
    """Structured treatment exposure S_specified^(1)."""
    return {
        "evidence": dict(evidence),
        "direction": _singleton_direction(direction),
    }


def null_package(evidence: dict) -> dict:
    """Structurally matched control exposure S_specified^(0)."""
    return {
        "evidence": N(evidence),
        "direction": None,
    }


def null_matches(treatment: dict, control: dict) -> bool:
    """Frozen structural comparison rule for the null package."""
    if set(treatment) != set(control):
        return False
    if set(treatment["evidence"]) != set(control["evidence"]):
        return False
    if control["direction"] is not None:
        return False

    t_e = treatment["evidence"]
    c_e = control["evidence"]
    for coord in NULL_MATCH_COORDINATES:
        tol = NULL_TOLERANCES[coord]
        if tol == "exact":
            if t_e[coord] != c_e[coord]:
                return False
        else:
            if abs(float(t_e[coord]) - float(c_e[coord])) > float(tol):
                return False
    return True
