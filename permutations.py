# https://leetcode.com/problems/permutations/description/
def permute(nums: list[int]) -> list[list[int]]:
    if not nums:
        return [[]]
    if len(nums) == 1:
        return [nums.copy()]
