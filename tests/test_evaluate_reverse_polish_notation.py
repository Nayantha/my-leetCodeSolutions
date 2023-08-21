import pytest

from evaluate_reverse_polish_notation import eval_rpn


@pytest.mark.parametrize("tokens, expected", [
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
])
def test_eval_rpn(tokens: list[str], expected: int):
    assert eval_rpn(tokens) == expected
