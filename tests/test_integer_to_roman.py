import pytest


@pytest.mark.parametrize("nums, expected", [
    (3, "III"),
    (58, "LVIII"),
    (1994, "MCMXCIV")
])
def test_int_to_roman(nums: int, expected: str):
    assert False
