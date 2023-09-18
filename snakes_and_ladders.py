# https://leetcode.com/problems/snakes-and-ladders/description/
from collections import deque


def snakes_and_ladders(board: list[list[int]]) -> int:
    board_length = len(board)

    def int_to_position(number: int):
        number -= 1
        row = number // board_length
        column = number % board_length
        if row % 2:
            column = board_length - 1
        return [row, column]

    queue = deque()  # [number, no of moves to get there]
    queue.append([1, 0])
    visited_numbers = set()
    while queue:
        number, moves_done = queue.popleft()
        for i in range(1, 7):
            next_number = number + i
            row, column = int_to_position(next_number)
            if board[row][column] == -1:
                next_number = board[row][column]
            if next_number == board_length ** 2:
                return moves_done + 1
            if next_number not in visited_numbers:
                visited_numbers.add(next_number)
                queue.append([next_number, moves_done + 1])
    return -1
