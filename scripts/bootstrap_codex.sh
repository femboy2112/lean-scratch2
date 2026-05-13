#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WITH_SAGE=0
for arg in "$@"; do
  case "$arg" in
    --with-sage) WITH_SAGE=1 ;;
    --help|-h)
      echo "Usage: bash scripts/bootstrap_codex.sh [--with-sage]"
      exit 0
      ;;
    *) echo "Unknown argument: $arg" >&2; exit 2 ;;
  esac
done

cd "$ROOT"

echo "[codex-bootstrap] root=$ROOT"

if [[ ! -x .venv/bin/python3 ]]; then
  echo "[codex-bootstrap] .venv missing; running Python-only setup first"
  bash scripts/setup_linux_mint.sh --sage skip
fi

. .venv/bin/activate

python3 - <<'PY'
missing=[]
for mod in ["sympy", "numpy", "pandas", "matplotlib", "rich", "yaml", "networkx"]:
    try:
        __import__(mod)
    except Exception:
        missing.append(mod)
if missing:
    raise SystemExit("missing Python modules: " + ", ".join(missing))
PY

python3 scripts/run_py_checks.py

if [[ -f scripts/check_codex_skills.py ]]; then
  python3 scripts/check_codex_skills.py
fi

if [[ "$WITH_SAGE" -eq 1 || "${CODEX_REQUIRE_SAGE:-0}" == "1" ]]; then
  if command -v sage >/dev/null 2>&1; then
    echo "[codex-bootstrap] sage found: $(command -v sage)"
  elif [[ -x "$ROOT/.sage-conda/bin/sage" ]]; then
    echo "[codex-bootstrap] local sage found: $ROOT/.sage-conda/bin/sage"
  else
    echo "[codex-bootstrap] Sage requested but missing; running auto Sage setup"
    bash scripts/setup_linux_mint.sh --sage auto
  fi
fi

echo "[codex-bootstrap] ready"
