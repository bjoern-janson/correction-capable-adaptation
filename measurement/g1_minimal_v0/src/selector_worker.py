import sys

from .selector import pi
from .transport import deserialize


def main() -> int:
    message = sys.stdin.buffer.read()
    package = deserialize(message)
    selected = pi(package)
    sys.stdout.write(selected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
