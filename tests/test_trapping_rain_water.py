import pytest

from trapping_rain_water import trap


@pytest.mark.parametrize("height, expected", [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9)
])
def test_trap(height: list[int], expected: int):
    assert trap(height) == expected
