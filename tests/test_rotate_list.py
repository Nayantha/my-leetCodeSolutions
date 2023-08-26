import pytest


@pytest.mark.parametrize("initial_list, number_of_rotations, rotated_list", [
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([0, 1, 2], 4, [2, 0, 1])
])
def test_rotate_right(initial_list: list[int], number_of_rotations: int, rotated_list: list[int]):
    assert False
