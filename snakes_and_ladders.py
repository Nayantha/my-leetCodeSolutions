# https://leetcode.com/problems/snakes-and-ladders/description/
from collections import deque


def snakes_and_ladders(board: list[list[int]]) -> int:
    board_length = len(board)

    def int_to_position(number: int):
        return [number // board_length, number % board_length]

    queue = deque([1, 0])  # [number, no of moves to get there]
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
