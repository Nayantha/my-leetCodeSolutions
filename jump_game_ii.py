# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
def jump(nums: list[int]) -> int:
    jumps = l = r = 0
    while r < len(nums) - 1:
        furthest_jump = 0
        for i in range(l, r + 1):
            furthest_jump = max(furthest_jump, i + nums[i])
        l = r + 1
        r = furthest_jump
        jumps += 1
    return jumps
