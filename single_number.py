# https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter
from typing import List


def single_number(nums: List[int]) -> int:
    num_and_count = Counter(nums)
    print(num_and_count)
