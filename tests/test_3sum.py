import pytest

from _3sum import three_sum, three_sum_ii


@pytest.mark.parametrize("nums, expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]])
])
def test_three_sum(nums: list[int], expected: list[list[int]]):
    for output in three_sum(nums):
        assert output in expected

@pytest.mark.parametrize("nums, expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]])
])
def test_three_sum(nums: list[int], expected: list[list[int]]):
    for output in three_sum_ii(nums):
        assert output in expected
