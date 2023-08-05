import pytest

from container_with_most_water import max_area


@pytest.mark.parametrize("heights, expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
])
def test_max_area(heights: list[int], expected: int):
    assert max_area(heights) == expected
