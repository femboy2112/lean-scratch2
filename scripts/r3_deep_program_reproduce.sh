#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

STAMP="${1:-$(date -u +%Y%m%dT%H%M%SZ)}"
SAGE_BIN="./.sage-conda/bin/sage"
export DOT_SAGE="$ROOT/.codex/sage"

python3 scripts/run_py_checks.py
"$SAGE_BIN" sage/r3_factor_structure_gcd.sage --timestamp "$STAMP"
"$SAGE_BIN" sage/r3_factor_relation_expansion.sage --timestamp "$STAMP"
python3 scripts/r3_deep_program_generate.py --timestamp "$STAMP"
python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
