from typing import List
from majority_element import Solution
import pytest


class TestSolution:
    @pytest.mark.parametrize("nums, expected", [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2)
    ])
    def test_majority_element(self, nums: List[int], expected: int):
        sol = Solution()
        assert sol.majority_element(nums) == expected
