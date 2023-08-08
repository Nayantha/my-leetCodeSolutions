# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150
def length_of_longest_substring(s: str) -> int:
    if len(s) == 1:
        return 1
    res_str = []
    max_len = 0
    for ele in s:
        if ele not in res_str:  # type: str
            res_str.append(ele)
        else:
            max_len = max(max_len, len(res_str))
            res_str = [ele]
    return max_len
