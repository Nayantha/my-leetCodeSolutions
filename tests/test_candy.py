import pytest


@pytest.mark.parametrize("ratings, expected", [
    ([1, 0, 2], 5),
    ([1, 2, 2], 4)
])
def test_candy(ratings: list[int], expected: int):
    assert False
