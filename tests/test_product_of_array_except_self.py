import pytest


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
])
def test_product_except_self(nums: list[int], expected: list[int]):
    assert False
