import pytest

from letter_combinations_of_a_phone_number import letter_combinations


@pytest.mark.parametrize("digits, combinations", (
        ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
        ["", []],
        ['2', ["a", "b", "c"]]
))
def test_letter_combinations(digits: str, combinations: list[str]):
    assert letter_combinations(digits) == combinations
