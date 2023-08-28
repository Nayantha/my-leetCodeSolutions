# https://leetcode.com/problems/lru-cache/
class LRUCache:
    map = {}

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        ...

    def put(self, key: int, value: int) -> None:
        ...
