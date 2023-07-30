import pytest

from candy import candy


@pytest.mark.parametrize("ratings, expected", [
    ([1, 0, 2], 5),
    ([1, 2, 2], 4),
    ([1, 3, 2, 2, 1], 7),
    ([1, 2, 87, 87, 87, 2, 1], 13)
])
def test_candy(ratings: list[int], expected: int):
    assert candy(ratings) == expected
