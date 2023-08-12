# https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150
def set_zeroes(matrix: list[list[int]]) -> None:
    matrix_to_bool = [[col == 0 for col in row] for row in matrix]
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            ele = matrix[row_index][column_index]
            is_place_zero = matrix_to_bool[row_index][column_index]
            if not ele and is_place_zero:
                for i in range(len(matrix[0])):
                    matrix[row_index][i] = 0
                for i in range(len(matrix)):
                    matrix[i][column_index] = 0
