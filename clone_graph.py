# https://leetcode.com/problems/clone-graph/description/
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional['Node']) -> Optional['Node']:
    old_node_to_new_node_map = dict()

    def clone_node(old_node: Node):
        if old_node in old_node_to_new_node_map:
            return old_node_to_new_node_map[old_node]
        new_node = Node(old_node.val)
        old_node_to_new_node_map[old_node] = new_node
        for neighbour_node in old_node.neighbors:
            new_node.neighbors.appenddfs(neighbour_node)
        return new_node
    return clone_node(node)
