# https://leetcode.com/problems/reverse-bits/?envType=study-plan-v2&envId=top-interview-150
def reverse_bits(n: int) -> int:
    res = 0
    for _ in range(32):
        res = res << 1
        res += n % 2
        n = n >> 1
    return res
