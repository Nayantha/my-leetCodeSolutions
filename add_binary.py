# https://leetcode.com/problems/add-binary/?envType=study-plan-v2&envId=top-interview-150
def add_binary(a: str, b: str) -> str:
    return str(bin(int(a, 2) + int(b, 2))).removeprefix("0b")
