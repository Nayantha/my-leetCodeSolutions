import pytest

from zigzag_conversion import convert


@pytest.mark.parametrize("s, num_rows, expected")
def test_convert(s: str, num_rows: int, expected: str):
    assert convert(s, num_rows) == expected
