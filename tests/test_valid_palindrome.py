import pytest

from valid_palindrome import is_palindrome


@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True)
])
def test_is_palindrome(s: str, expected: bool):
    assert is_palindrome(s) == expected
