# https://leetcode.com/problems/surrounded-regions/
def solve(board: list[list[str]]) -> None:
    rows = len(board)
    columns = len(board[0])

    def capture(row: int, column: int):
        if row not in range(rows) or column not in range(columns) or board[row][column] != "O":
            return
        board[row][column] = "T"
        capture(row - 1, column)
        capture(row + 1, column)
        capture(row, column - 1)
        capture(row, column + 1)

    # get un-surrounded regions
    for row_index in range(rows):
        for column_index in range(columns):
            if board[row_index][column_index] == "O" and (
                    row_index in [0, rows - 1] or column_index in [0, columns - 1]):
                capture(row_index, column_index)
    # get surrounded regions
    # rename un-surrounded regions
