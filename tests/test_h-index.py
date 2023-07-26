import pytest

from h_index import h_index


@pytest.mark.parametrize("citations, expected", [
    ([3, 0, 6, 1, 5], 3),
    ([1, 3, 1], 1)
])
def test_h_index(citations: list[int], expected: int):
    assert h_index(citations) == expected
