import pytest


@pytest.mark.parametrize("board, expected")
def test_is_valid_sudoku(board: list[list[int | str]], expected: bool):
    assert False
