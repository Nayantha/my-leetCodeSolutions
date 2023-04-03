import pytest
from merge_sorted_array import Solution


class TestSolution:
    @pytest.mark.parametrize("nums1,m, nums2,n, expected", [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3])
    ])
    def test_merge(self, nums1, m, nums2, n, expected):
        sol = Solution()
        sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)
        assert nums1 == expected
