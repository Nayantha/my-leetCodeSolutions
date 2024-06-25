import pytest

from generate_parentheses import generate_parentheses


@pytest.mark.parametrize("n, expected", [
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (0, []),
    (1, ["()"])
])
def test_generate_parentheses(n: int, expected: list[str]):
    assert generate_parentheses(n) == expected
