# https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150
def game_of_life(board: list[list[int]]) -> None:
    # Original | New | State
    #     0    |  0  |   0
    #     1    |  0  |   1
    #     0    |  0  |   2
    #     1    |  1  |   3

    def get_sum_of_neighbours(r, c):
        sum_of_adjacent_neighbours = 0
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if (i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS:
                    continue
                if board[i][j] in [1, 3]:
                    sum_of_adjacent_neighbours += 1
        return sum_of_adjacent_neighbours

    ROWS, COLS = len(board), len(board[0])
    for r in range(ROWS):
        for c in range(COLS):
            sum_of_neighbours = get_sum_of_neighbours(r, c)
            if board[r][c] and sum_of_neighbours in [2, 3]:
                board[r][c] = 3
            elif sum_of_neighbours == 3:
                board[r][c] = 2
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] in [2, 3]:
                board[r][c] = 1
