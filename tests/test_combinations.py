import pytest

from combinations import combine


@pytest.mark.parametrize("n, k, combinations")
def test_combine(n: int, k: int, combinations: list[list[int]]):
    assert combine(n, k) == combinations
