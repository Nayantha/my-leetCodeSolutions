# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m != len(nums1):
            for i in nums2:
                nums1.remove(0)
        nums1[:] = sorted(nums1 + nums2)
