# https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
def h_index(citations: list[int]) -> int:
    return sorted(citations)[len(citations) // 2]
