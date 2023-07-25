# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
def jump(nums: list[int]) -> int:
    jumps = left_most_index_of_jump = right_most_index_of_jump = 0
    while right_most_index_of_jump < len(nums) - 1:
        furthest_jump = 0
        for i in range(left_most_index_of_jump, right_most_index_of_jump + 1):
            furthest_jump = max(furthest_jump, i + nums[i])
        left_most_index_of_jump = right_most_index_of_jump + 1
        right_most_index_of_jump = furthest_jump
        jumps += 1
    return jumps
