# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
from typing import Optional

from data_structures.tree_node import TreeNode


def flatten(root: Optional[TreeNode]) -> None:
    if not root:
        return
    right_tree: Optional[TreeNode] = root.right
    left_tree: Optional[TreeNode] = root.left
    root.right = root.left
    root.left = None
    while left_tree.right:
        left_tree = left_tree.right
    left_tree.right = right_tree
