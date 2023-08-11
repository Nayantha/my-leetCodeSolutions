# https://leetcode.com/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150
def rotate(matrix: list[list[int]]) -> None:
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            # save top left
            top_left = matrix[top][l + i]
            # move bottom left to top left
            matrix[top][l + i] = matrix[bottom - i][l]
            # move bottom right to bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]
            # move top right to bottom right
            matrix[bottom][r - i] = matrix[top + i][r]
            # move top left to right
            matrix[top + i][r] = top_left
        l += 1
        r -= 1

def rotate_ii(matrix: list[list[int]]) -> None:
    left, right = 0, len(matrix) - 1
    top, bottom = 0, len(matrix[0]) - 1
    while left < right and top < bottom:
        for i in range(left, right):
            matrix[top][i], matrix[top + i][right] = matrix[top + i][right], matrix[top][i]
        for i in range(left, right):
            matrix[top + i][right], matrix[bottom][right - i - left] = matrix[bottom][right - i - left], \
                matrix[top + i][right]
        for i in range(left, right):
            matrix[bottom][right - i - left], matrix[bottom - top - i][left] = matrix[bottom - top - i][left], \
                matrix[bottom][right - i - left]
        left += 1
        right -= 1
        top += 1
        bottom -= 1
