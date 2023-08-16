import pytest

from merge_intervals import merge


@pytest.mark.parametrize("intervals, expected", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]])
])
def test_merge(intervals: list[list[int]], expected: list[list[int]]):
    assert merge(intervals) == expected
