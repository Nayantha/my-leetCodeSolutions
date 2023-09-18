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
