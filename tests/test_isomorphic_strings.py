import pytest

from isomorphic_strings import is_isomorphic


@pytest.mark.parametrize("s, t, expected", [
    ("egg", "add", True),
    ("paper", "title", True),
    ("foo", "bar", False)
])
def test_is_isomorphic(s: str, t: str, expected: bool):
    assert is_isomorphic(s, t) == expected
