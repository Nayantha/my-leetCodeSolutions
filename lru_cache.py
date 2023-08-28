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
        self.key_value_map_cache = {}
        self.capacity = capacity
        self.left = Node()  # least recently used
        self.right = Node()  # most recently used
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.key_value_map_cache:
            return self.key_value_map_cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.key_value_map_cache) >= self.capacity:
            del self.key_value_map_cache[self.evict_key]
            self.evict_key = list(self.key_value_map_cache.keys())[0] if self.key_value_map_cache.keys() else key
            self.key_value_map_cache[key] = value
        else:
            self.key_value_map_cache[key] = value
            self.evict_key = list(self.key_value_map_cache.keys())[0] if self.key_value_map_cache.keys() else key
