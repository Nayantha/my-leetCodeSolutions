# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque
from typing import Optional

from data_structures.tree_node import TreeNode


def zigzag_level_order(root: Optional[TreeNode]) -> list[list[int]]:
    res: list[list[int]] = []
    tree_nodes = deque([root])
    while tree_nodes:
        level_nodes = []
        for i in range(len(tree_nodes)):
            node = tree_nodes.popleft()
            if node:
                level_nodes.append(node.val)
                tree_nodes.append(node.left)
                tree_nodes.append(node.right)
        if level_nodes:
            res.append(level_nodes[::-1])
    return res
