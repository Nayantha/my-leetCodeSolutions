# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    index_map = dict()
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    return False
