from typing import List

import pytest

from single_number import single_number


@pytest.mark.parametrize("nums, expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1)
])
def test_single_number(nums: List[int], expected: int):
    single_number(nums)
