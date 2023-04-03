import pytest

from climbing_stairs import Solution
class TestSolution:
    @pytest.mark.parametrize("n, expected", [
        (2, 2),
        (3, 3),
        (4, 5)
    ])
    def test_climb_stairs(self, n, expected):
        sol = Solution()
        assert sol.climbStairs(n=n) == expected
