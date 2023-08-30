# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import Optional

from data_structures.tree_node import TreeNode


def build_ree(inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
    if not postorder or not inorder:
        return None
    root = TreeNode(postorder[-1])
    mid = inorder.index(postorder[-1])
    root.left = build_ree(inorder[:mid], postorder)
    root.right = build_ree(inorder[mid + 1:], postorder)
