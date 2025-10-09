import pytest
from math import isclose
from calculator.core import sum, sub, mul, div


# ---------- TESTS FOR sum() ----------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-1, -2, -3),
        (-1, 2, 1),
        (0, 0, 0),
        (1.5, 2.3, 3.8),
        (1e10, 1e10, 2e10),
    ]
)
def test_sum(a, b, expected):
    assert sum(a, b) == expected


# ---------- TESTS FOR sub() ----------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (-5, -3, -2),
        (-5, 3, -8),
        (0, 0, 0),
        (2.5, 1.2, 1.3),
        (1e10, 1e9, 9e9),
    ]
)
def test_sub(a, b, expected):
    assert sub(a, b) == expected


# ---------- TESTS FOR mul() ----------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (-2, -3, 6),
        (0, 5, 0),
        (2.5, 4, 10.0),
        (1e5, 1e5, 1e10),
    ]
)
def test_mul(a, b, expected):
    assert mul(a, b) == expected


# ---------- TESTS FOR div() ----------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (-6, 3, -2),
        (-6, -3, 2),
        (5, 2, 2.5),
        (1e10, 1e5, 1e5),
    ]
)
def test_div(a, b, expected):
    assert div(a, b) == expected


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)


# ---------- ADDITIONAL TESTS ----------
def test_commutativity_sum_mul():
    a, b = 7, 3
    assert sum(a, b) == sum(b, a)
    assert mul(a, b) == mul(b, a)


def test_non_commutativity_sub_div():
    a, b = 7, 3
    assert sub(a, b) != sub(b, a)
    assert div(a, b) != div(b, a)


def test_float_precision():
    a, b = 0.1, 0.2
    assert isclose(sum(a, b), 0.3, rel_tol=1e-9)
    assert isclose(mul(a, b), 0.02, rel_tol=1e-9)
