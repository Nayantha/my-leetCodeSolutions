from typing import List

import pytest

from best_time_to_buy_and_sell_stock_ii import max_profit


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0)
])
def test_max_profit(prices: List[int], expected: int):
    assert max_profit(prices) == expected
