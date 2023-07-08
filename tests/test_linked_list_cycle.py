from typing import List

import pytest


@pytest.mark.parametrize("data, next, expected", [
    ([3, 2, 0, -4], [1, 2, 3, 1], 1),
    ([1, 2], [1, 0], 0),
    ([1], [None], -1)
])
def test_has_cycle(data: List[int], next: List[int], expected: int):
    assert False
