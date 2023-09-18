# https://leetcode.com/problems/snakes-and-ladders/description/
def snakes_and_ladders(board: list[list[int]]) -> int:
    rows, columns = len(board), len(board[0])
    go_forward_in_columns = True
    for row in range(rows - 1, -1, -1):
        if go_forward_in_columns:
            for column in range(columns):
                print(f"board[r={row}][c={column}]={board[row][column]}")
        else:
            for column in range(columns - 1, -1, -1):
                print(f"board[r={row}][c={column}]={board[row][column]}")
        go_forward_in_columns = not go_forward_in_columns
