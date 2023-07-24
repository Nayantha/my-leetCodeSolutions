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


def can_jump_ii(nums: list[int]) -> bool:
    goal_position = len(nums) - 1
    for current_index in range(len(nums) - 1, -1, -1):
        if current_index + nums[current_index] >= goal_position:
            goal_position = current_index
    return goal_position == 0
