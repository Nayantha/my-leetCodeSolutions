# https://leetcode.com/problems/snakes-and-ladders/description/
def snakes_and_ladders(board: list[list[int]]) -> int:
    rows, columns = len(board), len(board[0])
    for row in range(rows - 1, -1, -1):
        for column in range(columns):
            print(f"board[r={row}][c={column}]={board[row][column]}")
