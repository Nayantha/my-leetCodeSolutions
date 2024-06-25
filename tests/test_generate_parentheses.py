import pytest


@pytest.mark.parametrize("n, expected", [
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (0, []),
    (1, ["()"])
])
def test_generate_parentheses(n: int, expected: list[str]):
    assert False
