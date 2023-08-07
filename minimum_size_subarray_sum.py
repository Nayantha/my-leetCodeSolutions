# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
def min_sub_array_len(target: int, nums: list[int]) -> int:
    if target > sum(nums):
        return 0
    for num in nums:
        if target <= num:
            return 1
    l, r = 0, 0
    window_size = 0
    while l < len(nums) and r < len(nums):
        if sum(nums[l:r]) < target:
            r += 1
        else:
            if not window_size:
                window_size = r - l
            else:
                window_size = min(window_size, r - l)
                l += 1
    return window_size
