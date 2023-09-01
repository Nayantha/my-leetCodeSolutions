# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
from typing import Optional

from data_structures.tree_node import TreeNode


def flatten(root: Optional[TreeNode]) -> None:
    def dfs(root):
        if not root:
            return
        left_tail = dfs(root.left)
        right_tail = dfs(root.right)
        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        return right_tail or left_tail or root

    dfs(root)
