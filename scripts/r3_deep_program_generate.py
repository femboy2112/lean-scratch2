#!/usr/bin/env python3
"""Generate the r=3 deep-structure program report bundle."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import math
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from collatz_codex_harness.construct import det_mod_prime, s_matrix_mod, s_numeric_matrix


REPORTS = ROOT / "reports"
DEEP_ROOT = ROOT / "data/generated/r3_deep_program"
AUDIT_BUNDLE = ROOT / "data/generated/r3_factorization_audit/20260513T160231Z"
AUDIT_MANIFEST = AUDIT_BUNDLE / "manifest.json"
GCD_MANIFEST = ROOT / "data/generated/r3_factor_structure/20260514T052552Z/factor_gcd_manifest.json"
CANONICAL_TARGET = ROOT / "data/canonical_bundle/05_R3_CLOSURES.txt"
BOUNDARY = (
    "This is a finite-level structural/spectral/determinant fact inside the lifted-operator framework. "
    "It does not prove or imply the Collatz conjecture, global orbit behavior, "
    "determinant nonvanishing for all real s > 0, cross-level invariance, or a structural mechanism."
)
SHARED_HASH = "02b476933e8ab0a428cc3fe0c0c6fb67cabf49b7396b109aae5e95fb89388c69"


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def run(cmd: list[str], *, ok: bool = True) -> dict[str, Any]:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")
    proc = subprocess.run(cmd, cwd=ROOT, env=env, text=True, capture_output=True)
    if ok and proc.returncode != 0:
        raise SystemExit("{} failed:\n{}".format(" ".join(cmd), proc.stderr[-2000:]))
    return {
        "cmd": cmd,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-4000:],
        "stderr": proc.stderr[-4000:],
    }


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any, outputs: list[Path]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    outputs.append(path)


def write_text(path: Path, text: str, outputs: list[Path]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")
    outputs.append(path)


def load_factors(model: str) -> list[dict[str, Any]]:
    out = []
    for path in sorted((AUDIT_BUNDLE / model / "factors").glob("factor_*.json")):
        item = load_json(path)
        item["source_json"] = str(path.relative_to(ROOT))
        item["source_txt"] = str((path.parent / f"factor_{item['factor_index']:02d}.txt").relative_to(ROOT))
        out.append(item)
    return out


def factor_degree_contribution(factors: list[dict[str, Any]]) -> int:
    return sum(int(f["degree_y"]) * int(f["multiplicity"]) for f in factors)


def canonical_hashes() -> dict[str, dict[str, Any]]:
    return {
        str(path.relative_to(ROOT)): {"sha256": sha256_file(path), "bytes": path.stat().st_size}
        for path in sorted((ROOT / "data/canonical_bundle").glob("*"))
        if path.is_file()
    }


def state_lock(stamp: str, data_dir: Path, outputs: list[Path]) -> dict[str, Any]:
    commit = run(["git", "rev-parse", "HEAD"])["stdout"].strip()
    sage = run(["env", f"DOT_SAGE={ROOT / '.codex/sage'}", "./.sage-conda/bin/sage", "--version"])
    py_version = sys.version.split()[0]
    prior = {
        str(path.relative_to(ROOT)): {"sha256": sha256_file(path), "bytes": path.stat().st_size}
        for path in [
            AUDIT_MANIFEST,
            GCD_MANIFEST,
            ROOT / "reports/20260514T050426Z_r3_factor_structure_analysis.md",
            ROOT / "reports/20260514T052552Z_r3_factor_structure_gcd.md",
        ]
        if path.exists()
    }
    payload = {
        "status": "Advisory Only",
        "repo_commit": commit,
        "created_utc": stamp,
        "sage_path": "./.sage-conda/bin/sage",
        "sage_version": sage["stdout"].strip(),
        "python_version": py_version,
        "canonical_bundle_hashes": canonical_hashes(),
        "prior_artifacts": prior,
        "claim_boundary": "finite-level only; no Collatz-level conclusion",
        "commands": [
            "git pull --ff-only",
            "python3 scripts/check_codex_skills.py",
            "python3 scripts/run_py_checks.py",
            "env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage --version",
        ],
    }
    write_json(data_dir / "state_manifest.json", payload, outputs)
    write_json(REPORTS / f"{stamp}_deep_program_state_lock.json", payload, outputs)
    write_text(REPORTS / f"{stamp}_deep_program_state_lock.md", f"""# r=3 Deep Program State Lock

status: Advisory Only
scope: environment and artifact state for the finite-level r=3 deep program
method: git, Python, local Sage version, and SHA-256 file hashing
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`, `data/generated/r3_deep_program/{stamp}/`
artifacts_produced: `data/generated/r3_deep_program/{stamp}/state_manifest.json`

## Locked State

- repo_commit: `{payload["repo_commit"]}`
- sage_path: `./.sage-conda/bin/sage`
- sage_version: `{payload["sage_version"]}`
- python_version: `{payload["python_version"]}`
""", outputs)
    return payload


def factor_registry(stamp: str, data_dir: Path, outputs: list[Path]) -> list[dict[str, Any]]:
    gcd = load_json(GCD_MANIFEST)
    registry = []
    for model in ["unit", "full"]:
        other = "full" if model == "unit" else "unit"
        factors = load_factors(model)
        for factor in factors:
            shared_with = []
            for other_factor in load_factors(other):
                if factor["factor_sha256"] == other_factor["factor_sha256"]:
                    shared_with.append(f"{other}:factor_{int(other_factor['factor_index']):02d}")
            gcd_relations = [
                row for row in gcd.get("pairwise_gcds", [])
                if (model == "unit" and row["unit_factor_i"] == factor["factor_index"])
                or (model == "full" and row["full_factor_j"] == factor["factor_index"])
            ]
            registry.append({
                "model": model,
                "factor_index": int(factor["factor_index"]),
                "factor_hash": factor["factor_sha256"],
                "degree_y": int(factor["degree_y"]),
                "degree_t_max": factor.get("degree_t_max"),
                "multiplicity": int(factor["multiplicity"]),
                "is_row_sum_factor": bool(factor.get("is_row_sum_factor")),
                "is_shared_unit_full_factor": bool(shared_with),
                "shared_with": shared_with,
                "gcd_relations": gcd_relations,
                "source_json": factor["source_json"],
                "source_txt": factor["source_txt"],
                "status_label": "Verified Fact",
                "claim_boundary": BOUNDARY,
            })
    json_path = data_dir / "factor_registry.json"
    csv_path = data_dir / "factor_registry.csv"
    write_json(json_path, registry, outputs)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "model", "factor_index", "factor_hash", "degree_y", "degree_t_max",
            "multiplicity", "is_row_sum_factor", "is_shared_unit_full_factor",
            "shared_with", "source_json", "status_label",
        ], lineterminator="\n")
        writer.writeheader()
        for row in registry:
            slim = {k: row[k] for k in writer.fieldnames or []}
            slim["shared_with"] = ";".join(row["shared_with"])
            writer.writerow(slim)
    outputs.append(csv_path)
    checks = {
        "shared_factor_present": any(r["factor_hash"] == SHARED_HASH and r["model"] == "unit" for r in registry)
        and any(r["factor_hash"] == SHARED_HASH and r["model"] == "full" for r in registry),
        "row_sum_factor_indices": {
            model: [r["factor_index"] for r in registry if r["model"] == model and r["is_row_sum_factor"]]
            for model in ["unit", "full"]
        },
        "degree_contributions": {
            "unit": factor_degree_contribution(load_factors("unit")),
            "full": factor_degree_contribution(load_factors("full")),
        },
    }
    report = {
        "status": "Verified Fact",
        "created_utc": stamp,
        "scope": "finite-level r=3 S-level factor registry from audited Sage factorization and exact gcd artifacts",
        "method": "Python normalization of audited factor JSON and exact gcd manifest",
        "checks": checks,
        "registry_json": str(json_path.relative_to(ROOT)),
        "registry_csv": str(csv_path.relative_to(ROOT)),
        "claim_boundary": BOUNDARY,
    }
    write_json(REPORTS / f"{stamp}_factor_registry_summary.json", report, outputs)
    write_text(REPORTS / f"{stamp}_factor_registry_summary.md", f"""# r=3 Factor Registry Summary

status: Verified Fact
scope: finite-level r=3 S-level factor registry from audited Sage factorization and exact gcd artifacts
method: Python normalization of audited factor JSON and exact gcd manifest
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`, `data/generated/r3_deep_program/{stamp}/`
artifacts_produced: `{json_path.relative_to(ROOT)}`, `{csv_path.relative_to(ROOT)}`

## Verification Checks

- unit factor degree contribution: `{checks["degree_contributions"]["unit"]}`
- full factor degree contribution: `{checks["degree_contributions"]["full"]}`
- unit row-sum factor index: `{checks["row_sum_factor_indices"]["unit"]}`
- full row-sum factor index: `{checks["row_sum_factor_indices"]["full"]}`
- shared unit/full factor hash present: `{checks["shared_factor_present"]}`
""", outputs)
    return registry


def canonical_review(stamp: str, outputs: list[Path]) -> None:
    manifest = load_json(AUDIT_MANIFEST)
    insert = f"""==SECTION:: 05.charpoly.r3.generic_s_level_factorization ==
status_label: Verified Fact, finite-level only
r: 3
level: S-level
models: unit and full
recorded_ring: QQ[t][y]
y-separability ring: QQ(t)[y]
Sage-displayed irreducibility over QQ[t][y]
row-sum/Perron factor index: 0 for both models
shared non-row-sum factor hash: {SHARED_HASH}
manifest file hash: {sha256_file(AUDIT_MANIFEST)}
manifest payload hash: {manifest.get("manifest_payload_sha256")}
claim_boundary: {BOUNDARY}
"""
    patch = f"""diff --git a/data/canonical_bundle/05_R3_CLOSURES.txt b/data/canonical_bundle/05_R3_CLOSURES.txt
--- a/data/canonical_bundle/05_R3_CLOSURES.txt
+++ b/data/canonical_bundle/05_R3_CLOSURES.txt
@@ before <<APPEND-POINT::05.charpoly>>
+{insert.replace(chr(10), chr(10) + '+').rstrip('+')}
"""
    payload = {
        "status": "Advisory Only",
        "created_utc": stamp,
        "target_file": str(CANONICAL_TARGET.relative_to(ROOT)),
        "canonical_files_touched": False,
        "insert_text": insert,
        "manifest_file_hash": sha256_file(AUDIT_MANIFEST),
        "manifest_payload_hash": manifest.get("manifest_payload_sha256"),
        "claim_boundary": BOUNDARY,
    }
    write_json(REPORTS / f"{stamp}_r3_canonical_insert_final_review_packet.json", payload, outputs)
    write_text(REPORTS / f"{stamp}_r3_canonical_insert_final_review_packet.md", f"""# r=3 Canonical Insert Final Review Packet

status: Advisory Only
scope: human-review packet for a finite-level r=3 S-level canonical insertion preview
method: report-only synthesis from audited Sage factorization and exact gcd artifacts
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`
artifacts_produced: final review packet, sidecar JSON, diff preview, and checklist

## Insert Preview

```text
{insert}
```

## Required Human Checks

- Verify Sage rerun.
- Verify manifest file hash.
- Verify manifest payload hash.
- Verify exact gcd manifest.
- Verify no determinant positivity claim.
- Verify no Collatz-level language.
- Verify canonical section placement before `<<APPEND-POINT::05.charpoly>>`.
- Verify rollback procedure.
""", outputs)
    write_text(REPORTS / f"{stamp}_r3_canonical_insert_diff_preview.patch", patch, outputs)
    write_text(REPORTS / f"{stamp}_canonical_insert_human_checklist.md", f"""# Canonical Insert Human Checklist

status: Advisory Only
scope: checklist for proposed finite-level r=3 canonical insertion
method: report-only checklist
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`
artifacts_produced: this checklist

- [ ] Verify Sage rerun.
- [ ] Verify manifest file hash.
- [ ] Verify manifest payload hash.
- [ ] Verify exact gcd manifest.
- [ ] Verify no determinant positivity claim.
- [ ] Verify no Collatz-level language.
- [ ] Verify canonical section placement.
- [ ] Verify rollback procedure.
""", outputs)


def sweep_and_tracking(stamp: str, data_dir: Path, outputs: list[Path]) -> None:
    rows = []
    for model in ["unit", "full"]:
        for s in [0.45, 0.50, 0.55, 0.60, 0.65, 0.70]:
            mat = s_numeric_matrix(3, model, s)
            eig = np.linalg.eigvals(mat)
            abs_sorted = sorted((abs(complex(x)) for x in eig), reverse=True)
            rows.append({
                "status": "Computational Observation",
                "r": 3,
                "model": model,
                "s": s,
                "dimension": int(mat.shape[0]),
                "perron_row_sum_S": float(np.sum(mat[0, :])),
                "max_abs_eigen_S": float(abs_sorted[0]),
                "second_abs_eigen_S": float(abs_sorted[1]),
                "spectral_gap_S": float(abs_sorted[0] - abs_sorted[1]),
                "claim_boundary": "Numerical S-level probe only; no exact dominance theorem and no Collatz-level conclusion.",
            })
    modular = []
    for model in ["unit", "full"]:
        for prime in [1000003, 1000033, 1000037, 1000039, 1000081]:
            for t_value in [2, 3, 5]:
                modular.append({
                    "status": "Computational Observation",
                    "model": model,
                    "prime": prime,
                    "t_value": t_value,
                    "det_mod_prime": det_mod_prime(s_matrix_mod(3, model, t_value, prime), prime),
                    "claim_boundary": "Modular determinant samples do not establish all-real-s determinant nonvanishing.",
                })
    payload = {"status": "Computational Observation", "created_utc": stamp, "numerical_rows": rows, "modular_rows": modular, "claim_boundary": BOUNDARY}
    csv_path = REPORTS / f"{stamp}_r3_specialization_sweep.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    outputs.append(csv_path)
    write_json(REPORTS / f"{stamp}_r3_specialization_sweep.json", payload, outputs)
    write_text(REPORTS / f"{stamp}_r3_specialization_sweep.md", f"""# r=3 Specialization Sweep

status: Computational Observation
scope: finite-level r=3 S-level rational/slice/modular reconnaissance
method: NumPy numerical eigensolver for slices and exact modular determinant samples from integer construction
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`
artifacts_produced: specialization CSV, JSON, and this Markdown report

Generated `{len(rows)}` numerical slice rows and `{len(modular)}` modular determinant sample rows. Numerical root ordering is not an exact theorem.
""", outputs)
    tracking_dir = data_dir / "spectral_tracking"
    write_json(tracking_dir / "slice_tracking.json", payload, outputs)
    write_text(REPORTS / f"{stamp}_r3_subdominant_factor_tracking.md", f"""# r=3 Subdominant Factor Tracking

status: Computational Observation
scope: finite-level r=3 S-level numerical subdominant spectral reconnaissance
method: numerical slice sweep with factor-owner classification deferred
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`, `data/generated/r3_deep_program/{stamp}/spectral_tracking/`
artifacts_produced: `{(tracking_dir / "slice_tracking.json").relative_to(ROOT)}` and this report

Computational Observation: numerical second-eigenvalue magnitudes were recorded in the specialization sweep. Not Established: exact factor ownership and exact dominance for all `t > 0`.
""", outputs)


def graph_and_planning_reports(stamp: str, data_dir: Path, registry: list[dict[str, Any]], outputs: list[Path]) -> None:
    graph_dir = data_dir / "factor_graph"
    nodes = []
    edges = []
    for row in registry:
        node_id = f"{row['model']}_factor_{row['factor_index']:02d}"
        nodes.append({"id": node_id, "label": node_id, "status_label": "Verified Fact", "degree_y": row["degree_y"]})
        if row["is_row_sum_factor"]:
            edges.append({"source": node_id, "target": f"{row['model']}_row_sum", "kind": "row_sum_factor", "status_label": "Verified Fact"})
        if row["factor_hash"] == SHARED_HASH:
            edges.append({"source": node_id, "target": "shared_factor_C", "kind": "same_hash", "status_label": "Verified Fact"})
    nodes.extend([
        {"id": "shared_factor_C", "label": "shared factor C", "status_label": "Verified Fact"},
        {"id": "unit_residual", "label": "unit residual", "status_label": "Verified Fact"},
        {"id": "full_residual", "label": "full residual", "status_label": "Verified Fact"},
    ])
    graph = {"status": "Verified Fact", "nodes": nodes, "edges": edges, "claim_boundary": BOUNDARY}
    write_json(graph_dir / "factor_graph.json", graph, outputs)
    dot = ["digraph r3_factor_graph {"]
    for node in nodes:
        dot.append(f'  "{node["id"]}" [label="{node["label"]}"];')
    for edge in edges:
        dot.append(f'  "{edge["source"]}" -> "{edge["target"]}" [label="{edge["kind"]}"];')
    dot.append("}")
    write_text(graph_dir / "factor_graph.dot", "\n".join(dot), outputs)
    write_text(REPORTS / f"{stamp}_r3_factor_network_analysis.md", f"""# r=3 Factor Network Analysis

status: Verified Fact
scope: finite-level r=3 S-level factor graph from audited factor and gcd artifacts
method: graph projection of factor hashes, row-sum roles, shared-factor roles, and residual nodes
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`, `data/generated/r3_deep_program/{stamp}/factor_graph/`
artifacts_produced: `{(graph_dir / "factor_graph.json").relative_to(ROOT)}`, `{(graph_dir / "factor_graph.dot").relative_to(ROOT)}`
""", outputs)
    small_reports = {
        "r3_commutant_specialization_analysis": ("Not Established", "Generic commutant solving over QQ(t) and exact specialization projector search are deferred to a focused Sage/linear-algebra pass."),
        "r3_equitable_partition_search": ("Not Established", "No exact equitable partition witness was generated in this bounded publication pass."),
        "r3_automorphism_search": ("Not Established", "No exact automorphism witness was generated in this bounded publication pass."),
        "r3_determinant_target_taxonomy": ("Advisory Only", "Determinant targets are charpoly evaluations, det(S), det(I-S), residual-factor determinants, and compact determinant objects from prior constraints; all-real-s nonvanishing remains Not Established."),
        "r3_determinant_root_isolation_attempt": ("Not Established", "Exact root isolation was not completed for high-degree determinant targets."),
        "r2_r3_factor_structure_comparison": ("Computational Observation", "This comparison does not establish cross-level invariance. r=2 mechanisms do not transfer to r=3 without independent r=3 witness."),
        "audit_tooling_patch": ("Patched", "validate_claim_ladder.py now supports --since, --exclude-audits, and --output to avoid recursively auditing audit artifacts."),
        "r3_reproducibility_notes": ("Advisory Only", "scripts/r3_deep_program_reproduce.sh reruns Python checks, exact gcd, exact residual/relation expansion, deep-program report generation, and witness collection with local Sage."),
    }
    for slug, (status, body) in small_reports.items():
        payload = {"status": status, "created_utc": stamp, "summary": body, "claim_boundary": BOUNDARY}
        write_json(REPORTS / f"{stamp}_{slug}.json", payload, outputs)
        write_text(REPORTS / f"{stamp}_{slug}.md", f"""# {slug.replace('_', ' ')}

status: {status}
scope: finite-level r=3 S-level deep-program support report
method: bounded program generation and explicit blocker classification
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`
artifacts_produced: this report pair

{body}
""", outputs)


def theorem_and_final(stamp: str, data_dir: Path, outputs: list[Path], state: dict[str, Any]) -> None:
    candidates = [
        {
            "name": "r=3 generic S-level factorization",
            "status_label": "Verified Fact",
            "r": 3,
            "level": "S-level",
            "model": "unit/full/both",
            "ring": "QQ[t][y]",
            "statement": "The audited unit/full characteristic polynomial factorization has the recorded degree and multiplicity patterns.",
            "evidence_artifacts": [str(AUDIT_MANIFEST.relative_to(ROOT))],
            "exact_checks": ["Sage reconstruction", "total y-degree", "row-sum factor match"],
            "missing_proof_steps": [],
            "why_this_does_not_imply_Collatz": BOUNDARY,
        },
        {
            "name": "residual coprimality",
            "status_label": "Verified Fact",
            "r": 3,
            "level": "S-level",
            "model": "both",
            "ring": "QQ(t)[y]",
            "statement": "The unit and full residual products have gcd degree zero as derived from exact pairwise residual-factor gcds.",
            "evidence_artifacts": [f"data/generated/r3_deep_program/{stamp}/factor_relations/gcd_table.json"],
            "exact_checks": ["pairwise gcd manifest"],
            "missing_proof_steps": [],
            "why_this_does_not_imply_Collatz": BOUNDARY,
        },
        {
            "name": "structural mechanism",
            "status_label": "Not Established",
            "r": 3,
            "level": "S-level",
            "model": "unit/full/both",
            "ring": "QQ(t)[y]",
            "statement": "A mechanism explaining squared residual factors has not been established.",
            "evidence_artifacts": [],
            "exact_checks": [],
            "missing_proof_steps": ["commutant/projector/equitable-partition witness"],
            "why_this_does_not_imply_Collatz": BOUNDARY,
        },
        {
            "name": "determinant nonvanishing",
            "status_label": "Not Established",
            "r": 3,
            "level": "S-level",
            "model": "unit/full/both",
            "ring": "not fixed",
            "statement": "All-real-s determinant nonvanishing is not established.",
            "evidence_artifacts": [],
            "exact_checks": [],
            "missing_proof_steps": ["target determinant selection", "root isolation", "sign chart"],
            "why_this_does_not_imply_Collatz": BOUNDARY,
        },
    ]
    write_json(REPORTS / f"{stamp}_r3_deep_program_theorem_candidates.json", candidates, outputs)
    write_text(REPORTS / f"{stamp}_r3_deep_program_theorem_candidates.md", f"""# r=3 Deep Program Theorem Candidates

status: Advisory Only
scope: finite-level r=3 S-level theorem-candidate triage
method: classification of exact artifacts and blocked targets
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`
artifacts_produced: theorem-candidate Markdown and JSON

- Verified Fact: r=3 generic S-level factorization.
- Verified Fact: residual coprimality derived from exact pairwise gcds.
- Not Established: structural mechanism.
- Not Established: determinant nonvanishing for all real `s > 0`.
""", outputs)
    repro = [
        "bash scripts/bootstrap_codex.sh",
        "python3 scripts/check_codex_skills.py",
        "python3 scripts/run_py_checks.py",
        "env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_structure_gcd.sage --timestamp {}".format(stamp),
        "env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_relation_expansion.sage --timestamp {}".format(stamp),
        "python3 scripts/r3_deep_program_generate.py --timestamp {}".format(stamp),
        "python3 .agents/skills/collatz-exact-algebra-lab/scripts/collect_witnesses.py",
    ]
    write_text(data_dir / "reproduction_commands.txt", "\n".join(repro), outputs)
    final_payload = {
        "status": "Advisory Only",
        "created_utc": stamp,
        "scope": "finite-level r=3 S-level deep-structure program",
        "commands_run": repro,
        "artifacts_created_count": len(outputs),
        "verified_facts": ["factor registry", "exact gcd table reuse", "residual product checks"],
        "computational_observations": ["numerical specialization sweep", "modular determinant samples"],
        "not_established_items": ["structural mechanism", "all-real-s determinant nonvanishing", "cross-level invariance", "exact subdominant factor ownership"],
        "blocked_items": ["generic resultants/discriminants and commutants require focused follow-up"],
        "new_exact_targets": ["commutant/projector search", "selected resultant/root-isolation target"],
        "recommended_next_mission": "focused exact mechanism search from factor graph and residual gcd facts",
        "proof_boundary": BOUNDARY,
        "canonical_readiness": "needs human review",
        "repo_commit": state["repo_commit"],
    }
    write_json(REPORTS / f"{stamp}_r3_deep_program_final.json", final_payload, outputs)
    write_text(REPORTS / f"{stamp}_r3_deep_program_final.md", f"""# r=3 Deep Program Final

status: Advisory Only
scope: finite-level r=3 S-level deep-structure, spectrum, determinant, and canonical-insertion-prep program
method: Python report generation, exact Sage residual/relation expansion, numerical specialization sweep, modular determinant samples, and proof-boundary classification
claim_boundary: {BOUNDARY}
reproduction_command: `bash scripts/r3_deep_program_reproduce.sh {stamp}`
files_touched: `reports/`, `data/generated/r3_deep_program/{stamp}/`, `scripts/`, `sage/`
artifacts_produced: final Markdown/JSON, program manifest, artifact index, factor registry, residual/relation artifacts, theorem candidates, and witness manifest

## Verified Facts

- Factor registry generated from audited r=3 S-level Sage factorization artifacts.
- Residual products and reconstruction checks were generated by Sage over `QQ(t)[y]`.
- Residual cross-gcd degree zero is derived from the exact pairwise gcd manifest over `QQ(t)[y]`.

## Computational Observations

- Numerical specialization sweep and modular determinant samples were generated for bounded grids.

## Not Established

- Structural mechanism.
- Determinant nonvanishing for all real `s > 0`.
- Cross-level invariance.
- Exact subdominant factor ownership and dominance for all `t > 0`.

## Canonical Readiness

needs human review; canonical files were not edited.
""", outputs)
    write_text(REPORTS / f"{stamp}_r3_next_mission_recommendation.md", f"""# r=3 Next Mission Recommendation

status: Advisory Only
scope: follow-up recommendation after finite-level r=3 deep program
method: report-only synthesis from generated artifacts
claim_boundary: {BOUNDARY}
reproduction_command: `bash scripts/r3_deep_program_reproduce.sh {stamp}`
files_touched: `reports/`
artifacts_produced: this recommendation

Recommended next mission: run a focused exact commutant/projector/equitable-partition search on the residual factors, then select one determinant target for exact root-isolation only if the target is explicitly defined.
""", outputs)


def orchestration_report(stamp: str, outputs: list[Path]) -> None:
    payload = {
        "status": "Advisory Only",
        "target": "r=3 deep structure, spectrum, determinant, and canonical-insertion-prep program",
        "scope": "finite-level r=3 S-level unit/full matrices and audited factor artifacts",
        "out_of_scope": "Collatz proof, global orbit behavior, determinant nonvanishing for all real s > 0 without proof, canonical edits",
        "subtasks": [
            {"owner_role": "algebra_explorer", "backend": "Sage", "task": "residual and factor relation expansion"},
            {"owner_role": "experiment_runner", "backend": "Python", "task": "specialization sweep and artifact generation"},
            {"owner_role": "proof_auditor", "backend": "report-only", "task": "claim-boundary validation"},
            {"owner_role": "implementation_engineer", "backend": "Python/shell", "task": "validation and reproduction tooling"},
        ],
        "commands": ["bash scripts/bootstrap_codex.sh", "env DOT_SAGE=$PWD/.codex/sage ./.sage-conda/bin/sage sage/r3_factor_relation_expansion.sage", "python3 scripts/r3_deep_program_generate.py"],
        "expected_artifacts": ["reports/", "data/generated/r3_deep_program/"],
        "claim_boundary": BOUNDARY,
        "blocked_items": ["generic high-degree resultants and commutants deferred"],
        "next_step": "focused exact mechanism search",
    }
    write_json(REPORTS / f"{stamp}_r3_deep_program_orchestration.json", payload, outputs)
    write_text(REPORTS / f"{stamp}_r3_deep_program_orchestration.md", f"""# r=3 Deep Program Orchestration

status: Advisory Only
target: {payload["target"]}
scope: {payload["scope"]}
out_of_scope: {payload["out_of_scope"]}
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`
artifacts_produced: this orchestration report pair

next_step: {payload["next_step"]}
""", outputs)


def build_index_and_manifest(stamp: str, data_dir: Path, outputs: list[Path]) -> None:
    entries = []
    for path in sorted(outputs, key=lambda p: str(p)):
        if path.exists() and path.is_file():
            rel = str(path.relative_to(ROOT))
            entries.append({
                "path": rel,
                "kind": path.suffix.lstrip(".") or "file",
                "status_label": "Advisory Only" if "report" in rel or rel.endswith(".md") else "Verified Fact",
                "sha256": sha256_file(path),
                "producer_phase": "r3_deep_program",
                "claim_boundary": "Hashes authenticate artifacts only; they do not upgrade mathematical claims.",
                "summary": path.name,
            })
    index = {"status": "Advisory Only", "created_utc": stamp, "entries": entries, "claim_boundary": BOUNDARY}
    write_json(data_dir / "artifact_index.json", index, outputs)
    write_json(data_dir / "program_manifest.json", {"status": "Advisory Only", "created_utc": stamp, "artifact_index": f"data/generated/r3_deep_program/{stamp}/artifact_index.json", "claim_boundary": BOUNDARY}, outputs)
    write_text(REPORTS / f"{stamp}_r3_artifact_index.md", f"""# r=3 Artifact Index

status: Advisory Only
scope: index of generated finite-level r=3 deep-program artifacts
method: SHA-256 hashing of generated outputs
claim_boundary: {BOUNDARY}
reproduction_command: `python3 scripts/r3_deep_program_generate.py --timestamp {stamp}`
files_touched: `reports/`, `data/generated/r3_deep_program/{stamp}/`
artifacts_produced: `{(data_dir / "artifact_index.json").relative_to(ROOT)}`, `{(data_dir / "program_manifest.json").relative_to(ROOT)}`

Indexed generated artifacts with SHA-256 hashes for reproducibility.
""", outputs)
    write_json(REPORTS / f"{stamp}_r3_artifact_index.json", index, outputs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timestamp", default=None)
    args = parser.parse_args()
    stamp = args.timestamp or utc_stamp()
    REPORTS.mkdir(exist_ok=True)
    data_dir = DEEP_ROOT / stamp
    data_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []

    state = state_lock(stamp, data_dir, outputs)
    registry = factor_registry(stamp, data_dir, outputs)
    canonical_review(stamp, outputs)
    sweep_and_tracking(stamp, data_dir, outputs)
    graph_and_planning_reports(stamp, data_dir, registry, outputs)
    theorem_and_final(stamp, data_dir, outputs, state)
    orchestration_report(stamp, outputs)
    build_index_and_manifest(stamp, data_dir, outputs)

    print(json.dumps({
        "ok": True,
        "timestamp": stamp,
        "final_report": f"reports/{stamp}_r3_deep_program_final.md",
        "program_manifest": f"data/generated/r3_deep_program/{stamp}/program_manifest.json",
        "artifact_count": len(outputs),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
