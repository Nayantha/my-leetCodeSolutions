import pytest

from valid_anagram import is_anagram


@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False)
])
def test_is_anagram(s: str, t: str, expected: bool):
    assert is_anagram(s, t) == expected
