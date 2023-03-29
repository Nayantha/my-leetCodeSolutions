# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        new_array = nums.copy()
        for i in range(len(nums)):
            new_array[(k + i) % len(nums)] = nums[i]
        nums.clear()
        nums += new_array


nums = [-1, -100, 3, 99]
sol = Solution()
sol.rotate(nums=nums, k=2)
print(nums)
