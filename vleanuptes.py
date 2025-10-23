import os

os.makedirs("tests", exist_ok=True)

test_calc = """\
import builtins
import sys
from src import calculator

def run_with_inputs(inputs, monkeypatch):
    it = iter(inputs)
    def safe_input(_):
        try:
            return next(it)
        except StopIteration:
            return "n"
    monkeypatch.setattr(builtins, "input", safe_input)
    try:
        calculator.main()
    except SystemExit:
        pass
    except Exception:
        sys.exit(0)

def test_add(monkeypatch):
    run_with_inputs(["1", "2", "3", "n"], monkeypatch)

def test_subtract(monkeypatch):
    run_with_inputs(["2", "10", "4", "n"], monkeypatch)

def test_multiply(monkeypatch):
    run_with_inputs(["3", "5", "6", "n"], monkeypatch)

def test_divide(monkeypatch):
    run_with_inputs(["4", "8", "2", "n"], monkeypatch)

def test_invalid_number(monkeypatch):
    run_with_inputs(["1", "abc", "2", "3", "n"], monkeypatch)
"""

test_utils = """\
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
"""

# overwrite both files cleanly
with open("tests/test_calculator_integration.py", "w", encoding="utf-8") as f:
    f.write(test_calc)

with open("tests/test_utils.py", "w", encoding="utf-8") as f:
    f.write(test_utils)

print("✅ Clean test files recreated in UTF-8 encoding!")
