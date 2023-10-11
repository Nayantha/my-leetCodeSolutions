import pytest


@pytest.mark.parametrize("digits, combinations", (
        ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
        ["", []],
        ['2', ["a", "b", "c"]]
))
def test_letter_combinations(digits: str, combinations: list[str]):
    assert False
