# https://leetcode.com/problems/lru-cache/
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.evict_key = 0

    def get(self, key: int) -> int:
        value = self.map.get(key)
        return value if value else -1

    def put(self, key: int, value: int) -> None:
        if len(self.map.keys()) >= self.capacity:
            del self.map[self.evict_key]
        self.evict_key = list(self.map.keys())[-1] if self.map.keys() else key
        self.map[key] = value
