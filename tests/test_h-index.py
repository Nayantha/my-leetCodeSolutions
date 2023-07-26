import pytest

from h_index import h_index


@pytest.mark.parametrize("citations, expected")
def test_h_index(citations: list[int], expected: int):
    assert h_index(citations) == expected
