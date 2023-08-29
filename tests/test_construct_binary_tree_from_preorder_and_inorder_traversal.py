import pytest

from construct_binary_tree_from_preorder_and_inorder_traversal import build_tree
from data_structures.tree_node import TreeNode
from data_structures.trees import generate_list_according_to_pre_order


@pytest.mark.parametrize("pre_order_list_values, in_order_list_values, expected_tree_node_values_in_pre_order", [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
    ([-1], [-1], [-1])
])
def test_build_tree(pre_order_list_values: list[int], in_order_list_values: list[int],
                    expected_tree_node_values_in_pre_order: list[int]):
    tree_root: TreeNode = build_tree(preorder=pre_order_list_values, inorder=in_order_list_values)
    pre_order_list_values_of_tree = generate_list_according_to_pre_order(tree_root)
    for value in pre_order_list_values:
        assert value in pre_order_list_values_of_tree
    pre_order_list_values_of_tree = [value for value in pre_order_list_values_of_tree if value]
    assert pre_order_list_values_of_tree == pre_order_list_values
