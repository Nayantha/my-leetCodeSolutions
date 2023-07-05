import pytest


@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False)
])
def test_is_anagram(s: str, t: str, expected: bool):
    ...
