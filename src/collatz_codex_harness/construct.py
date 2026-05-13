"""Finite-level lifted-operator matrix construction.

Canonical object:
    S_r,model(t)[i,j] = sum_live_columns t^(a0(row_i,col)+a0(row_j,col))

The prefactor c_r = h^2/(1-t^P)^2 is deliberately omitted here because
S is the unscaled polynomial form. B = c_r * S.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from math import gcd
from typing import Iterable, Literal

Model = Literal["unit", "full"]


R2_UNIT_EXPONENT_TABLE = [
    [2, 1, 18, 15, 4, 17, 14, 7, 12, 3, 16, 5, 8, 13, 6, 9, 10, 11],
    [16, 15, 14, 11, 18, 13, 10, 3, 8, 17, 12, 1, 4, 9, 2, 5, 6, 7],
    [8, 7, 6, 3, 10, 5, 2, 13, 18, 9, 4, 11, 14, 1, 12, 15, 16, 17],
    [4, 3, 2, 17, 6, 1, 16, 9, 14, 5, 18, 7, 10, 15, 8, 11, 12, 13],
    [14, 13, 12, 9, 16, 11, 8, 1, 6, 15, 10, 17, 2, 7, 18, 3, 4, 5],
    [10, 9, 8, 5, 12, 7, 4, 15, 2, 11, 6, 13, 16, 3, 14, 17, 18, 1],
]

R2_FULL_LEAF_EXPONENT_ROWS = [
    [6, 5, 4, 1, 8, 3, 18, 11, 16, 7, 2, 9, 12, 17, 10, 13, 14, 15],
    [18, 17, 16, 13, 2, 15, 12, 5, 10, 1, 14, 3, 6, 11, 4, 7, 8, 9],
    [12, 11, 10, 7, 14, 9, 6, 17, 4, 13, 8, 15, 18, 5, 16, 1, 2, 3],
]


@dataclass(frozen=True)
class LevelSpec:
    r: int
    model: Model
    modulus: int
    period: int
    rows: tuple[int, ...]
    live_columns: tuple[int, ...]


def multiplicative_order_2(modulus: int) -> int:
    """Return ord_modulus(2). Assumes gcd(2, modulus)=1."""
    if gcd(2, modulus) != 1:
        raise ValueError("modulus must be odd")
    value = 1 % modulus
    for k in range(1, modulus * 2 + 1):
        value = (value * 2) % modulus
        if value == 1:
            return k
    raise RuntimeError(f"failed to find order of 2 modulo {modulus}")


def unit_rows(r: int) -> tuple[int, ...]:
    """Canonical U_r rows: residues 1..3^r-1 not divisible by 3."""
    if r < 1:
        raise ValueError("r must be positive")
    modulus = 3**r
    return tuple(i for i in range(1, modulus) if gcd(i, 3) == 1)


def odd_multiples_of_3_representatives(r: int) -> tuple[int, ...]:
    """Odd multiples of 3 modulo 2*3^r used as full-model leaf reps."""
    return tuple(range(3, 2 * (3**r), 6))


def full_rows(r: int) -> tuple[int, ...]:
    return unit_rows(r) + odd_multiples_of_3_representatives(r)


def live_columns(r: int) -> tuple[int, ...]:
    """Live source columns for K_r: U_{r+1} inside modulus 3^(r+1)."""
    modulus = 3 ** (r + 1)
    return tuple(i for i in range(1, modulus) if gcd(i, 3) == 1)


def source_zero_columns(r: int) -> tuple[int, ...]:
    """Full-model zero source columns, not included in S."""
    return odd_multiples_of_3_representatives(r + 1)


def level_spec(r: int, model: Model) -> LevelSpec:
    if model not in {"unit", "full"}:
        raise ValueError("model must be 'unit' or 'full'")
    modulus = 3 ** (r + 1)
    period = multiplicative_order_2(modulus)
    rows = unit_rows(r) if model == "unit" else full_rows(r)
    return LevelSpec(
        r=r,
        model=model,
        modulus=modulus,
        period=period,
        rows=rows,
        live_columns=live_columns(r),
    )


@lru_cache(maxsize=None)
def a0(r: int, n: int, m: int) -> int:
    """Canonical exponent a0(n,m) in {1,...,P_r}.

    Defined by 2^a m ≡ 3n+1 (mod 3^(r+1)).
    """
    modulus = 3 ** (r + 1)
    period = multiplicative_order_2(modulus)
    target = (3 * n + 1) % modulus
    for a in range(1, period + 1):
        if (pow(2, a, modulus) * (m % modulus)) % modulus == target:
            return a
    raise ValueError(f"no a0 found for r={r}, n={n}, m={m}, target={target}")


def exponent_table(r: int, model: Model) -> list[list[int]]:
    spec = level_spec(r, model)
    return [[a0(r, n, m) for m in spec.live_columns] for n in spec.rows]


def s_entry_counter(row_a: list[int], row_b: list[int]) -> Counter[int]:
    c: Counter[int] = Counter()
    for ea, eb in zip(row_a, row_b, strict=True):
        c[ea + eb] += 1
    return c


def s_counter_matrix(r: int, model: Model) -> list[list[Counter[int]]]:
    """Return S matrix entries as exponent->coefficient Counters."""
    table = exponent_table(r, model)
    n = len(table)
    return [[s_entry_counter(table[i], table[j]) for j in range(n)] for i in range(n)]


def counter_to_sympy_expr(counter: Counter[int], symbol=None):
    """Convert an exponent Counter to a SymPy expression."""
    import sympy as sp

    t = symbol if symbol is not None else sp.Symbol("t")
    return sum(coeff * t**exp for exp, coeff in sorted(counter.items()))


def s_sympy_matrix(r: int, model: Model, symbol=None):
    """Return S_r,model(t) as a SymPy Matrix over ZZ[t]."""
    import sympy as sp

    t = symbol if symbol is not None else sp.Symbol("t")
    counters = s_counter_matrix(r, model)
    return sp.Matrix([[counter_to_sympy_expr(entry, t) for entry in row] for row in counters])


def eval_counter_float(counter: Counter[int], t_value: float) -> float:
    return float(sum(coeff * (t_value**exp) for exp, coeff in counter.items()))


def s_numeric_matrix(r: int, model: Model, s: float):
    """Evaluate S(t) numerically at t=2^(-s), using NumPy double precision."""
    import numpy as np

    t_value = 2.0 ** (-float(s))
    counters = s_counter_matrix(r, model)
    return np.array(
        [[eval_counter_float(entry, t_value) for entry in row] for row in counters],
        dtype=float,
    )


def row_sum_counters(r: int, model: Model) -> list[Counter[int]]:
    matrix = s_counter_matrix(r, model)
    out: list[Counter[int]] = []
    for row in matrix:
        total: Counter[int] = Counter()
        for entry in row:
            total.update(entry)
        out.append(+total)
    return out


def all_row_sums_equal(r: int, model: Model) -> bool:
    rows = row_sum_counters(r, model)
    return all(row == rows[0] for row in rows[1:])


def eval_counter_mod(counter: Counter[int], t_value: int, prime: int) -> int:
    total = 0
    tv = t_value % prime
    for exp, coeff in counter.items():
        total = (total + (coeff % prime) * pow(tv, exp, prime)) % prime
    return total


def s_matrix_mod(r: int, model: Model, t_value: int, prime: int) -> list[list[int]]:
    counters = s_counter_matrix(r, model)
    return [[eval_counter_mod(entry, t_value, prime) for entry in row] for row in counters]


def det_mod_prime(matrix: list[list[int]], prime: int) -> int:
    """Determinant over GF(prime) via Gaussian elimination."""
    n = len(matrix)
    a = [[x % prime for x in row] for row in matrix]
    det = 1
    for col in range(n):
        pivot = None
        for row in range(col, n):
            if a[row][col] % prime:
                pivot = row
                break
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = (-det) % prime
        pv = a[col][col] % prime
        det = (det * pv) % prime
        inv = pow(pv, -1, prime)
        for row in range(col + 1, n):
            factor = (a[row][col] * inv) % prime
            if factor:
                for k in range(col, n):
                    a[row][k] = (a[row][k] - factor * a[col][k]) % prime
    return det % prime
