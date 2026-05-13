#!/usr/bin/env python3
"""Create a TDAP orchestration plan and report for a Collatz target."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path


def repo_root() -> Path:
    p = Path.cwd().resolve()
    for q in [p, *p.parents]:
        if (q / "CODEX.md").exists() and (q / "data/canonical_bundle").exists():
            return q
    raise SystemExit("Could not locate repo root containing CODEX.md and data/canonical_bundle")


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return s[:80] or "collatz_target"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run(cmd: list[str], root: Path) -> dict:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(root / "src") + os.pathsep + env.get("PYTHONPATH", "")
    proc = subprocess.run(cmd, cwd=root, env=env, text=True, capture_output=True)
    return {
        "cmd": cmd,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-4000:],
        "stderr": proc.stderr[-4000:],
    }


def classify_backend(target: str) -> list[str]:
    t = target.lower()
    backends = []
    if any(k in t for k in ["factor", "determinant", "charpoly", "rank", "kernel", "exact"]):
        backends.append("Sage exact algebra")
    if any(k in t for k in ["spectrum", "scan", "data", "invariance", "structural", "mechanism", "recon"]):
        backends.append("Python/SymPy reconnaissance")
    if any(k in t for k in ["lean", "formal", "theorem", "proof"]):
        backends.append("Lean formalization skeleton")
    if not backends:
        backends = ["Python orchestration", "proof-boundary audit"]
    if "proof-boundary audit" not in backends:
        backends.append("proof-boundary audit")
    return backends


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Finite-level research target.")
    parser.add_argument("--run-preflight", action="store_true", help="Run bootstrap and skill validation first.")
    parser.add_argument("--out-prefix", default=None, help="Optional report slug/prefix.")
    args = parser.parse_args()

    root = repo_root()
    reports = root / "reports"
    reports.mkdir(exist_ok=True)

    preflight = None
    if args.run_preflight:
        preflight = run(["bash", ".agents/skills/collatz-research-orchestrator/scripts/preflight.sh"], root)

    target = args.target.strip()
    slug = args.out_prefix or slugify(target)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = f"{stamp}_{slug}_orchestration"

    canonical = []
    for p in sorted((root / "data/canonical_bundle").glob("*")):
        if p.is_file():
            canonical.append({"file": str(p.relative_to(root)), "sha256": sha256(p), "bytes": p.stat().st_size})

    backends = classify_backend(target)
    subtasks = [
        {
            "id": "A",
            "owner_role": "algebra_explorer",
            "task": "Identify exact symbolic structures, factorization hypotheses, and invariant decompositions relevant to the target.",
            "backend": "Sage exact algebra if determinant/charpoly/rank/kernel is involved; otherwise Python exact prototypes.",
        },
        {
            "id": "B",
            "owner_role": "experiment_runner",
            "task": "Run bounded Python/Sage experiments and produce witness JSON/CSV/log artifacts.",
            "backend": "Python orchestration with Sage when exact algebra is required.",
        },
        {
            "id": "C",
            "owner_role": "proof_auditor",
            "task": "Classify all outputs using the claim ladder and block Collatz-level escalation.",
            "backend": "report-only plus optional Lean stub generation.",
        },
        {
            "id": "D",
            "owner_role": "implementation_engineer",
            "task": "Patch scripts/tests if the target exposes missing harness functionality.",
            "backend": "Python/shell/pytest.",
        },
    ]

    suggested_commands = [
        "bash scripts/bootstrap_codex.sh",
        "python3 scripts/check_codex_skills.py",
        "python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py spectral-fast",
        "python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py",
        "python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py",
    ]

    data = {
        "target": target,
        "created_utc": stamp,
        "scope": "finite-level lifted-operator Collatz research only",
        "out_of_scope": "global Collatz conjecture proof or any claim that finite spectral closure implies global orbit behavior",
        "recommended_backends": backends,
        "canonical_inputs": canonical,
        "subtasks": subtasks,
        "suggested_commands": suggested_commands,
        "subagent_spawn_prompt": (
            "Spawn four subagents: algebra_explorer, experiment_runner, proof_auditor, "
            "and implementation_engineer. Have each return commands run, files touched, artifacts, "
            "claim labels, and blockers. Consolidate only after all results return."
        ),
        "preflight": preflight,
    }

    json_path = reports / f"{base}.json"
    md_path = reports / f"{base}.md"
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    md = [
        f"# TDAP Orchestration Report — {target}",
        "",
        f"- created_utc: `{stamp}`",
        "- status: `Advisory Only`",
        "- scope: finite-level lifted-operator Collatz research only",
        "- claim_boundary: no Collatz-level theorem is claimed or implied",
        "",
        "## Recommended backends",
        "",
        *[f"- {b}" for b in backends],
        "",
        "## Subtasks",
        "",
    ]
    for task in subtasks:
        md += [
            f"### {task['id']}. {task['owner_role']}",
            "",
            task["task"],
            "",
            f"Backend: `{task['backend']}`",
            "",
        ]
    md += [
        "## Suggested commands",
        "",
        "```bash",
        *suggested_commands,
        "```",
        "",
        "## Subagent spawn prompt",
        "",
        data["subagent_spawn_prompt"],
        "",
        "## Required proof-boundary pass",
        "",
        "Run:",
        "",
        "```bash",
        "python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py",
        "```",
        "",
    ]
    if preflight is not None:
        md += [
            "## Preflight",
            "",
            f"Return code: `{preflight['returncode']}`",
            "",
            "### stdout",
            "```text",
            preflight["stdout"],
            "```",
            "",
            "### stderr",
            "```text",
            preflight["stderr"],
            "```",
        ]

    md_path.write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({"ok": True, "markdown": str(md_path), "json": str(json_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
