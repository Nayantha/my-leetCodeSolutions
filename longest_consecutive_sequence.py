# https://leetcode.com/problems/longest-consecutive-sequence/
def longest_consecutive(nums: list[int]) -> int:
    nums = set(nums)
    longest_consecutive_list_len = 0

    for n in nums:
        if n - 1 not in nums:
            curr_len = 0
            while (n + curr_len) in nums:
                curr_len += 1
            longest_consecutive_list_len = max(longest_consecutive_list_len, curr_len)
    return longest_consecutive_list_len
