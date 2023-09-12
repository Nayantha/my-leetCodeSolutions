# https://leetcode.com/problems/surrounded-regions/
def solve(board: list[list[str]]) -> None:
    rows = len(board)
    columns = len(board[0])

    def capture(row: int, column: int):
        if row not in range(rows) or column not in range(columns) or board[row][column] != "O":
            return
    # get un-surrounded regions
    # get surrounded regions
    # rename un-surrounded regions
