import pytest


@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3)
])
def test_length_of_longest_substring(s: str, expected: int):
    assert False
