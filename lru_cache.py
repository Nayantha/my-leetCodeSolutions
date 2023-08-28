# https://leetcode.com/problems/lru-cache/
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.map.get(key)
        return value if value else -1

    def put(self, key: int, value: int) -> None:
        key_list = self.map.keys()
        if len(key_list) > 2:
            del self.map[key_list[-1]]
        self.map[key] = value
