from re

import pytest

from list_node import ListNode


@pytest.mark.parametrize("input_list, expected_list", [
    ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
    ([1, 1, 1, 2, 3], [2, 3])
])
def test_delete_duplicates(input_list: list[int], expected_list: list[int]):
    input_list_head = ListNode(val=input_list[0])
    expected_list_head = ListNode(val=expected_list[0])
    assert input_list_head == expected_list_head
    while input_list_head and expected_list_head:
        assert input_list_head.val == expected_list_head.val
        input_list_head = input_list_head.next
        expected_list_head.next = expected_list_head.next
