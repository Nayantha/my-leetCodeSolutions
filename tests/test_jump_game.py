from typing import List

import pytest


@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False)
])
def test_can_jump(nums: List[int], expected: bool):
    assert False
