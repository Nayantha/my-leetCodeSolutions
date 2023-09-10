# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional

from data_structures.tree_node import TreeNode


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    if root.left and root.right:
        return root.left.val < root.val < root.right.val and is_valid_bst(root.left) and is_valid_bst(root.right)
    elif not root.left and not root.right:
        return True
    elif root.left or root.right:
        return False
