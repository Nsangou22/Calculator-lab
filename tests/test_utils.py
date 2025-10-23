from src import utils
import pytest


def test_add_basic():
    assert utils.add(1, 2, 3) == 6


def test_subtract_basic():
    assert utils.subtract(10, 2, 3) == 5


def test_multiply_basic():
    assert utils.multiply(2, 3, 4) == 24


def test_divide_basic():
    assert utils.divide(8, 2) == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        utils.divide(10, 0)
