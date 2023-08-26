import pytest

from data_structures.singly_linked_list import array_to_list
from rotate_list import rotate_right


@pytest.mark.parametrize("initial_list, number_of_rotations, rotated_list", [
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([0, 1, 2], 4, [2, 0, 1])
])
def test_rotate_right(initial_list: list[int], number_of_rotations: int, rotated_list: list[int]):
    output_list_head = rotate_right(array_to_list(initial_list), number_of_rotations)
    rotated_list_head = array_to_list(rotated_list)
    while rotated_list_head and output_list_head:
        assert rotated_list_head.val == output_list_head.val
        rotated_list_head = rotated_list_head.next
        output_list_head = output_list_head.next
