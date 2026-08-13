import json
from pathlib import Path
import subprocess
import sys

from data.oc_table import OC
from .evidence import g
from .packages import treatment_package, null_package
from .provenance import append_record
from .randomizer import assign_treatment
from .transport import serialize, deserialize, equivalent


APPARATUS_ROOT = Path(__file__).resolve().parents[1]
FROZEN_WORKER_ENV = {
    "PYTHONHASHSEED": "0",
    "PYTHONIOENCODING": "utf-8",
}


def _run_adjudicator(evidence: dict) -> set[str]:
    proc = subprocess.run(
        [sys.executable, "-m", "src.adjudicator_worker"],
        cwd=APPARATUS_ROOT,
        env=FROZEN_WORKER_ENV,
        input=json.dumps(evidence, sort_keys=True, separators=(",", ":")),
        text=True,
        capture_output=True,
        check=True,
    )
    direction = proc.stdout.strip()
    if direction not in {"c_A", "c_B"}:
        raise RuntimeError("adjudicator returned invalid direction")
    return {direction}


def _run_selector(message: bytes) -> str:
    proc = subprocess.run(
        [sys.executable, "-m", "src.selector_worker"],
        cwd=APPARATUS_ROOT,
        env=FROZEN_WORKER_ENV,
        input=message,
        capture_output=True,
        check=True,
    )
    selected = proc.stdout.decode("utf-8").strip()
    if selected not in {"c_A", "c_B"}:
        raise RuntimeError("selector returned invalid candidate")
    return selected


def run_unit(
    unit_id: str,
    x_id: str,
    seed: str,
    *,
    log_path: str | Path | None = None,
    previous_hash: str | None = None,
) -> tuple[dict, str | None]:
    """Run one fidelity-audit unit; both potential packages predate assignment."""
    evidence = g(OC[x_id])
    direction = _run_adjudicator(evidence)

    s1 = treatment_package(evidence, direction)
    s0 = null_package(evidence)

    treatment = assign_treatment(unit_id, seed)
    s_specified = s1 if treatment == 1 else s0

    message = serialize(s_specified)
    s_selector = deserialize(message)
    if not equivalent(s_specified, s_selector):
        raise RuntimeError("Gamma equivalence failed before selector invocation")

    selected = _run_selector(message)
    record = {
        "unit_id": unit_id,
        "x_id": x_id,
        "evidence": evidence,
        "direction": sorted(direction),
        "s1_specified": s1,
        "s0_specified": s0,
        "treatment": treatment,
        "s_selector": s_selector,
        "selected": selected,
    }

    new_hash = None
    if log_path is not None:
        if previous_hash is None:
            raise ValueError("previous_hash is required when log_path is supplied")
        new_hash = append_record(log_path, record, previous_hash)

    return record, new_hash
