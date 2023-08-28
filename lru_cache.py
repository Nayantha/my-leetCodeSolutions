# https://leetcode.com/problems/lru-cache/
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.map.get(key)
        return value if value else -1

    def put(self, key: int, value: int) -> None:
        self.map[key] = value
