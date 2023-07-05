import pytest

from happy_number import is_happy


@pytest.mark.parametrize("n, expected", [
    (19, True),
    (2, False)
])
def test_is_happy(n: int, expected: bool):
    assert is_happy(n) == expected
