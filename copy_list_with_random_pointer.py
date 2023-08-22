# https://leetcode.com/problems/copy-list-with-random-pointer/
from typing import Optional


class Node:
    def __init__(self, x: int, next_node: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next_node = next_node
        self.random = random


def copy_random_list(self, head: 'Optional[Node]') -> 'Optional[Node]':
    ...
