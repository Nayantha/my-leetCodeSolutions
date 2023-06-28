from typing import List

import pytest

from best_time_to_buy_and_sell_stock import max_profit


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([2,4,1], 2)
])
def test_max_profit(prices: List[int], expected: int):
    assert max_profit(prices) == expected

