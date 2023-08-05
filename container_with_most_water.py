# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
def max_area(height: list[int]) -> int:
    result = 0
    for index_i, element_i in enumerate(height):
        for index_j, element_j in enumerate(height[index_i + 1:]):
            result = max((min(element_i, element_j) * (index_j + 1)), result)
    return result
