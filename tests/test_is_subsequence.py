import pytest

from is_subsequence import is_subsequence


@pytest.mark.parametrize("s, t, expected", [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("acb", "ahbgdc", False),
    ("b", "abc", True),
    ("", "abc", True),
    ("ab", "baab", True)
])
def test_is_subsequence(s: str, t: str, expected: bool):
    assert is_subsequence(s, t) == expected
