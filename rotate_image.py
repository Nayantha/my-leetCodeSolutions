# https://leetcode.com/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150
def rotate(matrix: list[list[int]]) -> None:
    left, right = 0, len(matrix) - 1
    top, bottom = 0, len(matrix[0]) - 1
    while left < right and top < bottom:
        for i in (left, right - 1):
            matrix[top][i], matrix[top][right - i] = matrix[top][right - i], matrix[top][i]
        for i in (top, bottom - 1):
            matrix[i][left], matrix[bottom - i][left] = matrix[bottom - i][left], matrix[i][left]
        for i in (left, right - 1):
            matrix[bottom][i], matrix[bottom][right - i] = matrix[bottom][right - i], matrix[bottom][i]
        left += 1
        top += 1
        right -= 1
        bottom -= 1
