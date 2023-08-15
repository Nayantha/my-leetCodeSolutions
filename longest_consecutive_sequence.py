# https://leetcode.com/problems/longest-consecutive-sequence/
def longest_consecutive(nums: list[int]) -> int:
    nums.sort()
    last_index_of_consecutive_list = 0
    longest_consecutive_list_len = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 1:
            last_index_of_consecutive_list += 1
        else:
            last_index_of_consecutive_list = 0
        longest_consecutive_list_len = max(longest_consecutive_list_len, last_index_of_consecutive_list)
    return longest_consecutive_list_len + 1
