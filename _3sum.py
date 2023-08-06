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
    nums.sort()
    nums = list(set(nums))
    for i in nums:
        for j in nums[i + 1:]:
            for k in nums[j + 1:]:
                triplet = sorted([i, j, k])
                if sum(triplet) == 0 and triplet not in result:
                    result.append(triplet)
    return result
