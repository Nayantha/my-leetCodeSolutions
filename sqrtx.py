# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r

sol = Solution()
print(sol.mySqrt(8))