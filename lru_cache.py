# https://leetcode.com/problems/lru-cache/
from typing import Optional


class Node:
    def __int__(self, value: int, key: int):
        self.value: int = value
        self.key: int = key
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.evict_key = 0

    def get(self, key: int) -> int:
        value = self.map.get(key)
        key_list = list(self.map.keys())
        key_list.remove(key)
        self.evict_key = key_list[0]
        return value if value != None else -1

    def put(self, key: int, value: int) -> None:
        if len(self.map) >= self.capacity:
            del self.map[self.evict_key]
            self.evict_key = list(self.map.keys())[0] if self.map.keys() else key
            self.map[key] = value
        else:
            self.map[key] = value
            self.evict_key = list(self.map.keys())[0] if self.map.keys() else key
