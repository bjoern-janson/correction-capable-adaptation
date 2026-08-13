import hashlib


def assign_treatment(unit_id: str, seed: str) -> int:
    """Prospective deterministic hash assignment using only licensed inputs."""
    h = hashlib.sha256(f"{seed}:{unit_id}".encode("utf-8")).hexdigest()
    return int(h, 16) % 2
