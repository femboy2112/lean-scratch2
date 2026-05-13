# Codex Skills Installed in This Harness

This repo contains three project-scoped skills under `.agents/skills/`.

## 1. `$collatz-proof-boundary-auditor`

Use first whenever a report, theorem candidate, or generated result might be overclaiming.

Primary command examples:

```text
$collatz-proof-boundary-auditor audit reports/<file>.md and generate a patch list.
```

```bash
python .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/<file>.md
```

## 2. `$collatz-exact-algebra-lab`

Use for Python/Sage experiments, exact algebra, determinant probes, factor searches, and witness manifests.

Primary command examples:

```text
$collatz-exact-algebra-lab run a Sage-backed r=3 unit factorization search and report exact blockers.
```

```bash
python .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py spectral-fast
python .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

## 3. `$collatz-research-orchestrator`

Use for the full target-decomposition-attack-proof-boundary loop.

Primary command examples:

```text
$collatz-research-orchestrator choose the next useful target and spawn subagents for algebra, experiment, and proof audit.
```

```bash
python .agents/skills/collatz-research-orchestrator/scripts/orchestrate.py --target "r=3 compact factorization" --run-preflight
```

## Recommended order

1. Use the orchestrator to choose and decompose.
2. Use the exact algebra lab to run experiments and produce witnesses.
3. Use the proof-boundary auditor to classify claims.
4. Run `/review` with `REVIEW_RULES.md` before accepting meaningful changes.
