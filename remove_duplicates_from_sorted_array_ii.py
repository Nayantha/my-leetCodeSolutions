# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    for num in nums.copy():
        if nums.count(num) > 2:
            nums.remove(num)
    return len(nums)
