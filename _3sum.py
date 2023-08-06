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
