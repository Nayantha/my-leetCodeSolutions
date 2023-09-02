# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import Optional

from data_structures.tree_node import TreeNode


def sum_numbers(root: Optional[TreeNode]) -> int:
    def dfs(curr, num):
        if not curr:
            return 0
        num = num * 10 + curr.val

    return dfs(root, 0)
