# https://leetcode.com/problems/implement-trie-prefix-tree/description/
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
        if prefix in self._word:
            return True
        return False
