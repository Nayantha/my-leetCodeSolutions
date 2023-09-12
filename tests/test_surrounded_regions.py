import pytest

from surrounded_regions import solve


@pytest.mark.parametrize("board, expected", [
    ([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
     [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]),
    ([["X"]], [["X"]])
])
def test_solve(board: list[list[str]], expected: list[list[str]]):
    solve(board)
    assert board == expected
