# https://leetcode.com/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False
    if not root.left and root.right and root.val == target_sum:
        return True
    current_sum = target_sum - root.val
    return has_path_sum(root.left, current_sum) or has_path_sum(root.right, current_sum)
