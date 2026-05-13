#!/usr/bin/env python3
"""Compare two output files by hash and optionally normalized JSON."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_json(path: Path) -> bytes:
    obj = json.loads(path.read_text(encoding="utf-8"))
    return json.dumps(obj, sort_keys=True, indent=2).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("left")
    parser.add_argument("right")
    parser.add_argument("--normalize-json", action="store_true")
    args = parser.parse_args()

    left = Path(args.left)
    right = Path(args.right)

    if args.normalize_json:
        lb = normalize_json(left)
        rb = normalize_json(right)
    else:
        lb = left.read_bytes()
        rb = right.read_bytes()

    result = {
        "left": str(left),
        "right": str(right),
        "left_sha256": sha256_bytes(lb),
        "right_sha256": sha256_bytes(rb),
        "equal": lb == rb,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["equal"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
