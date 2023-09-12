# https://leetcode.com/problems/surrounded-regions/
def solve(board: list[list[str]]) -> None:
    # board_copy = copy.deepcopy(board)
    rows = len(board)
    columns = len(board[0])
    board_copy = board.copy()
    for row_index in range(rows):
        for column_index in range(columns):
            if board_copy[row_index][column_index] == "O":
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, column = row_index + dr, column_index + dc
                    if row in range(rows) and column in range(columns) and board_copy[row][column] == "O":
                        board[row][column] = "X"
