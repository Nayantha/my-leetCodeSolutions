import pytest


@pytest.mark.parametrize("s, t, expected", [
    ("egg", "add", True),
    ("paper", "title", True),
    ("foo", "bar", False)
])
def test_is_isomorphic(s: str, t: str, expected: bool):
    assert False
