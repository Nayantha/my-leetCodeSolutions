# https://leetcode.com/problems/copy-list-with-random-pointer/
from typing import Optional


class Node:
    def __init__(self, x: int, next_node: 'Node' = None, random_node: 'Node' = None):
        self.val = int(x)
        self.next_node = next_node
        self.random = random_node


def copy_random_list(self, head: 'Optional[Node]') -> 'Optional[Node]':
    copy_of_the_list = {None: Node}  # old_node: new_node
    cur = head
    while cur:
        new_node = Node(cur.val)
        copy_of_the_list[cur] = new_node
        cur = cur.next_node
    cur = head
    while cur:
        node = copy_of_the_list[cur]
        node.next_node = copy_of_the_list[cur.next_node]
        node.random = copy_of_the_list[cur.random]
        cur = cur.next_node
    return copy_of_the_list[head]
