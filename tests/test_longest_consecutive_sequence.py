import pytest


@pytest.mark.parametrize("nums, expected", [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
])
def test_longest_consecutive(nums: list[int], expected: int):
    assert False
