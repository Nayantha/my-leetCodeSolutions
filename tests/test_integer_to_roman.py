import pytest

from integer_to_roman import int_to_roman


@pytest.mark.parametrize("num, expected", [
    (3, "III"),
    (58, "LVIII"),
    (1994, "MCMXCIV")
])
def test_int_to_roman(num: int, expected: str):
    int_to_roman(num)
