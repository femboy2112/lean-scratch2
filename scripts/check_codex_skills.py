#!/usr/bin/env python3
"""Validate project-scoped Codex skills have required structure."""
from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path


FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


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


def validate_codex_agents(root: Path, findings: list[dict]) -> None:
    codex_dir = root / ".codex"
    config_path = codex_dir / "config.toml"
    agents_dir = codex_dir / "agents"
    if not config_path.exists() and not agents_dir.exists():
        return

    agent_files = set()
    if config_path.exists():
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
                rel = role_config.get("config_file")
                if not rel:
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

    if agents_dir.exists():
        agent_files.update(agents_dir.glob("*.toml"))

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


def main() -> int:
    root = repo_root()
    skills_dir = root / ".agents/skills"
    expected = {
        "collatz-research-orchestrator",
        "collatz-exact-algebra-lab",
        "collatz-proof-boundary-auditor",
    }
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
            if not desc:
                findings.append({"severity": "BLOCKER", "skill": skill.name, "message": "missing description in frontmatter"})
            elif len(desc) < 60:
                findings.append({"severity": "WARNING", "skill": skill.name, "message": "description may be too short for implicit matching"})
            for sub in ["references", "scripts", "agents"]:
                if not (skill / sub).exists():
                    findings.append({"severity": "WARNING", "skill": skill.name, "message": f"missing optional {sub}/ directory"})

    missing = sorted(expected - found)
    for name in missing:
        findings.append({"severity": "BLOCKER", "skill": name, "message": "expected skill not found"})

    validate_codex_agents(root, findings)

    result = {
        "ok": not any(f["severity"] == "BLOCKER" for f in findings),
        "skills_found": sorted(found),
        "findings": findings,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
