import pytest

from data_structures.singly_linked_list import array_to_list


@pytest.mark.parametrize("input_list_values,partition_value,partitioned_list_values", [
    ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
    ([2, 1], 2, [1, 2]),
])
def test_partition(input_list_values: list[int], partition_value: int, partitioned_list_values: list[int]):
    input_list_head = array_to_list(input_list_values)
    partitioned_list_head = array_to_list(partitioned_list_values)
    
