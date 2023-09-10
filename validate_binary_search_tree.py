# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional

from data_structures.tree_node import TreeNode


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def is_valid(node: Optional[TreeNode], left_boundary: int, right_boundary: int):
        ...
