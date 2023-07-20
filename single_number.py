# https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def single_number(nums: List[int]) -> int:
    for num in nums:
        if nums.count(num) == 1:
            return num
