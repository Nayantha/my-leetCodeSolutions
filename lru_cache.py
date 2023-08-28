# https://leetcode.com/problems/lru-cache/
from typing import Optional


class Node:
    def __int__(self, value: int = 0, key: int = 0):
        self.value: int = value
        self.key: int = key
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.key_value_map_cache: dict[int: Node] = {}
        self.capacity = capacity
        self.left = Node()  # least recently used
        self.right = Node()  # most recently used
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        ...

    def insert(self, node):
        ...

    def get(self, key: int) -> int:
        if key in self.key_value_map_cache:
            self.remove(self.key_value_map_cache[key])
            self.insert(self.key_value_map_cache[key])
            return self.key_value_map_cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_value_map_cache:
            self.remove(self.key_value_map_cache[key])
        self.key_value_map_cache[key] = Node(value, key)
