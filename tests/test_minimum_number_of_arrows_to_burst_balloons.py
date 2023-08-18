import pytest

from minimum_number_of_arrows_to_burst_balloons import find_min_arrow_shots


@pytest.mark.parametrize("points, expected", [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ([[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]], 5)
])
def test_find_min_arrow_shots(points: list[list[int]], expected: int):
    assert find_min_arrow_shots(points) == expected
