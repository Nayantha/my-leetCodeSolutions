# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150
def length_of_longest_substring(s: str) -> int:
    res_str = []
    max_len = 0
    for ele in s:
        if ele not in res_str:  # type: str
            res_str.append(ele)
        else:
            res_str = [ele]
        max_len = max(max_len, len(res_str))
    return max_len
