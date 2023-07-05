# https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150

def is_anagram(s: str, t: str) -> bool:
    return sorted(list(s)) == sorted(list(t))
