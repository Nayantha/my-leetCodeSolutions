# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional

from data_structures.tree_node import TreeNode


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def is_valid(node: Optional[TreeNode], left_boundary: int, right_boundary: int):
        if not node:
            return True
        if not (left_boundary < node.val < right_boundary):
            return False
        return is_valid(node.left, left_boundary, node.val) and is_valid(node.right, node.val, right_boundary)
    return is_valid(root, int("-inf"), int("-inf"))
