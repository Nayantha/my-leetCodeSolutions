import pytest

from list_node import ListNode
from rotate_list import rotate_right


@pytest.mark.parametrize("initial_list, number_of_rotations, rotated_list", [
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([0, 1, 2], 4, [2, 0, 1])
])
def test_rotate_right(initial_list: list[int], number_of_rotations: int, rotated_list: list[int]):
    output_list_head = rotate_right(ListNode(val=initial_list[0]), number_of_rotations)
    rotated_list_head = ListNode(val=rotated_list[0])
    while rotated_list_head and output_list_head:
        assert rotated_list_head.val == output_list_head.val
        rotated_list_head = rotated_list_head.next
        output_list_head = output_list_head.next
