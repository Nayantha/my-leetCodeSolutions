from typing import List

import pytest


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 1], 3, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 3, 1, 2, 3], 2, False)
])
def test_contains_nearby_duplicate(nums: List[int], k: int, expected: bool):
    ...
