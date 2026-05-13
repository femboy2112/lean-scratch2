#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
if [[ -x .venv/bin/activate ]]; then
  . .venv/bin/activate
fi
python scripts/run_py_checks.py
pytest -q
python experiments/r3_spectral_probe.py --slices 0.50 0.55 0.60 --models unit full
python experiments/r3_modular_determinant_probe.py --model unit --samples 8
python experiments/r3_modular_determinant_probe.py --model full --samples 8
