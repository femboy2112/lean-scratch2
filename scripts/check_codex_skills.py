#!/usr/bin/env python3
"""Validate project-scoped Codex skills have required structure."""
from __future__ import annotations

import json
import re
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

    result = {
        "ok": not any(f["severity"] == "BLOCKER" for f in findings),
        "skills_found": sorted(found),
        "findings": findings,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
