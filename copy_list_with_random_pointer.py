# https://leetcode.com/problems/copy-list-with-random-pointer/
from typing import Optional


class Node:
    def __init__(self, x: int, next_node: 'Node' = None, random_node: 'Node' = None):
        self.val = int(x)
        self.next_node = next_node
        self.random = random_node


def copy_random_list(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    Copy the given lined list in to new memory places
    and exchange the next and random node point to the new memory places.
    :param head: The head of the linked list that needed to be copied.
    :return: The head of the linked list with all the new memory locations.
    """
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
