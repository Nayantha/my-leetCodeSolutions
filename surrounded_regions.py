# https://leetcode.com/problems/surrounded-regions/
def solve(board: list[list[str]]) -> None:
    # board_copy = copy.deepcopy(board)
    rows = len(board)
    columns = len(board[0])
    board_copy = board.copy()
    for row_index in range(1, rows - 1):
        for column_index in range(1, columns - 1):
            if board_copy[row_index][column_index] == "O":
                directions = [
                    [-1, -1], [-1, 0], [-1, 1],
                    [0, -1], [0, 1],
                    [1, -1], [1, 0], [1, 1]
                ]
                sum_of_x = 0
                sum_of_o = 0
                for dr, dc in directions:
                    row, column = row_index + dr, column_index + dc
                    if row in range(rows) and column in range(columns):
                        if board_copy[row][column] == "X":
                            sum_of_x += 1
                        elif board_copy[row][column] == "O":
                            sum_of_o += 1
                if sum_of_x > sum_of_o:
                    board[row_index][column_index] = "X"
