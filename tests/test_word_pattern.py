import pytest


@pytest.mark.parametrize("pattern, s, expected", [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False)
])
def test_word_pattern(pattern: str, s: str, expected: bool):
    assert False
