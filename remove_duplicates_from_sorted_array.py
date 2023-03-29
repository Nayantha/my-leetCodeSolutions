# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        num = list(set(nums))
        nums.clear()
        nums += num
        nums.sort()
        return len(nums)
    