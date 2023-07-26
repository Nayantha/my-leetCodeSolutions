# https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
def h_index(citations: list[int]) -> int:
    citations = sorted(citations)
    for index, citation in enumerate(citations):
        if citation >= len(citations) - index:
            return len(citations) - index
    return 0


def h_index_ii(citations: list[int]) -> int:
    total_num_of_citations = len(citations)
    left_pointer = 0
    right_pointer = total_num_of_citations
    citations.sort()
    while left_pointer < right_pointer:
        mid_point = left_pointer + (right_pointer + left_pointer) // 2
        if citations[mid_point] == total_num_of_citations - mid_point:
            return citations[mid_point]
        elif citations[mid_point] > total_num_of_citations - mid_point:
            right_pointer = mid_point - 1
        else:
            left_pointer = mid_point + 1
    return total_num_of_citations - left_pointer
