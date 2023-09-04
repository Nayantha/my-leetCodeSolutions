# https://leetcode.com/problems/count-complete-tree-nodes/
from typing import Optional

from data_structures.tree_node import TreeNode


def count_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
