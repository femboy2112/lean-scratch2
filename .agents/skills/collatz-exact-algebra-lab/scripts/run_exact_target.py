#!/usr/bin/env python3
"""Run known Collatz harness targets with logging and witness metadata."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


TARGETS = {
    "spectral-fast": {
        "cmd": ["python3", "experiments/r3_spectral_probe.py", "--slices", "0.50", "0.55", "0.60", "--models", "unit", "full"],
        "status": "Computational Observation",
        "method": "Python numerical/symbolic reconnaissance",
    },
    "modular-unit-fast": {
        "cmd": ["python3", "experiments/r3_modular_determinant_probe.py", "--model", "unit", "--samples", "4"],
        "status": "Computational Observation",
        "method": "Python modular determinant probe",
    },
    "modular-full-fast": {
        "cmd": ["python3", "experiments/r3_modular_determinant_probe.py", "--model", "full", "--samples", "4"],
        "status": "Computational Observation",
        "method": "Python modular determinant probe",
    },
    "factor-python": {
        "cmds": [
            ["python3", "experiments/r3_factor_search.py", "unit"],
            ["python3", "experiments/r3_factor_search.py", "full"],
        ],
        "status": "Computational Observation",
        "method": "Python/SymPy factor reconnaissance",
    },
    "cross-level": {
        "cmd": ["python3", "experiments/cross_level_invariance.py"],
        "status": "Computational Observation",
        "method": "Python cross-level invariant reconnaissance",
    },
    "sage-r2": {
        "cmd": ["sage", "sage/r2_verify_factorization.sage"],
        "status": "Verified Fact",
        "method": "Sage exact algebra",
        "requires_sage": True,
    },
    "sage-r3-unit": {
        "cmd": ["sage", "sage/r3_factorization_search.sage", "unit"],
        "status": "Computational Observation",
        "method": "Sage exact algebra factor search",
        "requires_sage": True,
    },
    "sage-r3-full": {
        "cmd": ["sage", "sage/r3_factorization_search.sage", "full"],
        "status": "Computational Observation",
        "method": "Sage exact algebra factor search",
        "requires_sage": True,
    },
}


def repo_root() -> Path:
    p = Path.cwd().resolve()
    for q in [p, *p.parents]:
        if (q / "CODEX.md").exists() and (q / "experiments").exists():
            return q
    raise SystemExit("Could not locate repo root")


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", choices=sorted(TARGETS))
    parser.add_argument("--no-run", action="store_true", help="Only write the planned command and witness skeleton.")
    args = parser.parse_args()

    root = repo_root()
    spec = TARGETS[args.target]
    reports = root / "reports"
    reports.mkdir(exist_ok=True)

    if spec.get("requires_sage") and not shutil.which("sage"):
        local_sage = root / ".sage-conda/bin/sage"
        if local_sage.exists():
            spec = dict(spec)
            spec["cmd"] = [str(local_sage), *spec["cmd"][1:]]
        else:
            raise SystemExit("Sage target requested but sage is not available. Run: bash scripts/bootstrap_codex.sh --with-sage")

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = f"{stamp}_{args.target}"
    log_path = reports / f"{base}.log"
    witness_path = reports / f"{base}_witness.json"
    md_path = reports / f"{base}_analysis.md"

    env = os.environ.copy()
    env["PYTHONPATH"] = str(root / "src") + os.pathsep + env.get("PYTHONPATH", "")
    env.setdefault("DOT_SAGE", str(root / ".codex" / "sage"))

    result = None
    if not args.no_run:
        commands = spec.get("cmds") or [spec["cmd"]]
        stdout_parts = []
        stderr_parts = []
        returncodes = []
        for cmd in commands:
            proc = subprocess.run(cmd, cwd=root, env=env, text=True, capture_output=True)
            returncodes.append(proc.returncode)
            stdout_parts.append("$ " + " ".join(cmd) + "\n" + proc.stdout)
            stderr_parts.append("$ " + " ".join(cmd) + "\n" + proc.stderr)
        stdout = "\n\n".join(stdout_parts)
        stderr = "\n\n".join(stderr_parts)
        log_path.write_text(
            "[stdout]\n" + stdout + "\n\n[stderr]\n" + stderr,
            encoding="utf-8",
        )
        result = {
            "returncode": max(returncodes) if returncodes else 0,
            "returncodes": returncodes,
            "stdout_tail": stdout[-4000:],
            "stderr_tail": stderr[-4000:],
        }
    else:
        commands = spec.get("cmds") or [spec["cmd"]]
        log_path.write_text(
            "\n".join("$ " + " ".join(cmd) for cmd in commands) + "\n\nNO RUN REQUESTED\n",
            encoding="utf-8",
        )
        result = {"returncode": None, "stdout_tail": "", "stderr_tail": "no-run"}

    input_hashes = {}
    for p in ["CODEX.md", "CLAIM_GUARDRAILS.md", "data/canonical_bundle/PROMPT.md"]:
        fp = root / p
        if fp.exists():
            input_hashes[p] = file_hash(fp)

    witness = {
        "status": spec["status"] if result["returncode"] in (0, None) else "Not Established",
        "target": args.target,
        "scope": "finite-level lifted-operator Collatz harness",
        "method": spec["method"],
        "claim_boundary": "This does not prove or imply the Collatz conjecture.",
        "reproduction_command": " && ".join(" ".join(cmd) for cmd in (spec.get("cmds") or [spec["cmd"]])),
        "input_hashes": input_hashes,
        "outputs": [str(log_path.relative_to(root))],
        "warnings": [] if result["returncode"] == 0 else ["command did not complete successfully or was not run"],
        "created_utc": stamp,
        "result": result,
    }
    witness_path.write_text(json.dumps(witness, indent=2), encoding="utf-8")

    md = f"""# Analysis Report — {args.target}

- status: `{witness['status']}`
- scope: {witness['scope']}
- method: {witness['method']}
- claim_boundary: {witness['claim_boundary']}
- reproduction_command: `{witness['reproduction_command']}`
- created_utc: `{stamp}`

## Result

Return code: `{result['returncode']}`

## Artifacts

- `{log_path.relative_to(root)}`
- `{witness_path.relative_to(root)}`

## stdout tail

```text
{result['stdout_tail']}
```

## stderr tail

```text
{result['stderr_tail']}
```
"""
    md_path.write_text(md, encoding="utf-8")

    print(json.dumps({"ok": result["returncode"] in (0, None), "analysis": str(md_path), "witness": str(witness_path), "log": str(log_path)}, indent=2))
    return 0 if result["returncode"] in (0, None) else result["returncode"]


if __name__ == "__main__":
    raise SystemExit(main())
