import pytest

from integer_to_roman import int_to_roman


@pytest.mark.parametrize("num, expected", [
    (3, "III"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
    (4, "IV"),
    (9, "IX"),
    (40, "XL"),
    (90, "XC"),
    (400, "CD"),
    (900, "CM")
])
def test_int_to_roman(num: int, expected: str):
    assert int_to_roman(num) == expected
