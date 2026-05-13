#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
if [[ ! -f "$ROOT/CODEX.md" ]]; then
  here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  ROOT="$(cd "$here/../../../.." && pwd)"
fi

cd "$ROOT"

echo "[orchestrator-preflight] root=$ROOT"
if [[ -x scripts/bootstrap_codex.sh || -f scripts/bootstrap_codex.sh ]]; then
  bash scripts/bootstrap_codex.sh
else
  echo "[orchestrator-preflight] missing scripts/bootstrap_codex.sh" >&2
  exit 1
fi

python scripts/check_codex_skills.py
echo "[orchestrator-preflight] ok"
