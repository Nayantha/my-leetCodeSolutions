# https://leetcode.com/problems/two-sum/submissions/

from typing import List
from itertools import combinations

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in combinations(nums, 2):
            if i[0] + i[1] == target:
                first_number = nums.index(i[0])
                last_number = nums.index(i[1])
                if first_number == last_number:
                    last_number = nums[first_number+1:].index(i[1]) + first_number + 1
                return [first_number, last_number]
        return []


def main():
    soln = Solution()
    
    # assert == [0, 1]
    print(soln.two_sum([3, 2, 3], 6))


if __name__ == "__main__":
    main()
