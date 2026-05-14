# Specialized Skills Validation

status: Verified Fact
scope: capability validation only; no canonical files and no mathematical claims changed
method: `check_codex_skills.py`, `run_py_checks.py`, `build_specialized_codex_capabilities.py`, and final checker rerun
claim_boundary: This is a finite-level workflow capability validation. It does not prove or imply any Collatz-level theorem.
reproduction_command: python3 scripts/check_codex_skills.py && python3 scripts/run_py_checks.py && python3 scripts/build_specialized_codex_capabilities.py && python3 scripts/check_codex_skills.py
files_touched: `.agents/skills/*/.gitkeep` support placeholders, `.codex/agents/proof_auditor.toml`, `reports/py_sanity_checks.json`, and the reports listed below
artifacts_produced: `reports/20260514T070727Z_codex_capability_matrix.md`, `reports/20260514T070727Z_codex_capability_matrix.json`, `reports/20260514T070727Z_specialized_skills_validation.md`

## Result

- `Verified Fact`: all expected core and specialized skills are discoverable.
- `Verified Fact`: all expected configured agent role files are present.
- `Verified Fact`: final `python3 scripts/check_codex_skills.py` returned `ok: true` with an empty `findings` list.
- `Patched`: `.codex/agents/proof_auditor.toml` now states the explicit `Collatz-level` boundary phrase checked by the validator.
- `Patched`: optional support placeholder directories now exist for the specialized skills and for the orchestrator assets directory.

## Non-Goals

- No heavy Sage algebra was run.
- No canonical bundle files were modified.
- No mathematical claim was upgraded or changed.

## Capability Coverage

- `active plan execution` -> `collatz-campaign-manager` / `campaign_operator`; backend: Python/report orchestration; expected artifacts: phase manifests, checkpointing, resume/retry, final manifests.
- `exact Sage factor work` -> `collatz-factor-structure-lab` / `sage_factor_algebraist`; backend: Sage exact algebra; expected artifacts: QQ[t][y] and QQ(t)[y] exact factorization work.
- `residual/gcd/resultant work` -> `collatz-factor-structure-lab` / `factor_cartographer`; backend: Sage exact algebra plus report indexes; expected artifacts: factor registries, pairwise gcds, resultants, discriminants.
- `canonical insert previews` -> `collatz-canonical-curator` / `canonical_curator`; backend: report-only curation; expected artifacts: canonical insertion previews and rollback notes.
- `artifact hashes/indexes` -> `collatz-provenance-reproducibility-lab` / `provenance_librarian`; backend: Python/report provenance; expected artifacts: hash verification, artifact indexes, witness manifest hygiene.
- `commutants/projectors/symmetry` -> `collatz-symmetry-mechanism-lab` / `mechanism_hunter`; backend: Python/Sage structural search; expected artifacts: commutants, automorphisms, projectors, equitable partitions.
- `determinant root isolation` -> `collatz-spectrum-determinant-lab` / `determinant_root_analyst`; backend: Sage exact algebra; expected artifacts: Sturm/sign-chart attempts without positivity overclaim.
- `spectral tracking` -> `collatz-spectrum-determinant-lab` / `spectral_tracker`; backend: Python/SymPy plus exact artifact links; expected artifacts: factor-root ownership and subdominant spectral behavior tracking.
- `Lean bridge` -> `collatz-lean-formalization-bridge` / `formalization_engineer`; backend: Lean stubs/report-only proof obligations; expected artifacts: finite-level theorem stubs after exact witness audit.
- `adversarial review` -> `collatz-red-team-reviewer` / `red_team_skeptic`; backend: report-only recomputation and consistency checks; expected artifacts: source-artifact contradiction and overclaim detection.

## Blocked Items

None.
