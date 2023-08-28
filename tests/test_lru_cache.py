from lru_cache import LRUCache


def test_case_i():
    lru_cache_object = LRUCache(2)
    lru_cache_object.put(1, 1)
    assert lru_cache_object.map == {1: 1}
    lru_cache_object.put(2, 2)
    assert lru_cache_object.map == {1: 1, 2: 2}
    assert lru_cache_object.get(1) == 1
    lru_cache_object.put(3, 3)
    assert lru_cache_object.map == {1: 1, 3: 3}
    assert lru_cache_object.get(2) == -1
    lru_cache_object.put(4, 4)
    assert lru_cache_object.map == {4: 4, 3: 3}
    assert lru_cache_object.get(1) == -1
    assert lru_cache_object.get(3) == 3
    assert lru_cache_object.get(4) == 4
