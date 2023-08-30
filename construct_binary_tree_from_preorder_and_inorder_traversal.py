# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import Optional

from data_structures.tree_node import TreeNode


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    values_to_index_map_of_inorder_list = {value: index for index, value in enumerate(inorder)}

    def helper_func(left, right):
        if left > right:
            return None
        root = TreeNode(preorder.pop())
        index_of_root_val_in_inorder_list = values_to_index_map_of_inorder_list[root.val]
        root.left = helper_func(left, index_of_root_val_in_inorder_list - 1)
        root.right = helper_func(index_of_root_val_in_inorder_list + 1, right)
        return root

    return helper_func(0, len(inorder) - 1)
