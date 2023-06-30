import pytest

from valid_palindrome import is_palindrome, is_palindrome_two_pointers


@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("0P", False)
])
def test_is_palindrome(s: str, expected: bool):
    assert is_palindrome_two_pointers(s) == expected
    assert is_palindrome(s) == expected
