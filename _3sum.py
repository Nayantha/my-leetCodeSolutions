# https://leetcode.com/problems/3sum/
from itertools import combinations


def three_sum(nums: list[int]) -> list[list[int]]:
    result = list()
    for triplet in combinations(nums, 3):
        triplet = sorted(list(triplet))
        if sum(triplet) == 0:
            if triplet not in result:
                result.append(triplet)
    return result


def three_sum_ii(nums: list[int]) -> list[list[int]]:
    result = []
    nums = list(set(nums))
    for i in nums:
        for j in nums[i + 1:]:
            for k in nums[i + j + 1:]:
                triplet = sorted([i, j, k])
                if sum(triplet) == 0 and triplet not in result:
                    result.append(triplet)
    return result

def three_sum_iii(nums: list[int]) -> list[list[int]]:
    result = []
    nums = list(set(sorted(nums)))
    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            triplet = sorted(nums[i], nums[l], nums[r])
            if sum(triplet) == 0 and triplet not in result:
                result.append(triplet)
    return result
