# https://leetcode.com/problems/binary-tree-right-side-view/
from collections import deque
from typing import Optional

from data_structures.tree_node import TreeNode


def right_side_view(root: Optional[TreeNode]) -> list[int]:
    right_node_values: list[int] = []
    queue = deque([root])
    while queue:
        right_side = None
        queue_length = len(queue)

        for i in range(queue_length):
            node = queue.popleft()
            if node:
                right_side = node
                queue.append(node.left)
                queue.append(node.right)
        if right_side:
            right_node_values.append(right_side.val)
    return right_node_values
