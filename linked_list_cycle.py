# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional
class LinkedList:
    def __init__(self):
        self.head: ListNode | None = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return self.val


def has_cycle(head: Optional[ListNode]) -> bool:
    nodes = set()
    temp_node = head
    while temp_node:
        if temp_node in nodes:
            return True
        nodes.add(temp_node)
        temp_node = temp_node.next
    return False
