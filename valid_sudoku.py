# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
import collections


def is_valid_sudoku(board: list[list[str]]) -> bool:
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for row_index in range(9):
        for column_index in range(9):
            item = board[row_index][column_index]
            if item == ".":
                continue
            if item in rows[row_index] or item in cols[column_index] or item in squares[
                (row_index // 3, column_index // 3)]:
                return False
            cols[column_index].add(item)
            rows[row_index].add(item)
            squares[(row_index // 3, column_index // 3)].add(item)
    return True
