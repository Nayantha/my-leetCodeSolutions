from typing import List

import pytest

from jump_game import can_jump


@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False)
])
def test_can_jump(nums: List[int], expected: bool):
    assert can_jump(nums) == expected
