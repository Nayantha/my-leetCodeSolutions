# https://leetcode.com/problems/surrounded-regions/
def solve(board: list[list[str]]) -> None:
    un_surrounded_areas = []
    rows = len(board)
    columns = len(board[0])
    for row_index in range(0, rows - 1, rows - 2):
        for column_index in range(0, columns - 1, columns - 2):
            if board[row_index][column_index] == "O":
                un_surrounded_areas.append((row_index, column_index))
