# https://leetcode.com/problems/number-of-1-bits/?envType=study-plan-v2&envId=top-interview-150
def hamming_weight(n: int) -> int:
    return str(bin(n)).count("1", 2)
