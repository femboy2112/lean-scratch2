#!/usr/bin/env python3
"""Audit one report or source file for proof-boundary violations."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path


ALLOWED_LABELS = [
    "Verified Fact",
    "Computational Observation",
    "Not Established",
    "Withdrawn",
    "Patched",
    "Contradiction Detected",
    "Over-Upgraded",
    "Advisory Only",
]

FORBIDDEN_PATTERNS = [
    r"\bproves?\s+Collatz\b",
    r"\bproved\s+the\s+Collatz\s+conjecture\b",
    r"\bsolves?\s+the\s+Collatz\s+conjecture\b",
    r"\bessentially\s+proves?\s+Collatz\b",
    r"\bshows?\s+no\s+divergent\s+Collatz\s+orbits?\s+exist\b",
    r"\bspectral\s+radius\s+bound\s+solves?\s+the\s+conjecture\b",
]

WEAK_EXACTNESS_PATTERNS = [
    r"\bnumerical(?:ly)?\b.*\b(proves?|establishes?|shows?)\b",
    r"\bfloat(?:ing[- ]point)?\b.*\b(proves?|establishes?)\b",
    r"\bmodular\b.*\bpositive\s+for\s+all\s+real\b",
    r"\bone\s+slice\b.*\bgeneric\b",
]


def repo_root() -> Path:
    p = Path.cwd().resolve()
    for q in [p, *p.parents]:
        if (q / "CODEX.md").exists() and (q / "reports").exists():
            return q
    return p


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def line_findings(text: str, patterns: list[str], severity: str) -> list[dict]:
    out = []
    for i, line in enumerate(text.splitlines(), start=1):
        for pat in patterns:
            if re.search(pat, line, flags=re.IGNORECASE):
                out.append({"severity": severity, "line": i, "pattern": pat, "text": line.strip()})
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Report/source file to audit.")
    parser.add_argument("--out-prefix", default=None)
    args = parser.parse_args()

    root = repo_root()
    target = Path(args.path)
    if not target.is_absolute():
        target = root / target
    if not target.exists():
        raise SystemExit(f"Missing file: {target}")

    text = target.read_text(encoding="utf-8", errors="replace")
    findings = []
    findings += line_findings(text, FORBIDDEN_PATTERNS, "BLOCKER")
    findings += line_findings(text, WEAK_EXACTNESS_PATTERNS, "WARNING")

    label_hits = {label: text.count(label) for label in ALLOWED_LABELS}
    has_label = any(v > 0 for v in label_hits.values())

    if not has_label:
        findings.append({
            "severity": "WARNING",
            "line": None,
            "pattern": "missing allowed status label",
            "text": "No approved claim label found.",
        })

    if any(f["severity"] == "BLOCKER" for f in findings):
        disposition = "REJECT"
    elif findings:
        disposition = "PASS_WITH_PATCHES"
    else:
        disposition = "PASS"

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    slug = args.out_prefix or re.sub(r"[^a-zA-Z0-9]+", "_", target.stem).strip("_")[:80]
    reports = root / "reports"
    reports.mkdir(exist_ok=True)
    json_path = reports / f"{stamp}_{slug}_audit.json"
    md_path = reports / f"{stamp}_{slug}_audit.md"

    payload = {
        "disposition": disposition,
        "audited_file": str(target.relative_to(root) if target.is_relative_to(root) else target),
        "audited_sha256": sha256(target),
        "created_utc": stamp,
        "label_hits": label_hits,
        "findings": findings,
        "claim_boundary": "Audit checks proof-boundary language only; it does not prove mathematical claims.",
    }
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    md = [
        f"# Proof-Boundary Audit — {target.name}",
        "",
        f"- disposition: `{disposition}`",
        f"- audited_file: `{payload['audited_file']}`",
        f"- audited_sha256: `{payload['audited_sha256']}`",
        f"- created_utc: `{stamp}`",
        "- claim_boundary: audit only; no mathematical claim is upgraded",
        "",
        "## Label hits",
        "",
        "| Label | Count |",
        "|---|---:|",
    ]
    for label, count in label_hits.items():
        md.append(f"| {label} | {count} |")
    md += ["", "## Findings", ""]
    if findings:
        md += ["| Severity | Line | Finding |", "|---|---:|---|"]
        for f in findings:
            line = "" if f["line"] is None else str(f["line"])
            text_cell = f["text"].replace("|", "\\|")
            md.append(f"| {f['severity']} | {line} | `{f['pattern']}` — {text_cell} |")
    else:
        md.append("No proof-boundary violations detected by the pattern audit.")
    md += [
        "",
        "## Required next action",
        "",
        "If disposition is `PASS_WITH_PATCHES` or `REJECT`, patch the cited language and rerun this audit.",
        "",
    ]
    md_path.write_text("\n".join(md), encoding="utf-8")

    print(json.dumps({"ok": disposition == "PASS", "disposition": disposition, "markdown": str(md_path), "json": str(json_path)}, indent=2))
    return 0 if disposition in {"PASS", "PASS_WITH_PATCHES"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
