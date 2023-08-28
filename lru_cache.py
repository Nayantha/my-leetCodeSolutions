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
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        value = self.key_value_map_cache.get(key)
        key_list = list(self.key_value_map_cache.keys())
        key_list.remove(key)
        self.evict_key = key_list[0]
        return value if value != None else -1

    def put(self, key: int, value: int) -> None:
        if len(self.key_value_map_cache) >= self.capacity:
            del self.key_value_map_cache[self.evict_key]
            self.evict_key = list(self.key_value_map_cache.keys())[0] if self.key_value_map_cache.keys() else key
            self.key_value_map_cache[key] = value
        else:
            self.key_value_map_cache[key] = value
            self.evict_key = list(self.key_value_map_cache.keys())[0] if self.key_value_map_cache.keys() else key
