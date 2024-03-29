import pytest

from valid_sudoku import is_valid_sudoku


@pytest.mark.parametrize("board, expected", [
     ([["5", "3", ".", ".", "7", ".", ".", ".", "."]
           , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
           , [".", "9", "8", ".", ".", ".", ".", "6", "."]
           , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
           , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
           , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
           , [".", "6", ".", ".", ".", ".", "2", "8", "."]
           , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
           , [".", ".", ".", ".", "8", ".", ".", "7", "9"]], True),
     ([["8", "3", ".", ".", "7", ".", ".", ".", "."]
           , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
           , [".", "9", "8", ".", ".", ".", ".", "6", "."]
           , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
           , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
           , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
           , [".", "6", ".", ".", ".", ".", "2", "8", "."]
           , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
           , [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False)
])
def test_is_valid_sudoku(board: list[list[int | str]], expected: bool):
    is_valid_sudoku(board)
    assert is_valid_sudoku(board) == expected
