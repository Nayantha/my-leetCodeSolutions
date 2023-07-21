from typing import List

import pytest

from remove_duplicates_from_sorted_array_ii import remove_duplicates


@pytest.mark.parametrize("nums,expected_nums_list,expected_nums_list_len")
def test_remove_duplicates(nums: List[int], expected_nums_list: List[int], expected_nums_list_len: int):
    assert remove_duplicates(nums) == len(expected_nums_list)
    for i, j in zip(nums, expected_nums_list):
        assert i == j
