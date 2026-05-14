# Codex Skills Installed in This Harness

This repo contains project-scoped skills under `.agents/skills/`.

## Core skills

### 1. `$collatz-research-orchestrator`

Use for active-plan execution, target decomposition, subagent routing, and consolidated reports.

Primary launch:

```text
$collatz-research-orchestrator go
```

`go` means: read `plans/ACTIVE_CODEX_PLAN.md`, execute the active mission packet, obey the publication addendum, commit safe results, push them to GitHub, and do not claim or imply a Collatz proof.

### 2. `$collatz-exact-algebra-lab`

Use for Python/Sage experiments, exact algebra, determinant probes, factor searches, spectrum analysis, and witness manifests.

```bash
python3 .agents/skills/collatz-exact-algebra-lab/scripts/run_exact_target.py spectral-fast
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
```

For Sage work in this repo, prefer explicit local Sage:

```bash
env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage <script>
```

### 3. `$collatz-proof-boundary-auditor`

Use whenever a report, theorem candidate, generated result, or patch proposal might overclaim.

```bash
python3 .agents/skills/collatz-proof-boundary-auditor/scripts/audit_report.py reports/<file>.md
```

## Specialized skills

### 4. `$collatz-provenance-reproducibility-lab`

Use for hash verification, manifest validation, artifact indexes, reproduction commands, witness manifests, bundle comparison, and audit-noise control.

### 5. `$collatz-canonical-curator`

Use for canonical insertion previews, diff previews, human checklists, rollback notes, and proof-boundary-safe canonical wording. It must not edit canonical bundle files unless the active packet explicitly authorizes it.

### 6. `$collatz-factor-structure-lab`

Use for r=3 S-level factor registries, residual characteristic polynomials, pairwise gcds, resultants, discriminants, substitution searches, quotient/residual relations, and factor-network graph artifacts.

### 7. `$collatz-symmetry-mechanism-lab`

Use for commutants, automorphisms, equitable partitions, projectors, idempotents, block decompositions, quotient matrices, and structural-mechanism candidate reports.

### 8. `$collatz-spectrum-determinant-lab`

Use for determinant target taxonomy, exact root-isolation attempts, Sturm/sign-chart work, factor-root tracking, subdominant spectral experiments, and specialization sweeps.

### 9. `$collatz-campaign-manager`

Use for long multi-phase missions, phase receipts, checkpointing, timeouts, resume/retry, skip-completed logic, and final program manifests.

### 10. `$collatz-lean-formalization-bridge`

Use only for audited finite-level theorem candidates. It converts exact finite-level statements into Lean stubs, proof-obligation tables, and formalization-readiness reports. Do not use it for exploratory or numerical claims.

### 11. `$collatz-red-team-reviewer`

Use for adversarial evidence review: recomputing hashes, checking scripts against reports, finding contradictions, and downgrading unsupported proof bridges.

## Recommended workflow

For large research campaigns:

```text
1. $collatz-research-orchestrator
2. $collatz-campaign-manager
3. $collatz-provenance-reproducibility-lab
4. $collatz-factor-structure-lab / $collatz-symmetry-mechanism-lab / $collatz-spectrum-determinant-lab
5. $collatz-canonical-curator, if canonical review artifacts are needed
6. $collatz-proof-boundary-auditor
7. $collatz-red-team-reviewer
8. $collatz-lean-formalization-bridge only after exact theorem candidates stabilize
```

## Boundary

All skills are finite-level research tools. None of them may claim or imply a proof of the Collatz conjecture from finite-level matrix facts.
