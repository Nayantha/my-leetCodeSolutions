# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
def is_valid_sudoku(board: list[list[str]]) -> bool:
    for row in board:
        for item in row:
            if row.count(item) > 0 and type(item) == int:
                return False

    for column_index in range(9):
        column = [row[column_index] for row in board]
        for item in column:
            if column.count(item) > 0 and type(item) == int:
                return False

    return True
