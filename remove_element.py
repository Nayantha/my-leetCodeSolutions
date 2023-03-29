# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not(0 <= len(nums) <= 100):
            return 0
        if any(i for i in nums if not(0 <= i <= 50)):
            return 0
        if not (0 <= val <= 100):
            return 0
        nums[:] = list(filter(lambda num: num != val, nums))
        return len(nums)
        pass
    