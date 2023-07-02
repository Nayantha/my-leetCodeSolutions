# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

def is_subsequence(s: str, t: str) -> bool:
    sub_string = "".join([letter for letter in t if letter in s])
    return s == sub_string or s in sub_string
