# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def can_jump(nums: List[int]) -> bool:
    current_jump = nums[0]
    for current_index in range(1, len(nums)):
        if current_jump == 0:
            return False
        current_jump -= 1
        current_jump = max(current_jump, nums[current_index])
    return True
