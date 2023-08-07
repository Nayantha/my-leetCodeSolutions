import pytest

from minimum_size_subarray_sum import min_sub_array_len


@pytest.mark.parametrize("target, nums, expected")
def test_min_sub_array_len(target: int, nums: list[int], expected: int):
    assert min_sub_array_len(target, nums) == expected
