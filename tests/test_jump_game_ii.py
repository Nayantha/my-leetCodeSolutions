import pytest

from jump_game_ii import jump


@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 0, 1, 4], 2)
])
def test_jump(nums: list[int], expected: int):
    assert jump(nums) == expected
