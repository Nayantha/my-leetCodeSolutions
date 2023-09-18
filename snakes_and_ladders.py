# https://leetcode.com/problems/snakes-and-ladders/description/
def snakes_and_ladders(board: list[list[int]]) -> int:
    board_length = len(board)

    def int_to_position(number: int):
        return [number // board_length, number % board_length]
