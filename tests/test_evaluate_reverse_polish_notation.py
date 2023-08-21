import pytest

from evaluate_reverse_polish_notation import eval_rpn


@pytest.mark.parametrize("tokens, expected")
def test_eval_rpn(tokens: list[str], expected: int):
    assert eval_rpn(tokens) == expected
