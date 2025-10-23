import builtins
from src import calculator


def test_full_flow(monkeypatch):
    inputs = iter(["1", "3", "4", "n"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    calculator.main()
