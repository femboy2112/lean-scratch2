"""Canonical hashing helpers for witness artifacts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: str | Path) -> str:
    p = Path(path)
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_json_bytes(obj: Any) -> bytes:
    """Canonical compact JSON bytes used for deterministic artifact hashing."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_json(obj: Any) -> str:
    return sha256_bytes(canonical_json_bytes(obj))


def rational_pair(num: int, den: int = 1) -> list[int]:
    if den == 0:
        raise ZeroDivisionError("denominator cannot be zero")
    if den < 0:
        num, den = -num, -den
    return [int(num), int(den)]
