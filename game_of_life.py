# https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150
def game_of_life(board: list[list[int]]) -> None:
    for row_index in range(len(board)):
        for col_index in range(len(board[0])):
            ele = board[row_index][col_index]
            sum_of_neighbours = sum(
                # first row / the row above
                board.__getitem__(row_index - 1).__getitem__(col_index - 1) +
                board.__getitem__(row_index - 1).__getitem__(col_index) +
                board.__getitem__(row_index - 1).__getitem__(col_index + 1) +
                # same row
                board.__getitem__(row_index).__getitem__(col_index - 1) +
                board.__getitem__(row_index).__getitem__(col_index + 1) +
                # row below
                board.__getitem__(row_index + 1).__getitem__(col_index - 1) +
                board.__getitem__(row_index + 1).__getitem__(col_index) +
                board.__getitem__(row_index + 1).__getitem__(col_index + 1)
            )
            if ele == 1 and (sum_of_neighbours != 2 or sum_of_neighbours != 3):
                board[row_index][col_index] = 0
            if ele == 0 and sum_of_neighbours == 3:
                board[row_index][col_index] = 1
