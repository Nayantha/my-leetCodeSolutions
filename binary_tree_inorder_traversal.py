# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


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
