# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

def is_subsequence(self, s: str, t: str) -> bool:
    for letter in s:
        if letter not in t:
            return False
    return True
