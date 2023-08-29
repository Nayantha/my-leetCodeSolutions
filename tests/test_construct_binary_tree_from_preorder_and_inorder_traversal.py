import pytest


@pytest.mark.parametrize("pre_order_list_values, in_order_list_values, expected_tree_node_values_in_pre_order")
def test_build_tree(pre_order_list_values: list[int], in_order_list_values: list[int],
                    expected_tree_node_values_in_pre_order: list[int]):
    assert False
