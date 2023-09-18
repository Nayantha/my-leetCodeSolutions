import pytest


@pytest.mark.parametrize("board, min_turns_to_top", [
    ([
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]
     ], 4),
    ([
         [-1, -1],
         [-1, 3]
     ], 1)
])
def test_snakes_and_ladders(board: list[list[int]], min_turns_to_top: int):
    assert False
