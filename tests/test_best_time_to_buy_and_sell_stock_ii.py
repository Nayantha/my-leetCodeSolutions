from typing import List

import pytest


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0)
])
def test_max_profit(prices: List[int], expected: int):
    assert False
