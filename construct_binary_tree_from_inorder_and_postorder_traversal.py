# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import Optional

from data_structures.tree_node import TreeNode


def build_tree(inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
    if not postorder or not inorder:
        return None
    mid = inorder.index(postorder.pop())
    root = TreeNode(inorder[mid])
    root.left = build_tree(inorder[:mid], postorder)
    root.right = build_tree(inorder[mid + 1:], postorder)
