import pytest

from _3sum import three_sum, three_sum_ii, three_sum_iii


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
def test_three_sum_ii(nums: list[int], expected: list[list[int]]):
    for output in three_sum_ii(nums):
        assert output in expected


@pytest.mark.parametrize("nums, expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]])
])
def test_three_sum_iii(nums: list[int], expected: list[list[int]]):
    output = three_sum_iii(nums)
    for expected_list_ele in expected:
        assert expected_list_ele in output
