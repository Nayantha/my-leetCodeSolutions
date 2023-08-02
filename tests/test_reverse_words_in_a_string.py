import pytest


@pytest.mark.parametrize("s, expected", [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a")
])
def test_reverse_words(s: str, expected: str):
    assert False
