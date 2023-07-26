# https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
def h_index(citations: list[int]) -> int:
    citations = sorted(citations)
    for index, citation in enumerate(citations):
        if citation >= len(citations) - index:
            return len(citations) - index
    return 0
