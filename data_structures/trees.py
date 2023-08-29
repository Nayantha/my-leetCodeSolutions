from data_structures.tree_node import TreeNode


def generate_list_according_to_pre_order(root: TreeNode) -> list[int | None]:
    pre_order_value_list = []
    traverse_in_binary_tree(root, pre_order_value_list)
    return pre_order_value_list


def traverse_in_binary_tree(root: TreeNode, pre_order_value_list: list[int | None]):
    if root:
        pre_order_value_list.append(root.val)
        traverse_in_binary_tree(root.left, pre_order_value_list)
        traverse_in_binary_tree(root.right, pre_order_value_list)
    pre_order_value_list.append(None)
