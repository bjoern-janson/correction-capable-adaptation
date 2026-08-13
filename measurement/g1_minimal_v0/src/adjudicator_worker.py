import json
import sys

from .adjudicator import q


def main() -> int:
    evidence = json.loads(sys.stdin.read())
    direction = q(evidence)
    sys.stdout.write(next(iter(direction)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
