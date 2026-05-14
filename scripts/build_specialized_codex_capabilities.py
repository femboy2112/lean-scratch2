#!/usr/bin/env python3
"""Idempotent helper for the specialized Codex capability layer.

This script is intentionally conservative: it verifies and creates the expected
specialized skill/agent paths if they are absent, but it does not overwrite
existing hand-edited files by default. It is a maintenance aid for future skill
refreshes, not part of the mathematical research kernel.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SPECIALIZED_SKILLS = {
    "collatz-provenance-reproducibility-lab": "Artifact provenance, reproducibility, hash verification, manifest validation, artifact indexing, and rerun-script skill for the Collatz finite-level research repo. Use for generated data bundles, SHA-256 checks, witness manifests, reproduction commands, and audit-noise control.",
    "collatz-canonical-curator": "Canonical insertion preview and human-review curation skill. Use to prepare canonical patch proposals, diff previews, insertion checklists, canonical wording checks, rollback notes, and proof-boundary-safe canonical review packets without modifying canonical bundle files.",
    "collatz-factor-structure-lab": "Exact factor-structure analysis skill for r=3 Collatz S-level artifacts. Use for factor registries, residual characteristic polynomials, pairwise gcds, resultants, discriminants, quotient/residual relations, substitution searches, and factor-network graph artifacts over QQ[t][y] and QQ(t)[y].",
    "collatz-symmetry-mechanism-lab": "Structural-mechanism discovery skill for the Collatz r=3 finite-level matrix program. Use for commutants, automorphisms, equitable partitions, projectors, idempotents, block decompositions, quotient matrices, specialization-based mechanism hints, and structural-mechanism candidate reports.",
    "collatz-spectrum-determinant-lab": "Determinant and spectrum analysis skill for finite-level Collatz matrix artifacts. Use for determinant target taxonomy, root-isolation attempts, Sturm/sign-chart work, factor-root tracking, subdominant spectral experiments, specialization sweeps, and strict separation of numerical observations from exact claims.",
    "collatz-campaign-manager": "Multi-phase campaign execution skill for long Collatz research missions. Use for phase manifests, checkpointing, timeouts, resume/retry behavior, partial completion reports, skip-completed logic, and final program manifests.",
    "collatz-lean-formalization-bridge": "Lean formalization bridge for audited finite-level Collatz theorem candidates. Use to convert exact finite-level statements into Lean stubs, proof-obligation tables, dependency maps, and formalization-readiness reports. Do not use for exploratory or numerical claims.",
    "collatz-red-team-reviewer": "Adversarial verification skill for Collatz research artifacts. Use to red-team reports, recompute hashes, compare claims against source artifacts, scan for contradictions, identify unsupported proof bridges, and produce independent review reports.",
}

AGENT_FILES = {
    "sage_factor_algebraist.toml",
    "factor_cartographer.toml",
    "mechanism_hunter.toml",
    "determinant_root_analyst.toml",
    "spectral_tracker.toml",
    "canonical_curator.toml",
    "provenance_librarian.toml",
    "campaign_operator.toml",
    "formalization_engineer.toml",
    "red_team_skeptic.toml",
}


def ensure_text(path: Path, content: str) -> str:
    if path.exists():
        return "exists"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "created"


def skill_stub(name: str, description: str) -> str:
    title = name.replace("collatz-", "").replace("-", " ").title()
    return f"""---
name: {name}
description: {description}
---

# {title}

This is a specialized finite-level Collatz research skill. Preserve claim labels,
use exact evidence for theorem-grade statements, and never claim or imply a
Collatz-level theorem from finite-level matrix artifacts.
"""


def agent_stub(filename: str) -> str:
    role = filename.removesuffix(".toml")
    return f'''model_reasoning_effort = "high"
model_verbosity = "medium"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
developer_instructions = """
Purpose: Specialized Collatz finite-level research role: {role}.

Use exact evidence for theorem-grade finite-level claims. Preserve blockers and
failed commands. Never claim or imply a Collatz-level theorem.
"""
'''


def main() -> int:
    actions: list[tuple[str, str]] = []
    for name, desc in sorted(SPECIALIZED_SKILLS.items()):
        base = ROOT / ".agents" / "skills" / name
        actions.append((str((base / "SKILL.md").relative_to(ROOT)), ensure_text(base / "SKILL.md", skill_stub(name, desc))))
        for sub in ["references", "scripts", "assets"]:
            keep = base / sub / ".gitkeep"
            actions.append((str(keep.relative_to(ROOT)), ensure_text(keep, "")))
    for filename in sorted(AGENT_FILES):
        path = ROOT / ".codex" / "agents" / filename
        actions.append((str(path.relative_to(ROOT)), ensure_text(path, agent_stub(filename))))

    for path, status in actions:
        print(f"{status}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
