# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import Optional

from data_structures.tree_node import TreeNode


def build_tree(inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
    if not postorder or not inorder:
        return None
    values_to_index_map_of_inorder_list = {value: index for index, value in enumerate(inorder)}

    def helper_func(left, right):
        ...

    return helper_func(0, len(inorder) - 1)
