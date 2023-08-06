import pytest

from _3sum import three_sum


@pytest.mark.parametrize("nums, expected")
def test_three_sum(nums: list[int], expected: list[list[int]]):
    assert three_sum(nums) == expected
