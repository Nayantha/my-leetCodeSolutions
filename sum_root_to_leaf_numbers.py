# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import Optional

from data_structures.tree_node import TreeNode


def sum_numbers(root: Optional[TreeNode]) -> int:
    def dfs(curr, num):
        if not curr:
            return 0
        num = num * 10 + curr.val
        if not curr.left and not curr.right:
            return num
        return dfs(curr.left, num) + dfs(curr.right, num)

    return dfs(root, 0)


def sum_numbers_ii(root: Optional[TreeNode]) -> int:
    def pre_order_share_value(cur: Optional[TreeNode], value: str):
        if not cur:
            return 0
