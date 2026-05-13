# Collatz Codex Research Harness v2

This ZIP is meant to be extracted at the root of your local repo. It gives Codex a concrete Python/Sage workspace for the finite-level lifted-operator Collatz program.

## First command on Linux Mint

```bash
bash scripts/setup_linux_mint.sh --sage auto
```

Then run:

```bash
bash scripts/bootstrap_codex.sh --with-sage
```

For a lighter first pass without Sage:

```bash
bash scripts/setup_linux_mint.sh --sage skip
bash scripts/bootstrap_codex.sh
```



## v2 addition — Codex skills

This version includes three project-scoped Codex skills:

```text
.agents/skills/collatz-research-orchestrator/
.agents/skills/collatz-exact-algebra-lab/
.agents/skills/collatz-proof-boundary-auditor/
```

Use them explicitly inside Codex:

```text
$collatz-research-orchestrator plan the next r=3 compact-factorization attack and spawn useful subagents.
$collatz-exact-algebra-lab run bounded Python/Sage probes and generate witness artifacts.
$collatz-proof-boundary-auditor audit the newest reports for over-upgraded claims.
```

Validate the skill installation:

```bash
python scripts/check_codex_skills.py
```

The repo also now includes:

```text
AGENTS.md                         Repo-level Codex operating rules
REVIEW_RULES.md                   Custom review instructions for /review
PLANS.md                          Execution-plan template
CODEX_SKILLS.md                   Usage guide for the three skills
.codex/config.toml                Optional project-scoped Codex configuration
.codex/agents/*.toml              Subagent role configs
.codex/prompts/*.md               Copy-paste launch prompts
```


## What this harness does

- Rebuilds the canonical finite-level `S(t)` matrices from the deterministic source rule.
- Verifies the r=2 locked exponent tables against the canonical text bundle.
- Regenerates r=3 unit/full exponent tables from the congruence rule.
- Provides numerical spectral probes labelled as **Computational Observation** only.
- Provides modular determinant probes for nonvanishing reconnaissance.
- Provides Sage scripts for exact characteristic-polynomial / factorization work.
- Keeps all Collatz-level claims out of scope unless a separate proof-boundary package is produced.

## Directory map

```text
CODEX.md                         Immediate instructions for Codex
CODEX_TASKS.md                   Research backlog and execution order
CLAIM_GUARDRAILS.md              Hard claim-status rules
data/canonical_bundle/           The nine canonical files + PROMPT.md
scripts/setup_linux_mint.sh      Deterministic Linux Mint setup
scripts/bootstrap_codex.sh       Smart bootstrap / dependency repair for Codex
scripts/install_sage_conda.sh    Conda-forge Sage installer fallback
scripts/run_py_checks.py         Fast construction sanity gates
experiments/                     Python reconnaissance scripts
sage/                            Sage exact-algebra scripts
src/collatz_codex_harness/       Reusable construction + report code
tests/                           pytest sanity checks
reports/                         Generated outputs
lean/                            Lean proof-spine placeholder, not primary engine
```

## Claim discipline

Every generated report must include one of the canonical labels:

- Verified Fact
- Computational Observation
- Not Established
- Withdrawn
- Patched
- Contradiction Detected
- Over-Upgraded
- Advisory Only

Default new outputs from this harness are **Computational Observation** until separately audited.

## Primary workflow

1. Run `scripts/bootstrap_codex.sh`.
2. Run `pytest`.
3. Use Python experiments for reconnaissance.
4. Use Sage scripts for exact algebra once a target is worth the cost.
5. Save outputs under `reports/`.
6. Do not edit `data/canonical_bundle/` unless explicitly preparing a canonical patch.

## Important limitation

Finite-level spectral closures, exact characteristic polynomials, determinant probes, and structural mechanisms do **not** prove the Collatz conjecture by themselves. Treat the connection to Collatz as construction-level only until a separate theorem bridges finite-level facts to a Collatz-level conclusion.
