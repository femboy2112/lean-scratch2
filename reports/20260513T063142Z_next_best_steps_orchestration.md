# TDAP Orchestration Report — next best finite-level r=3 determinant and compact-factorization triage

- created_utc: `20260513T063142Z`
- status: `Advisory Only`
- scope: finite-level lifted-operator Collatz research only
- claim_boundary: no Collatz-level theorem is claimed or implied

## Target

Plan the next finite-level research cycle around r=3 determinant and compact-factorization triage, using existing exact S-level characteristic-polynomial closures at `s = 0.50`, `0.55`, and `0.60` as the starting evidence.

## Scope

- `Advisory Only`: select the next bounded research targets and commands.
- `Computational Observation`: cheap Python/SymPy reconnaissance and modular probes.
- `Verified Fact`: only exact Sage results with auditable witnesses and hashes.

## Out of scope

- Any Collatz-level theorem or implication.
- Any claim that finite-level spectral, determinant, or compact-factor evidence proves global orbit behavior.
- Any transfer of r=2 mechanisms to r=3 without an independent r=3 witness.

## Next Best Steps

1. Run the Tier 1 Python reconnaissance bundle to refresh r=3 spectral, modular determinant, factor-search, and cross-level observations.
2. Collect a witness manifest immediately after the Python run so every new report artifact is hash-addressed.
3. Promote only stable or contradictory patterns to Sage exact algebra, starting with `sage-r3-unit`; run `sage-r3-full` only if the unit result gives a concrete factor/determinant target.
4. Audit every generated report with the proof-boundary validator before updating canonical notes or Lean stubs.
5. If exact Sage produces a stable theorem candidate, generate a theorem-candidate note first; Lean stubs come only after the proof auditor classifies the claim as finite-level and exact.

## Recommended backends

- Sage exact algebra
- Python/SymPy reconnaissance
- proof-boundary audit

## Subtasks

### A. algebra_explorer

Priority: inspect r=3 unit/full determinant and factorization hypotheses after the refreshed Python probes. Search for exact symbolic structures, factorization hypotheses, quotient/residual decompositions, and invariant decompositions relevant to compact-factorization triage.

Backend: `Sage exact algebra if determinant/charpoly/rank/kernel is involved; otherwise Python exact prototypes.`

### B. experiment_runner

Priority: run bounded reconnaissance first: `spectral-fast`, `modular-unit-fast`, `modular-full-fast`, `factor-python`, then `cross-level`. Produce JSON/log artifacts and preserve return codes.

Backend: `Python orchestration with Sage when exact algebra is required.`

### C. proof_auditor

Classify all outputs using the claim ladder and block Collatz-level escalation.

Backend: `report-only plus optional Lean stub generation.`

### D. implementation_engineer

Patch scripts/tests if the target exposes missing harness functionality.

Backend: `Python/shell/pytest.`

## Suggested commands

```bash
env PATH=/tmp/codex-python-shim:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin bash .agents/skills/collatz-research-orchestrator/scripts/preflight.sh
env PATH=/tmp/codex-python-shim:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py spectral-fast
env PATH=/tmp/codex-python-shim:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py modular-unit-fast
env PATH=/tmp/codex-python-shim:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py modular-full-fast
env PATH=/tmp/codex-python-shim:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py factor-python
env PATH=/tmp/codex-python-shim:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py cross-level
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py
```

## Expected artifacts

- `reports/*_spectral-fast.log`
- `reports/*_spectral-fast_witness.json`
- `reports/*_modular-unit-fast_witness.json`
- `reports/*_modular-full-fast_witness.json`
- `reports/*_factor-python_witness.json`
- `reports/*_cross-level_witness.json`
- `reports/witness_manifest.json`
- Proof-boundary validator JSON printed to stdout, saved if the next execution pass needs a durable audit artifact.

## Blocked items

- `python` is not available as a command in the current shell. This pass used `/tmp/codex-python-shim/python -> /usr/bin/python3`; either keep that shim in the command environment or add a real Python alias before running repo scripts that call `python` internally.
- Sage exact work is not scheduled until the Python reconnaissance produces a concrete target or the user explicitly asks to spend the exact-algebra runtime.

## Next step

Run the Tier 1 command sequence above, collect the witness manifest, and audit the generated reports. If the refreshed observations show a stable determinant/factor pattern, promote the smallest exact target to `sage-r3-unit`.

## Subagent spawn prompt

Spawn four subagents: algebra_explorer, experiment_runner, proof_auditor, and implementation_engineer. Have each return commands run, files touched, artifacts, claim labels, and blockers. Consolidate only after all results return.

## Required proof-boundary pass

Run:

```bash
python .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py
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
Matplotlib created a temporary cache directory at /tmp/matplotlib-210343s5 because there was an issue with the default path (/home/leah/.config/matplotlib); it is highly recommended to set the MPLCONFIGDIR environment variable to a writable directory, in particular to speed up the import of Matplotlib and to better support multiprocessing.

```
