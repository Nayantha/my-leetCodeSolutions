import pytest

from valid_sudoku import is_valid_sudoku


@pytest.mark.parametrize("board, expected")
def test_is_valid_sudoku(board: list[list[int | str]], expected: bool):
    is_valid_sudoku(board)
