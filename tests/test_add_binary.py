import pytest

from add_binary import add_binary


@pytest.mark.parametrize("a, b, expectation", [
    ("11", "1", "100"),
    ("1010", "1011", "10101")
])
def test_add_binary(a: str, b: str, expectation: str):
    add_binary(a, b)
