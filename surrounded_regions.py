# https://leetcode.com/problems/surrounded-regions/
def solve(board: list[list[str]]) -> None:
    # board_copy = copy.deepcopy(board)
    rows = len(board)
    columns = len(board[0])
    board_copy = board.copy()
    for row_index in range(1, rows - 1):
        for column_index in range(1, columns - 1):
            if board_copy[row_index][column_index] == "O":
                board[row_index][column_index] = "X"
