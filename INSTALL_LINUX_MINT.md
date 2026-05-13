# Linux Mint Install Notes

## Recommended path

Run:

```bash
bash scripts/setup_linux_mint.sh --sage auto
```

This does three things:

1. Installs system packages through `apt` when sudo is available.
2. Creates `.venv` and installs Python dependencies.
3. Installs or locates SageMath using this order:
   - existing `sage` on `PATH`;
   - `apt install sagemath` if your Mint/Ubuntu repositories provide it;
   - local conda-forge Sage environment at `.sage-conda` if apt has no candidate.

## Lighter Python-only path

```bash
bash scripts/setup_linux_mint.sh --sage skip
```

Use this first if you only want the fast Python checks and numerical probes.

## Why Sage may use Conda

Sage's own installation guide recommends conda-forge for Linux distributions that do not provide an up-to-date Sage package. The official Sage download page also says pre-built Linux binaries have been discontinued and points users to the installation guide.

## Disk/RAM warning

Sage is large. The Conda install can consume multiple GB. Use the Python-only path on constrained machines, then move heavy exact algebra to a stronger machine if needed.
