import pytest

from plus_one import Solution


class TestSolution:
    @pytest.mark.parametrize("digits, expected", [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0])
    ])
    def test_plus_one(self, digits, expected):
        sol = Solution()
        assert sol.plusOne(digits=digits) == expected
