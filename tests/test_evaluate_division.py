import pytest

from evaluate_division import calc_equation


@pytest.mark.parametrize("equations, values, queries", [
    ([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]),
    ([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]),
    ([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]])
])
def test_calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]):
    assert calc_equation(equations, values, queries) == expedted
