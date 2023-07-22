# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def rotate(nums: List[int], k: int) -> None:
    nums_len = len(nums)
    k = k % nums_len
    list_separation_index = nums_len - k
    nums = nums[list_separation_index:] + nums[:list_separation_index]
    print(nums)
