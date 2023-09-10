# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
from typing import Optional, List

from data_structures.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.list = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            self.list[:] = [x for x in self.list if x is not None]
            return list(self.list)
        self.inorderTraversal(root.left)
        self.list.append(root.val)
        self.inorderTraversal(root.right)
        return self.list
