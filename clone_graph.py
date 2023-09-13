# https://leetcode.com/problems/clone-graph/description/
import copy
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional['Node']) -> Optional['Node']:
    return copy.deepcopy(node)
