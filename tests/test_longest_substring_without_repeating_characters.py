import pytest

from longest_substring_without_repeating_characters import length_of_longest_substring


@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("au", 2),
    (" ", 1)
])
def test_length_of_longest_substring(s: str, expected: int):
    assert length_of_longest_substring(s) == expected
