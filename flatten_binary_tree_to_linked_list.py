# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
from typing import Optional

from data_structures.tree_node import TreeNode


def flatten(root: Optional[TreeNode]) -> None:
    def dfs(root):
        if not root:
            return
        lefttail = dfs(root.left)
        righttail = dfs(root.right)
        if lefttail:
            lefttail.right = root.right
            root.right = root.left
            root.left = None
        return righttail or lefttail or root

    dfs(root)
