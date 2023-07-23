# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def max_profit(prices: List[int]) -> int:
    profit = 0
    buy_day_price = prices[0]
    for i in range(1, len(prices)):
        sell_day_price = prices[i]
        if sell_day_price > buy_day_price:
            profit += sell_day_price - buy_day_price
        buy_day_price = sell_day_price
    return profit
