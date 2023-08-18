import pytest

from minimum_number_of_arrows_to_burst_balloons import find_min_arrow_shots


@pytest.mark.parametrize("points, expected", [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ([[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]], 2)
])
def test_find_min_arrow_shots(points: list[list[int]], expected: int):
    """
    test find_min_arrow_shots in minimum_number_of_arrows_to_burst_balloons modules
    :param points: data that send as argument to the testing function
    :param expected: the expected result mapped to each point argument, used to validate the function output
    """
    assert find_min_arrow_shots(points) == expected
