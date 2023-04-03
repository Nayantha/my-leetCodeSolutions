import pytest

from search_insert_position import Solution


class TestSolution:
    @pytest.mark.parametrize("nums, target, expected", [
        ([1, 2, 4, 6, 7], 3, 2)
    ])
    def test_search_insert(self, nums, target, expected):
        sol = Solution()
        assert sol.searchInsert(nums=nums, target=target) == expected
    
    def test_binary_search(self):
        assert True
