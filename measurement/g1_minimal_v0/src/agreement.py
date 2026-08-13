from data.domain import X
from data.oc_table import OC
from config.thresholds import GAMMA_FROZEN
from .evidence import g
from .adjudicator import q
from .reference import r


def agreement_rate() -> float:
    """Exact-equality agreement over all X, equally weighted; no ties occur."""
    matches = 0
    for x in X:
        evidence = g(OC[x])
        matches += int(q(evidence) == r(evidence))
    return matches / len(X)


def agreement_passes() -> bool:
    return agreement_rate() >= GAMMA_FROZEN
