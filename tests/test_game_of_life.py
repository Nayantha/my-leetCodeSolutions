import pytest

from game_of_life import game_of_life


@pytest.mark.parametrize("board, expected")
def test_game_of_life(board: list[list[int]], expected: list[list[int]]):
    game_of_life(board)
    assert board == expected
