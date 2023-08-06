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
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            triplet = sorted([a, nums[l], nums[r]])
            three_sum = sum(triplet)
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                result.append(triplet)
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return result
