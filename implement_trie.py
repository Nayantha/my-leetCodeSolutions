# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class TrieNode:
    def __init__(self):
        self.letter_collections = {}
        self.is_last_letter = False


class Trie:

    def __init__(self):
        self.letter_collection: str = ""

    def insert(self, word: str) -> None:
        self.letter_collection = word

    def search(self, word: str) -> bool:
        if word == self.letter_collection:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return self.letter_collection.startswith(prefix)
