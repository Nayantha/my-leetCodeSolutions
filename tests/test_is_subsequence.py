import pytest
@pytest.mark.parametrize("s, t, expected", [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False)
])
def test_is_subsequence(s: str, t: str, expected: bool):
    ...
