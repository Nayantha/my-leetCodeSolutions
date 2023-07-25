import pytest

from jump_game_ii import jump


@pytest.mark.parametrize("nums, expected")
def test_jump(nums: list[int], expected: int):
    assert jump(nums) == int
