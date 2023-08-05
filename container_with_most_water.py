# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
def max_area(height: list[int]) -> int:
    areas = []
    left_pointer = 0
    right_pointer = len(height) - 1
    while left_pointer < right_pointer:
        areas.append(
            (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
        )
        if height[right_pointer] > height[left_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1
    return max(areas)
