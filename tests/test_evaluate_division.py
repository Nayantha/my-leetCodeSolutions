import pytest

from evaluate_division import calc_equation


@pytest.mark.parametrize("equations, values, queries, expected", [
    ([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
     [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]),
    ([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
     [3.75000, 0.40000, 5.00000, 0.20000]),
    ([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]], [0.50000, 2.00000, -1.00000, -1.00000])
])
def test_calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]], expected: list[int]):
    assert calc_equation(equations, values, queries) == expected
