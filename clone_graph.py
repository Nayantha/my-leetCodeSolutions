# https://leetcode.com/problems/clone-graph/description/
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None
    if not node.neighbors:
        return Node(node.val)
    old_to_new_node_map = {}
    new_node = Node(node.val)
    old_to_new_node_map[node] = new_node
    old_node_queue = deque([node])
    while old_node_queue:
        next_node = old_node_queue.popleft()
    return new_node
