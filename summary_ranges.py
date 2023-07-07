# https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def summary_ranges(nums: List[int]) -> List[str]:
    ranges = []
    for i, num in enumerate(nums):
        if ranges and ranges[-1][1] == num - 1:
            ranges[-1] = (ranges[-1][0], num)
        else:
            ranges.append((num, num))
    return [f"{x}->{y}" if x != y else f"{x}" for x, y in ranges]
