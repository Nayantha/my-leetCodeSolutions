# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

def is_subsequence(s: str, t: str) -> bool:
    if s in t:
        return True
    for letter in s:
        if letter not in t:
            return False
        else:
            t = t[t.index(letter)+1:]
    return True
