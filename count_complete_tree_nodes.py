# https://leetcode.com/problems/count-complete-tree-nodes/
from typing import Optional

from data_structures.tree_node import TreeNode


def count_nodes(root: Optional[TreeNode]) -> int:
    def inorder_traversal(node, count):
        if node:
            count += 1
            inorder_traversal(node.left, count)
            inorder_traversal(node.right, count)
