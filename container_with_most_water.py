# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
def max_area(height: list[int]) -> int:
    result = 0
    for left_pointer in range(len(height)):
        for right_pointer in range(left_pointer + 1, len(height)):
            result = max(result, min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer))
    return result
