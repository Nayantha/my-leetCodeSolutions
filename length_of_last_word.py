# https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

def length_of_last_word(s: str) -> int:
    return len(s.strip().split(" ")[-1])
