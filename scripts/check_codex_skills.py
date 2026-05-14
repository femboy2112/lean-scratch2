#!/usr/bin/env python3
"""Validate project-scoped Codex skills and agent role configs.

This checker intentionally validates both the original core skills and the
specialized finite-level Collatz research skills. Optional support directories
are warnings, not blockers, because some skills are prompt-first while others
also ship helper scripts/assets.
"""
from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path


FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

CORE_SKILLS = {
    "collatz-research-orchestrator",
    "collatz-exact-algebra-lab",
    "collatz-proof-boundary-auditor",
}

SPECIALIZED_SKILLS = {
    "collatz-provenance-reproducibility-lab",
    "collatz-canonical-curator",
    "collatz-factor-structure-lab",
    "collatz-symmetry-mechanism-lab",
    "collatz-spectrum-determinant-lab",
    "collatz-campaign-manager",
    "collatz-lean-formalization-bridge",
    "collatz-red-team-reviewer",
}

EXPECTED_AGENT_FILES = {
    "algebra_explorer.toml",
    "experiment_runner.toml",
    "proof_auditor.toml",
    "implementation_engineer.toml",
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


def repo_root() -> Path:
    p = Path.cwd().resolve()
    for q in [p, *p.parents]:
        if (q / "CODEX.md").exists():
            return q
    return p


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def validate_codex_agents(root: Path, findings: list[dict]) -> list[str]:
    codex_dir = root / ".codex"
    config_path = codex_dir / "config.toml"
    agents_dir = codex_dir / "agents"
    agent_files = set()
    configured_agents: list[str] = []

    if not config_path.exists():
        findings.append({"severity": "BLOCKER", "path": ".codex/config.toml", "message": "missing Codex config"})
        return []

    try:
        config = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        findings.append({
            "severity": "BLOCKER",
            "path": str(config_path.relative_to(root)),
            "message": f"invalid TOML: {exc}",
        })
        config = {}

    agents = config.get("agents", {})
    if isinstance(agents, dict):
        for role, role_config in sorted(agents.items()):
            if not isinstance(role_config, dict):
                continue
            configured_agents.append(role)
            rel = role_config.get("config_file")
            if not rel:
                findings.append({
                    "severity": "BLOCKER",
                    "agent": role,
                    "message": "missing config_file in .codex/config.toml",
                })
                continue
            path = codex_dir / rel
            agent_files.add(path)
            if not path.exists():
                findings.append({
                    "severity": "BLOCKER",
                    "agent": role,
                    "path": str(path.relative_to(root)),
                    "message": "agent config_file target missing",
                })

        max_threads = agents.get("max_threads")
        if isinstance(max_threads, int) and max_threads < 6:
            findings.append({
                "severity": "WARNING",
                "path": str(config_path.relative_to(root)),
                "message": "max_threads < 6; specialized research campaigns may underuse subagents",
            })

    if agents_dir.exists():
        agent_files.update(agents_dir.glob("*.toml"))
    else:
        findings.append({"severity": "BLOCKER", "path": ".codex/agents", "message": "missing agent config directory"})

    existing_agent_names = {p.name for p in agent_files if p.exists()}
    for missing in sorted(EXPECTED_AGENT_FILES - existing_agent_names):
        findings.append({
            "severity": "BLOCKER",
            "path": f".codex/agents/{missing}",
            "message": "expected agent config missing",
        })

    for path in sorted(agent_files):
        if not path.exists():
            continue
        rel = str(path.relative_to(root))
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            findings.append({"severity": "BLOCKER", "path": rel, "message": f"invalid TOML: {exc}"})
            continue
        if "model_context" in data:
            findings.append({
                "severity": "BLOCKER",
                "path": rel,
                "message": "Codex agent role files do not support model_context; use developer_instructions",
            })
        instructions = data.get("developer_instructions")
        if not isinstance(instructions, str) or not instructions.strip():
            findings.append({
                "severity": "BLOCKER",
                "path": rel,
                "message": "missing non-empty developer_instructions",
            })
        if "Collatz-level" not in instructions and "Collatz" in instructions:
            findings.append({
                "severity": "WARNING",
                "path": rel,
                "message": "agent instructions may be missing explicit Collatz-level boundary language",
            })

    return configured_agents


def main() -> int:
    root = repo_root()
    skills_dir = root / ".agents/skills"
    expected = CORE_SKILLS | SPECIALIZED_SKILLS
    findings = []
    found = set()

    if not skills_dir.exists():
        findings.append({"severity": "BLOCKER", "message": "missing .agents/skills directory"})
    else:
        for skill in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
            skill_md = skill / "SKILL.md"
            if not skill_md.exists():
                findings.append({"severity": "BLOCKER", "skill": skill.name, "message": "missing SKILL.md"})
                continue
            meta = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
            name = meta.get("name")
            desc = meta.get("description")
            if not name:
                findings.append({"severity": "BLOCKER", "skill": skill.name, "message": "missing name in frontmatter"})
            else:
                found.add(name)
                if name != skill.name:
                    findings.append({
                        "severity": "BLOCKER",
                        "skill": skill.name,
                        "message": f"frontmatter name {name!r} does not match directory name",
                    })
            if not desc:
                findings.append({"severity": "BLOCKER", "skill": skill.name, "message": "missing description in frontmatter"})
            elif len(desc) < 60:
                findings.append({"severity": "WARNING", "skill": skill.name, "message": "description may be too short for implicit matching"})
            for sub in ["references", "scripts", "assets"]:
                if not (skill / sub).exists():
                    findings.append({"severity": "WARNING", "skill": skill.name, "message": f"missing optional {sub}/ directory"})

    missing = sorted(expected - found)
    for name in missing:
        findings.append({"severity": "BLOCKER", "skill": name, "message": "expected skill not found"})

    configured_agents = validate_codex_agents(root, findings)

    result = {
        "ok": not any(f["severity"] == "BLOCKER" for f in findings),
        "core_skills_expected": sorted(CORE_SKILLS),
        "specialized_skills_expected": sorted(SPECIALIZED_SKILLS),
        "skills_found": sorted(found),
        "configured_agents": configured_agents,
        "expected_agent_files": sorted(EXPECTED_AGENT_FILES),
        "findings": findings,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
