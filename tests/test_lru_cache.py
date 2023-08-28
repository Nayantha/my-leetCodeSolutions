from lru_cache import LRUCache


def test_case_i():
    lru_cache_object = LRUCache(2)
    lru_cache_object.put(1, 1)
    lru_cache_object.put(2, 2)
    lru_cache_object.get(1)
    lru_cache_object.put(3, 3)
    lru_cache_object.get(2)
    lru_cache_object.put(4, 4)
    lru_cache_object.get(1)
    lru_cache_object.get(3)
    lru_cache_object.get(4)
