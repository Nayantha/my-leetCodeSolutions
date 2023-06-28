# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        unique_number_set = set(sorted(nums))
        max_occurrences = 0
        max_occurred_num = 0
        for num in unique_number_set:
            num_count = nums.count(num)
            if max_occurrences < num_count:
                max_occurrences = num_count
                max_occurred_num = num
        return max_occurred_num
