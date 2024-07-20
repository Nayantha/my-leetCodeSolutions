# https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def trap(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    total_height = 0
    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            total_height += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            total_height += right_max - height[r]

    return total_height
