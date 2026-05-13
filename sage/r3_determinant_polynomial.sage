# Exact r=3 determinant polynomial attempt.
# Run: sage sage/r3_determinant_polynomial.sage unit|full

import sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from collatz_codex_harness.construct import s_counter_matrix

if len(sys.argv) < 2 or sys.argv[1] not in ["unit", "full"]:
    raise SystemExit("usage: sage sage/r3_determinant_polynomial.sage unit|full")
model = sys.argv[1]

R = PolynomialRing(QQ, "t")
t = R.gen()

def counter_expr(c):
    return R(sum(ZZ(coeff) * t**ZZ(exp) for exp, coeff in c.items()))

started = time.time()
counters = s_counter_matrix(3, model)
M = Matrix(R, [[counter_expr(entry) for entry in row] for row in counters])
det = M.det()
fac = det.factor()
elapsed = time.time() - started

report = ROOT / "reports" / f"sage_r3_{model}_determinant.sageout"
report.write_text("\n".join([
    "status: Computational Observation pending independent audit",
    "scope: exact determinant polynomial over QQ[t]",
    f"model: {model}",
    f"dimension: {M.nrows()}",
    f"elapsed_sec: {elapsed:.3f}",
    "claim_boundary: determinant polynomial artifact only; no all-real-s nonvanishing proof and no Collatz-level conclusion",
    "",
    str(fac),
    "",
]))
print(report)
