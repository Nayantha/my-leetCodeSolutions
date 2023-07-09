# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    def traverse(root: Optional[TreeNode], depth: int):
        if not root:
            return depth
        return max(traverse(root.left, depth + 1), traverse(root.right, depth + 1))

    return traverse(root, 0)
