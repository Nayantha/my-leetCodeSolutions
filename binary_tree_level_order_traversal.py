# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
from typing import Optional

from data_structures.tree_node import TreeNode


def level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
    res: list[list[int]] = []
    node_queue = deque([root])
    while node_queue:
        level_nodes = []
        for i in range(len(node_queue)):
            node = node_queue.popleft()
            if node:
                level_nodes.append(node.val)
                node_queue.append(node.left)
                node_queue.append(node.right)
        if level_nodes:
            res.append(level_nodes)
    return res
