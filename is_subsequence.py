# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

def is_subsequence(s: str, t: str) -> bool:
    if not s and t:
        return True
    s_index = 0
    t_index = 0
    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
            t_index += 1
        else:
            t_index += 1
    if t_index == len(t) and s_index == len(s):
        return True
    else:
        return False
