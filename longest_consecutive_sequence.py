# https://leetcode.com/problems/longest-consecutive-sequence/
def longest_consecutive(nums: list[int]) -> int:
    nums.sort()
    last_index_of_consecutive_list = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[last_index_of_consecutive_list] in [0, 1]:
            last_index_of_consecutive_list += 1
    return last_index_of_consecutive_list
