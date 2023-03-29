# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums: List[int], first: int, last: int, target: int) -> int:
        if first >= last:
            if target <= nums[first]:
                return first
            else:
                return first + 1
        mid = int(first + (last - first) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, last, target)
        else:
            return self.binary_search(nums, first, mid -1 , target)
            