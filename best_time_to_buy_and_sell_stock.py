# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

from typing import List
def max_profit(prices: List[int]) -> int:
    min_sell_value = min(prices)
    sellable_price_list = prices[prices.index(min_sell_value) + 1:]
    if not sellable_price_list:
        return 0
    return max(sellable_price_list) - min_sell_value

