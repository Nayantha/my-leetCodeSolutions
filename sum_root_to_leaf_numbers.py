# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import Optional

from data_structures.tree_node import TreeNode


def sum_numbers(root: Optional[TreeNode]) -> int:
    def dfs(curr, num):
        if not curr:
            num = num * 10 + curr.left + num * 10 + curr.right
            dfs(curr.left, num)
            dfs(curr.right, num)
        return num

    return dfs(root, 0)
