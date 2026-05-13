# Exact r=3 characteristic-polynomial/factorization attempt.
# Run: sage sage/r3_factorization_search.sage unit
#      sage sage/r3_factorization_search.sage full
# Warning: full model may be expensive.

import sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from collatz_codex_harness.construct import level_spec, s_counter_matrix

if len(sys.argv) < 2 or sys.argv[1] not in ["unit", "full"]:
    raise SystemExit("usage: sage sage/r3_factorization_search.sage unit|full")

model = sys.argv[1]
R = PolynomialRing(QQ, "t")
t = R.gen()

def counter_expr(c):
    return R(sum(ZZ(coeff) * t**ZZ(exp) for exp, coeff in c.items()))

def matrix_S(r, model):
    counters = s_counter_matrix(r, model)
    return Matrix(R, [[counter_expr(entry) for entry in row] for row in counters])

started = time.time()
spec = level_spec(3, model)
M = matrix_S(3, model)
print(f"r=3 model={model} dim={M.nrows()} period={spec.period}")
print("computing characteristic polynomial...")
cp = M.charpoly(var="y")
print("factoring...")
fac = cp.factor()
elapsed = time.time() - started

out = []
out.append("status: Computational Observation pending independent audit")
out.append("scope: r=3 S-level exact polynomial over QQ[t]")
out.append(f"model: {model}")
out.append(f"dimension: {M.nrows()}")
out.append(f"elapsed_sec: {elapsed:.3f}")
out.append("claim_boundary: exact finite-level algebra only; no Collatz-level conclusion")
out.append("")
out.append(str(fac))
out.append("")

report = ROOT / "reports" / f"sage_r3_{model}_factorization.sageout"
report.parent.mkdir(exist_ok=True)
report.write_text("\n".join(out))
print(report)
