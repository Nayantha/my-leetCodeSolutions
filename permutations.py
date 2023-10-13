# https://leetcode.com/problems/permutations/description/
def permute(nums: list[int]) -> list[list[int]]:
    if not nums:
        return [[]]
    if len(nums) == 1:
        return [nums[:]]
    result = []
    for i in range(len(nums)):
        num = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(num)
        result.extend(perms)

        nums.append(num)
    return result
