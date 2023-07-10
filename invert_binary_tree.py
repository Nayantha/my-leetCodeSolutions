# https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

from binary_tree_inorder_traversal import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    invert(root)
    return root


def invert(node: Optional[TreeNode]):
    if node:
        node.right, node.left = node.left, node.right
        invert(node.right)
        invert(node.left)
