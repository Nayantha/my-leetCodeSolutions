# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
def max_area(height: list[int]) -> int:
    left_pointer, right_pointer = 0, len(height) - 1
    max_area = right_pointer * min(height[left_pointer], height[right_pointer])
    while left_pointer != right_pointer:
        if height[right_pointer] > height[left_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1
        max_area = max(
            (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer]),
            max_area
        )
    return max_area
