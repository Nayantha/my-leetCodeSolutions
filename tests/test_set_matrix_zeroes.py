import pytest

from set_matrix_zeroes import set_zeroes


@pytest.mark.parametrize("matrix, expected")
def test_set_zeroes(matrix: list[list[int]], expected: list[list[int]]):
    set_zeroes(matrix)
    assert matrix == expected
