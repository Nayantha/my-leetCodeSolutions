from typing import List

import pytest


@pytest.mark.parametrize("nums, expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1)
])
def test_single_number(nums: List[int], expected: int):
    assert False
