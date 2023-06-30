import pytest


@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True)
])
def test_is_palindrome(s: str, expected: str):
    assert False
