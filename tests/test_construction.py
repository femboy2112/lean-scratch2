from collatz_codex_harness.construct import (
    R2_FULL_LEAF_EXPONENT_ROWS,
    R2_UNIT_EXPONENT_TABLE,
    all_row_sums_equal,
    exponent_table,
    full_rows,
    live_columns,
    multiplicative_order_2,
    unit_rows,
)


def test_periods():
    assert multiplicative_order_2(27) == 18
    assert multiplicative_order_2(81) == 54


def test_r2_tables():
    assert unit_rows(2) == (1, 2, 4, 5, 7, 8)
    assert full_rows(2) == (1, 2, 4, 5, 7, 8, 3, 9, 15)
    assert live_columns(2) == (1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26)
    assert exponent_table(2, "unit") == R2_UNIT_EXPONENT_TABLE
    assert exponent_table(2, "full")[6:] == R2_FULL_LEAF_EXPONENT_ROWS


def test_dimensions():
    assert len(unit_rows(3)) == 18
    assert len(full_rows(3)) == 27
    assert len(live_columns(3)) == 54


def test_row_sums_equal():
    for r in (2, 3):
        for model in ("unit", "full"):
            assert all_row_sums_equal(r, model)
