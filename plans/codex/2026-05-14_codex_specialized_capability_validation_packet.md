# Codex Mission Packet — Specialized Capability Validation

- **plan_id:** `2026-05-14_codex_specialized_capability_validation_packet`
- **status:** `Advisory Only`
- **purpose:** validate the new specialized Codex skills and agents without running heavy mathematics
- **scope:** capability validation only; no canonical files and no mathematical claims changed

## Mission

Validate that the specialized skill and agent layer loads, is documented, and maps cleanly to the r=3 deep research program.

## Required reads

```text
CODEX_SKILLS.md
CODEX_TASKS.md
.codex/config.toml
scripts/check_codex_skills.py
```

## Commands

```bash
python3 scripts/check_codex_skills.py
python3 scripts/run_py_checks.py
python3 scripts/build_specialized_codex_capabilities.py
python3 scripts/check_codex_skills.py
```

## Required outputs

```text
reports/<timestamp>_codex_capability_matrix.md
reports/<timestamp>_codex_capability_matrix.json
reports/<timestamp>_specialized_skills_validation.md
```

## Capability matrix requirements

The matrix must map current project needs to the new skill/agent layer:

```text
active plan execution -> collatz-campaign-manager / campaign_operator
exact Sage factor work -> collatz-factor-structure-lab / sage_factor_algebraist
residual/gcd/resultant work -> collatz-factor-structure-lab / factor_cartographer
canonical insert previews -> collatz-canonical-curator / canonical_curator
artifact hashes/indexes -> collatz-provenance-reproducibility-lab / provenance_librarian
commutants/projectors/symmetry -> collatz-symmetry-mechanism-lab / mechanism_hunter
determinant root isolation -> collatz-spectrum-determinant-lab / determinant_root_analyst
spectral tracking -> collatz-spectrum-determinant-lab / spectral_tracker
Lean bridge -> collatz-lean-formalization-bridge / formalization_engineer
adversarial review -> collatz-red-team-reviewer / red_team_skeptic
```

## Non-goals

Do not run heavy Sage algebra. Do not modify canonical files. Do not claim mathematical progress.

## Claim boundary

This packet validates Codex workflow capability only. It does not prove or imply any Collatz-level theorem.
