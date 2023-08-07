import pytest

from minimum_size_subarray_sum import min_sub_array_len


@pytest.mark.parametrize("target, nums, expected", [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)
])
def test_min_sub_array_len(target: int, nums: list[int], expected: int):
    assert min_sub_array_len(target, nums) == expected
