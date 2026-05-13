# Fast exact r=2 sanity/factorization script.
# Run: sage sage/r2_verify_factorization.sage

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from collatz_codex_harness.construct import s_counter_matrix

R = PolynomialRing(QQ, "t")
t = R.gen()
Y = PolynomialRing(R, "y")
y = Y.gen()

def counter_expr(c):
    return R(sum(ZZ(coeff) * t**ZZ(exp) for exp, coeff in c.items()))

def matrix_S(r, model):
    counters = s_counter_matrix(r, model)
    return Matrix(R, [[counter_expr(entry) for entry in row] for row in counters])

out = []
for model in ["unit", "full"]:
    M = matrix_S(2, model)
    cp = M.charpoly(var="y")
    fac = cp.factor()
    out.append(f"MODEL {model}")
    out.append(f"dimension={M.nrows()}")
    out.append(f"charpoly_factorization={fac}")
    out.append("")

report = ROOT / "reports" / "sage_r2_factorization.sageout"
report.parent.mkdir(exist_ok=True)
report.write_text("\n".join(out))
print(report)
