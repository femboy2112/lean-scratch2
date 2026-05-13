.PHONY: setup setup-sage bootstrap check test probe probe-fast sage-r2 skills-check skill-preflight audit-reports witness-manifest clean

setup:
	bash scripts/setup_linux_mint.sh --sage skip

setup-sage:
	bash scripts/setup_linux_mint.sh --sage auto

bootstrap:
	bash scripts/bootstrap_codex.sh

check:
	PYTHONPATH=src python scripts/run_py_checks.py

test:
	pytest -q

probe:
	PYTHONPATH=src python experiments/r3_spectral_probe.py --slices 0.50 0.55 0.60 --models unit full
	PYTHONPATH=src python experiments/r3_modular_determinant_probe.py --model unit --samples 20
	PYTHONPATH=src python experiments/r3_modular_determinant_probe.py --model full --samples 20

probe-fast:
	PYTHONPATH=src python experiments/r3_spectral_probe.py --slices 0.50 0.55 0.60 --models unit full
	PYTHONPATH=src python experiments/r3_modular_determinant_probe.py --model unit --samples 4
	PYTHONPATH=src python experiments/r3_modular_determinant_probe.py --model full --samples 4

sage-r2:
	sage sage/r2_verify_factorization.sage

clean:
	rm -rf reports/*.json reports/*.csv reports/*.md reports/*.txt reports/*.sageout reports/*.log .pytest_cache


skills-check:
	python scripts/check_codex_skills.py

skill-preflight:
	bash .agents/skills/collatz-research-orchestrator/scripts/preflight.sh

audit-reports:
	python .agents/skills/collatz-proof-boundary-auditor/scripts/validate_claim_ladder.py

witness-manifest:
	python .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py
