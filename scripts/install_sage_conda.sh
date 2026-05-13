#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MINIFORGE_DIR="${MINIFORGE_DIR:-$ROOT/.miniforge3}"
SAGE_PREFIX="${SAGE_CONDA_PREFIX:-$ROOT/.sage-conda}"
INSTALLER="$ROOT/Miniforge3-$(uname)-$(uname -m).sh"
URL="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

cd "$ROOT"

have_cmd() { command -v "$1" >/dev/null 2>&1; }

if have_cmd sage; then
  echo "[sage-conda] sage already on PATH: $(command -v sage)"
  sage --version || true
  exit 0
fi

if [[ ! -x "$MINIFORGE_DIR/bin/conda" ]]; then
  echo "[sage-conda] downloading Miniforge installer"
  curl -L "$URL" -o "$INSTALLER"
  echo "[sage-conda] installing Miniforge into $MINIFORGE_DIR"
  bash "$INSTALLER" -b -p "$MINIFORGE_DIR"
fi

CONDA="$MINIFORGE_DIR/bin/conda"
if [[ ! -x "$CONDA" ]]; then
  echo "[sage-conda] conda executable missing after install: $CONDA" >&2
  exit 1
fi

if [[ ! -x "$SAGE_PREFIX/bin/sage" ]]; then
  echo "[sage-conda] creating Sage environment at $SAGE_PREFIX"
  "$CONDA" create -y -p "$SAGE_PREFIX" -c conda-forge sage python=3.11
else
  echo "[sage-conda] Sage environment already exists: $SAGE_PREFIX"
fi

cat > "$ROOT/activate_sage.sh" <<ACTIVATE
#!/usr/bin/env bash
source "$MINIFORGE_DIR/etc/profile.d/conda.sh"
conda activate "$SAGE_PREFIX"
ACTIVATE
chmod +x "$ROOT/activate_sage.sh"

echo "[sage-conda] done"
echo "[sage-conda] run Sage with: $SAGE_PREFIX/bin/sage"
echo "[sage-conda] or activate with: source activate_sage.sh"
