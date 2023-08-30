import pytest


@pytest.mark.parametrize("post_order_list_values, in_order_list_values, expected_tree_node_values_in_pre_order", [
    ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
    ([-1], [-1], [-1])
])
def test_build_tree(post_order_list_values: list[int], in_order_list_values: list[int],
                    expected_tree_node_values_in_pre_order: list[int]):
    assert False
