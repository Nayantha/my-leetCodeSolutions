import pytest

from data_structures.singly_linked_list import array_to_list
from partition_list import partition


@pytest.mark.parametrize("input_list_values,partition_value,partitioned_list_values", [
    ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
    ([2, 1], 2, [1, 2]),
])
def test_partition(input_list_values: list[int], partition_value: int, partitioned_list_values: list[int]):
    input_list_head = array_to_list(input_list_values)
    partitioned_list_head = array_to_list(partitioned_list_values)
    output_list_head = partition(input_list_head, partition_value)
    while partitioned_list_head and output_list_head:
        assert output_list_head.val == partitioned_list_head.val
        output_list_head = output_list_head.next
        partitioned_list_head = partitioned_list_head.next
