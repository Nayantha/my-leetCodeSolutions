import pytest

from list_node import ListNode


@pytest.mark.parametrize("input_list, expected_list", [
    ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
    ([1, 1, 1, 2, 3], [2, 3])
])
def test_delete_duplicates(input_list: list[int], expected_list: list[int]):
    list_values = [1, 2, 3, 3, 4, 4, 5]
    head = ListNode(val=list_values[0])
