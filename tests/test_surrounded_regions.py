import pytest


@pytest.mark.parametrize("board, expected", [
    ([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
     [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]),
    ([["X"]], [["X"]])
])
def test_solve(board: list[list[str]], expected: list[list[str]]):
    assert False
