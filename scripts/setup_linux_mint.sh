#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SAGE_MODE="skip"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --sage=*)
      SAGE_MODE="${1#--sage=}"
      shift
      ;;
    --sage)
      if [[ $# -ge 2 && "$2" != --* ]]; then
        SAGE_MODE="$2"
        shift 2
      else
        SAGE_MODE="auto"
        shift
      fi
      ;;
    --help|-h)
      cat <<USAGE
Usage: bash scripts/setup_linux_mint.sh [--sage skip|auto|apt|conda]

Default: --sage skip
Recommended full setup: --sage auto
USAGE
      exit 0
      ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done

cd "$ROOT"

echo "[setup] root=$ROOT"
if [[ -r /etc/os-release ]]; then
  . /etc/os-release
  echo "[setup] detected OS: ${PRETTY_NAME:-unknown}"
fi

have_cmd() { command -v "$1" >/dev/null 2>&1; }

run_sudo() {
  if [[ "$(id -u)" -eq 0 ]]; then
    "$@"
  elif have_cmd sudo; then
    sudo "$@"
  else
    echo "[setup] sudo not available; cannot run: $*" >&2
    return 1
  fi
}

install_apt_basics() {
  if ! have_cmd apt-get; then
    echo "[setup] apt-get not found; skipping apt package installation"
    return 0
  fi
  echo "[setup] installing system packages via apt"
  run_sudo apt-get update
  run_sudo apt-get install -y \
    python3 python3-venv python3-pip git curl ca-certificates \
    build-essential pkg-config gfortran jq \
    libgmp-dev libmpfr-dev libmpc-dev
}

setup_venv() {
  echo "[setup] preparing Python virtual environment"
  python3 -m venv .venv
  . .venv/bin/activate
  python3 -m pip install --upgrade pip wheel setuptools
  python3 -m pip install -r requirements.txt
  python3 -m pip install -e .
  echo "[setup] Python environment ready: $ROOT/.venv"
}

apt_has_sage_candidate() {
  have_cmd apt-cache || return 1
  local candidate
  candidate="$(apt-cache policy sagemath 2>/dev/null | awk '/Candidate:/ {print $2}')"
  [[ -n "$candidate" && "$candidate" != "(none)" ]]
}

install_sage_apt() {
  if ! have_cmd apt-get; then
    echo "[setup] apt-get not available; cannot apt-install Sage" >&2
    return 1
  fi
  if ! apt_has_sage_candidate; then
    echo "[setup] apt has no sagemath candidate" >&2
    return 1
  fi
  echo "[setup] installing SageMath via apt"
  run_sudo apt-get install -y sagemath
}

ensure_sage() {
  if have_cmd sage; then
    echo "[setup] sage already found: $(command -v sage)"
    sage --version || true
    return 0
  fi

  case "$SAGE_MODE" in
    skip)
      echo "[setup] skipping Sage install (--sage skip)"
      ;;
    apt)
      install_sage_apt
      ;;
    conda)
      bash scripts/install_sage_conda.sh
      ;;
    auto)
      if apt_has_sage_candidate; then
        install_sage_apt || bash scripts/install_sage_conda.sh
      else
        bash scripts/install_sage_conda.sh
      fi
      ;;
    *)
      echo "[setup] unknown Sage mode: $SAGE_MODE" >&2
      exit 2
      ;;
  esac
}

install_apt_basics || echo "[setup] apt basics skipped/failed; continuing with local Python attempt"
setup_venv
ensure_sage

echo "[setup] done"
echo "[setup] activate Python: source .venv/bin/activate"
if [[ -x "$ROOT/.sage-conda/bin/sage" ]]; then
  echo "[setup] local Sage: $ROOT/.sage-conda/bin/sage"
fi
