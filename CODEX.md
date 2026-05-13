# CODEX OPERATING INSTRUCTIONS

You are working inside a finite-level lifted-operator Collatz research repo.

## Start here

Run:

```bash
bash scripts/bootstrap_codex.sh
```

If the current task requires Sage exact algebra and `sage` is not found, run:

```bash
bash scripts/bootstrap_codex.sh --with-sage
```

If dependencies are missing, repair them by running:

```bash
bash scripts/setup_linux_mint.sh --sage auto
```

Do not silently skip failed dependency setup. If sudo is unavailable, fall back to the Python-only path and clearly mark Sage-dependent tasks as blocked.



## Installed Codex skills

This repo includes project-scoped skills under `.agents/skills/`.

Preferred workflow:

```text
1. $collatz-research-orchestrator
2. $collatz-exact-algebra-lab
3. $collatz-proof-boundary-auditor
4. /review using REVIEW_RULES.md
```

Validate skills:

```bash
python scripts/check_codex_skills.py
```

Use `CODEX_SKILLS.md` for explicit invocation prompts.


## Mandatory reading order

Read these before changing math code:

```text
data/canonical_bundle/PROMPT.md
data/canonical_bundle/01_FRAMEWORK_AND_CONVENTIONS.txt
data/canonical_bundle/02_LOCKED_BASELINE_THEOREMS.txt
data/canonical_bundle/03_CONSTRUCTION_DATA.txt
data/canonical_bundle/06_MATHEMATICAL_CONSTRAINTS.txt
data/canonical_bundle/07_INTERPRETATION_AND_BOUNDARIES.txt
```

Use files 04, 05, and 08 for closure/reconnaissance details.

## Do not invent missing math

If a construction detail is not in the bundle, do not guess it. Either derive it directly from a stated rule or mark the task blocked.

## Current open targets

1. r=3 compact factorization.
2. r=3 structural mechanism.
3. r=3 subdominant spectral structure.
4. r=3 determinant nonvanishing for all real `s > 0`.
5. r=3 exact determinant polynomials.
6. cross-level r=2/r=3 spectral invariance.
7. proof-boundary clarification for what finite-level facts can and cannot imply.

## Output requirements

Every report must state:

```text
status: Verified Fact | Computational Observation | Not Established | Withdrawn | Patched | Contradiction Detected | Over-Upgraded | Advisory Only
scope: exact level/model/slice or exploratory range
method: Python/SymPy, Sage, modular probe, numerical probe, proof sketch, etc.
claim_boundary: what this does NOT establish
reproduction_command: exact command used
```

## Hard stop conditions

Stop and flag contradiction if a result conflicts with:

- r=2 locked Perron values.
- r=2 canonical exponent tables.
- r=3 `P_3 = 54` and `MOD = 81` construction rule.
- scaling exponents: unit r=2 `c^6`, full r=2 `c^9`, unit r=3 `c_3^18`, full r=3 `c_3^27`.
- negative descent-to-Q closures at s=0.55 or s=0.60.

## Preferred execution pattern

1. Run a cheap Python sanity check.
2. Run a small numerical or modular reconnaissance.
3. Promote only the most promising branch to Sage exact algebra.
4. Save machine-readable JSON first, Markdown summary second.
5. Label new results as Computational Observation unless an exact witness is generated and independently auditable.
