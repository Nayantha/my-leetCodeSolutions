# https://leetcode.com/problems/surrounded-regions/
def solve(board: list[list[str]]) -> None:
    # board_copy = copy.deepcopy(board)
    board_copy = board.copy()
    for row_index in range(len(board)):
        for column_index in range(len(board[0])):
            if board_copy[row_index][column_index] == "O" and board_copy[row_index + 1][column_index] == "O" and \
                    board_copy[row_index - 1][column_index] == "O" and board_copy[row_index][
                column_index + 1] == "O" and board_copy[row_index][column_index - 1] == "O":
                board[row_index][column_index] = "X"
