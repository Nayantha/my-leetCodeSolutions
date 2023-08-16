import pytest

from merge_intervals import merge


@pytest.mark.parametrize("intervals, expected")
def test_merge(intervals: list[list[int]], expected: list[list[int]]):
    assert merge(intervals) == expected
