import pytest


@pytest.mark.parametrize("value_list, right_node_value_list", [
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
    ([1, None, 3], [1, 3]),
    ([], [])
])
def test_right_side_view(value_list: list[int], right_node_value_list: list[int]):
    ...
