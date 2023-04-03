# https://leetcode.com/problems/plus-one/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        number = int("".join(digits))
        number += 1
        return [int(digit) for digit in str(number)]
