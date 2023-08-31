# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    if not root:
        return root
    queue = deque([root])
