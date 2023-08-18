import pytest


@pytest.mark.parametrize("points, expected", [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2)
])
def test_find_min_arrow_shots(points: list[list[int]], expected: int):
    assert False
