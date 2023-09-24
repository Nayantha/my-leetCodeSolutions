# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class TrieNode:
    def __init__(self):
        self.letter_collections = {}
        self.is_last_letter = False


class Trie:

    def __init__(self):
        self._word: str = ""

    def insert(self, word: str) -> None:
        self._word = word

    def search(self, word: str) -> bool:
        if word == self._word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return self._word.startswith(prefix)
