import pytest

from sqrtx import Solution
class TestSolution:
    @pytest.mark.parametrize("x, expected",[
        (4, 2),
        (8, 2),
        (1, 1)
    ])
    def test_my_sqrt(self, x, expected):
        sol = Solution()
        assert sol.mySqrt(x=x) == expected
