# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

from typing import List
def max_profit(prices: List[int]) -> int:
    max_profit_gainable = 0
    left = 0
    right = 1
    while right < len(prices):
        profit = prices[right] - prices[left]
        if prices[right] > prices[left]:
            max_profit_gainable = max(profit, max_profit_gainable)
        else:
            left = right
        right += 1
    return max_profit_gainable
