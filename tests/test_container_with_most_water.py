import pytest

from container_with_most_water import max_area


@pytest.mark.parametrize("heights, expected")
def test_max_area(heights: list[int], expected: int):
    assert max_area(heights) == expected
