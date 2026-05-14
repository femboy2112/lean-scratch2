# TDAP Orchestration Report — specialized capability validation

- created_utc: `20260514T070401Z`
- status: `Advisory Only`
- scope: finite-level lifted-operator Collatz research only
- out_of_scope: global Collatz conjecture proof or any claim that finite spectral closure implies global orbit behavior
- claim_boundary: no Collatz-level theorem is claimed or implied

## Recommended backends

- Python orchestration
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

## Expected artifacts

- `reports/<timestamp>_codex_specialized_capability_validation_orchestration.md`
- `reports/<timestamp>_codex_specialized_capability_validation_orchestration.json`
- `reports/<timestamp>_codex_capability_matrix.md`
- `reports/<timestamp>_codex_capability_matrix.json`
- `reports/<timestamp>_specialized_skills_validation.md`

## Blocked items

None at orchestration time.

## Next step

Run proof-boundary validation, then commit and push the safe capability-validation result set.
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
  "core_skills_expected": [
    "collatz-exact-algebra-lab",
    "collatz-proof-boundary-auditor",
    "collatz-research-orchestrator"
  ],
  "specialized_skills_expected": [
    "collatz-campaign-manager",
    "collatz-canonical-curator",
    "collatz-factor-structure-lab",
    "collatz-lean-formalization-bridge",
    "collatz-provenance-reproducibility-lab",
    "collatz-red-team-reviewer",
    "collatz-spectrum-determinant-lab",
    "collatz-symmetry-mechanism-lab"
  ],
  "skills_found": [
    "collatz-campaign-manager",
    "collatz-canonical-curator",
    "collatz-exact-algebra-lab",
    "collatz-factor-structure-lab",
    "collatz-lean-formalization-bridge",
    "collatz-proof-boundary-auditor",
    "collatz-provenance-reproducibility-lab",
    "collatz-red-team-reviewer",
    "collatz-research-orchestrator",
    "collatz-spectrum-determinant-lab",
    "collatz-symmetry-mechanism-lab"
  ],
  "configured_agents": [
    "algebra_explorer",
    "campaign_operator",
    "canonical_curator",
    "determinant_root_analyst",
    "experiment_runner",
    "factor_cartographer",
    "formalization_engineer",
    "implementation_engineer",
    "mechanism_hunter",
    "proof_auditor",
    "provenance_librarian",
    "red_team_skeptic",
    "sage_factor_algebraist",
    "spectral_tracker"
  ],
  "expected_agent_files": [
    "algebra_explorer.toml",
    "campaign_operator.toml",
    "canonical_curator.toml",
    "determinant_root_analyst.toml",
    "experiment_runner.toml",
    "factor_cartographer.toml",
    "formalization_engineer.toml",
    "implementation_engineer.toml",
    "mechanism_hunter.toml",
    "proof_auditor.toml",
    "provenance_librarian.toml",
    "red_team_skeptic.toml",
    "sage_factor_algebraist.toml",
    "spectral_tracker.toml"
  ],
  "findings": []
}
[codex-bootstrap] ready
{
  "ok": true,
  "core_skills_expected": [
    "collatz-exact-algebra-lab",
    "collatz-proof-boundary-auditor",
    "collatz-research-orchestrator"
  ],
  "specialized_skills_expected": [
    "collatz-campaign-manager",
    "collatz-canonical-curator",
    "collatz-factor-structure-lab",
    "collatz-lean-formalization-bridge",
    "collatz-provenance-reproducibility-lab",
    "collatz-red-team-reviewer",
    "collatz-spectrum-determinant-lab",
    "collatz-symmetry-mechanism-lab"
  ],
  "skills_found": [
    "collatz-campaign-manager",
    "collatz-canonical-curator",
    "collatz-exact-algebra-lab",
    "collatz-factor-structure-lab",
    "collatz-lean-formalization-bridge",
    "collatz-proof-boundary-auditor",
    "collatz-provenance-reproducibility-lab",
    "collatz-red-team-reviewer",
    "collatz-research-orchestrator",
    "collatz-spectrum-determinant-lab",
    "collatz-symmetry-mechanism-lab"
  ],
  "configured_agents": [
    "algebra_explorer",
    "campaign_operator",
    "canonical_curator",
    "determinant_root_analyst",
    "experiment_runner",
    "factor_cartographer",
    "formalization_engineer",
    "implementation_engineer",
    "mechanism_hunter",
    "proof_auditor",
    "provenance_librarian",
    "red_team_skeptic",
    "sage_factor_algebraist",
    "spectral_tracker"
  ],
  "expected_agent_files": [
    "algebra_explorer.toml",
    "campaign_operator.toml",
    "canonical_curator.toml",
    "determinant_root_analyst.toml",
    "experiment_runner.toml",
    "factor_cartographer.toml",
    "formalization_engineer.toml",
    "implementation_engineer.toml",
    "mechanism_hunter.toml",
    "proof_auditor.toml",
    "provenance_librarian.toml",
    "red_team_skeptic.toml",
    "sage_factor_algebraist.toml",
    "spectral_tracker.toml"
  ],
  "findings": []
}
[orchestrator-preflight] ok

```

### stderr
```text
/home/leah/.config/matplotlib is not a writable directory
Matplotlib created a temporary cache directory at /tmp/matplotlib-a8axwzct because there was an issue with the default path (/home/leah/.config/matplotlib); it is highly recommended to set the MPLCONFIGDIR environment variable to a writable directory, in particular to speed up the import of Matplotlib and to better support multiprocessing.

```