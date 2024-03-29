import pytest

from snakes_and_ladders import snakes_and_ladders


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
     ], 1),
    (
            [
                [-1, 1, 2, -1],
                [2, 13, 15, -1],
                [-1, 10, -1, -1],
                [-1, 6, 2, 8]
            ],
            2
    )
])
def test_snakes_and_ladders(board: list[list[int]], min_turns_to_top: int):
    assert snakes_and_ladders(board) == min_turns_to_top
