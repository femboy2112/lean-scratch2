"""Helpers for local canonical text bundle inspection."""

from __future__ import annotations

import re
from pathlib import Path

BUNDLE_DIR = Path(__file__).resolve().parents[2] / "data" / "canonical_bundle"


def canonical_files(bundle_dir: Path = BUNDLE_DIR) -> list[Path]:
    return sorted(p for p in bundle_dir.iterdir() if p.suffix in {".txt", ".md"})


def read_bundle_file(name: str, bundle_dir: Path = BUNDLE_DIR) -> str:
    return (bundle_dir / name).read_text(encoding="utf-8")


def section_map(bundle_dir: Path = BUNDLE_DIR) -> dict[str, tuple[str, int]]:
    """Map section IDs to (filename,line_number)."""
    out: dict[str, tuple[str, int]] = {}
    pattern = re.compile(r"^==SECTION::\s*([^=]+?)\s*==")
    for path in canonical_files(bundle_dir):
        for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            m = pattern.match(line)
            if m:
                out[m.group(1).strip()] = (path.name, idx)
    return out
