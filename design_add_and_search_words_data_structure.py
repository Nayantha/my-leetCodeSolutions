# https://leetcode.com/problems/design-add-and-search-words-data-structure/
from implement_trie import TrieNode
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        ...

    def search(self, word: str) -> bool:
        ...
