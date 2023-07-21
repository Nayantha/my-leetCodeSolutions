from typing import List

import pytest

from remove_duplicates_from_sorted_array_ii import remove_duplicates


@pytest.mark.parametrize("nums,expected_nums_list,expected_nums_list_len", [
    ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3], 5),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3], 7)
])
def test_remove_duplicates(nums: List[int], expected_nums_list: List[int], expected_nums_list_len: int):
    assert remove_duplicates(nums) == expected_nums_list_len
    for i, j in zip(nums, expected_nums_list):
        assert i == j
