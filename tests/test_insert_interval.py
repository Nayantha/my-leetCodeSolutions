import pytest

from insert_interval import insert


@pytest.mark.parametrize("intervals, new_interval, expected", [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]])
])
def test_insert(intervals: list[list[int]], new_interval: list[int], expected: list[list[int]]):
    assert insert(intervals, new_interval) == expected
