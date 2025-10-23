import builtins
import sys
from src import calculator


def run_with_inputs(inputs, monkeypatch):
    """
    Feed simulated user inputs to calculator.main() safely.
    Always quits after the loop to prevent hanging.
    """
    it = iter(inputs)

    def safe_input(_):
        try:
            return next(it)
        except StopIteration:
            sys.exit(0)

    monkeypatch.setattr(builtins, "input", safe_input)

    try:
        calculator.main()
    except SystemExit:
        pass


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


def test_invalid_choice(monkeypatch):
    """Covers the 'Invalid choice' branch."""
    run_with_inputs(["9", "2", "3", "n"], monkeypatch)


def test_divide_by_zero(monkeypatch):
    """Covers ZeroDivisionError inside calculator.main()."""
    run_with_inputs(["4", "10", "0", "n"], monkeypatch)
