import pytest

from set_matrix_zeroes import set_zeroes


@pytest.mark.parametrize("matrix, expected", [
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
])
def test_set_zeroes(matrix: list[list[int]], expected: list[list[int]]):
    set_zeroes(matrix)
    assert matrix == expected
