# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
def min_sub_array_len(target: int, nums: list[int]) -> int:
    l, total, res = 0, 0, float("inf")
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if res == float("inf") else res
