import pytest

from group_anagrams import group_anagrams


@pytest.mark.parametrize("strs, expected", [
    (["eat","tea","tan","ate","nat","bat"], )
])
def test_group_anagrams(strs: list[str], expected: list[list[str]]):
    assert group_anagrams(strs) == expected
