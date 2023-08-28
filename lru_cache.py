# https://leetcode.com/problems/lru-cache/
from collections import OrderedDict
from typing import Optional


class Node:
    def __init__(self, value: int = 0, key: int = 0):
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

    def remove(self, node: Node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node: Node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

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
        self.insert(self.key_value_map_cache[key])
        if len(self.key_value_map_cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.key_value_map_cache[lru.key]


class LRUCacheII:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache_map = OrderedDict()

    def get(self, key):
        if key in self.cache_map:
            self.cache_map.move_to_end(key)
            return self.cache_map[key]
        else:
            return -1

    def push(self, key, value):
        if key in self.cache_map:
            self.cache_map[key] = value
            self.cache_map.move_to_end(key)
        else:
            if self.size < self.capacity:
                self.size += 1
                self.cache_map[key] = value
            else:
                self.cache_map.popitem(False)
                self.cache_map[key] = value
