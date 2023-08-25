import pytest

from list_node import ListNode
from remove_duplicates_from_sorted_list_ii import delete_duplicates


@pytest.mark.parametrize("input_list, expected_list", [
    ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
    ([1, 1, 1, 2, 3], [2, 3])
])
def test_delete_duplicates(input_list: list[int], expected_list: list[int]):
    expected_list_head = ListNode(val=expected_list[0])
    output_list_head = delete_duplicates(ListNode(val=input_list[0]))
    assert output_list_head == expected_list_head
    while output_list_head and expected_list_head:
        assert output_list_head.val == expected_list_head.val
        output_list_head = output_list_head.next
        expected_list_head.next = expected_list_head.next
