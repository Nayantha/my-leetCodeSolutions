import pytest

from zigzag_conversion import convert


@pytest.mark.parametrize("s, num_rows, expected", [
    ("PAYPALISHIRING", 1, "PAYPALISHIRING"),
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A")
])
def test_convert(s: str, num_rows: int, expected: str):
    assert convert(s, num_rows) == expected
