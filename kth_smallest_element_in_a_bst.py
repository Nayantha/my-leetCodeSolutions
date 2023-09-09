# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional

from data_structures.tree_node import TreeNode


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    node_stack = []
    current_node = root
    index_of_the_number = 0
    return index_of_the_number
