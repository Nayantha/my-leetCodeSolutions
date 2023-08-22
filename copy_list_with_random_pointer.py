# https://leetcode.com/problems/copy-list-with-random-pointer/
import random
from typing import Optional


class Node:
    def __init__(self, x: int, next_node: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next_node = next_node
        self.random = random


def copy_random_list(self, head: 'Optional[Node]') -> 'Optional[Node]':
    list_values: list[Node] = []
    while head:
        list_values.append(head)
        head = head.next_node
    new_head = list_values[0]
    for node in list_values.copy():
        rand_node = random.choices(list_values)
        node.random = rand_node
        list_values.remove(rand_node)
    return new_head
