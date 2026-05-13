# TDAP Orchestration Report — r=3 compact factorization and determinant nonvanishing triage

- created_utc: `20260513T152142Z`
- status: `Advisory Only`
- scope: finite-level lifted-operator Collatz research only
- claim_boundary: no Collatz-level theorem is claimed or implied

## Recommended backends

- Sage exact algebra
- proof-boundary audit

## Subtasks

### A. algebra_explorer

Identify exact symbolic structures, factorization hypotheses, and invariant decompositions relevant to the target.

Backend: `Sage exact algebra if determinant/charpoly/rank/kernel is involved; otherwise Python exact prototypes.`

### B. experiment_runner

Run bounded Python/Sage experiments and produce witness JSON/CSV/log artifacts.

Backend: `Python orchestration with Sage when exact algebra is required.`

### C. proof_auditor

Classify all outputs using the claim ladder and block Collatz-level escalation.

Backend: `report-only plus optional Lean stub generation.`

### D. implementation_engineer

Patch scripts/tests if the target exposes missing harness functionality.

Backend: `Python/shell/pytest.`

## Suggested commands

```bash
bash scripts/bootstrap_codex.sh
python3 scripts/check_codex_skills.py
python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py spectral-fast
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py
```

## Subagent spawn prompt

Spawn four subagents: algebra_explorer, experiment_runner, proof_auditor, and implementation_engineer. Have each return commands run, files touched, artifacts, claim labels, and blockers. Consolidate only after all results return.

## Required proof-boundary pass

Run:

```bash
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py
```

## Preflight

Return code: `0`

### stdout
```text
[orchestrator-preflight] root=/home/leah/Collatz/lean-scratch2
[codex-bootstrap] root=/home/leah/Collatz/lean-scratch2
{
  "ok": true,
  "report": "/home/leah/Collatz/lean-scratch2/reports/py_sanity_checks.json",
  "payload_sha256": "923614c3cce18c352706f3e881e70b2155df37d29e7223fe2136e28502d3dca6"
}
{
  "ok": true,
  "skills_found": [
    "collatz-exact-algebra-lab",
    "collatz-proof-boundary-auditor",
    "collatz-research-orchestrator"
  ],
  "findings": []
}
[codex-bootstrap] ready
{
  "ok": true,
  "skills_found": [
    "collatz-exact-algebra-lab",
    "collatz-proof-boundary-auditor",
    "collatz-research-orchestrator"
  ],
  "findings": []
}
[orchestrator-preflight] ok

```

### stderr
```text
/home/leah/.config/matplotlib is not a writable directory
Matplotlib created a temporary cache directory at /tmp/matplotlib-hky8axdn because there was an issue with the default path (/home/leah/.config/matplotlib); it is highly recommended to set the MPLCONFIGDIR environment variable to a writable directory, in particular to speed up the import of Matplotlib and to better support multiprocessing.

```