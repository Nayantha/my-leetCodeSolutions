# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class TrieNode:
    def __init__(self):
        self.letter_collections = {}
        self.is_last_letter = False


class Trie:

    def __init__(self):
        self.root_node: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        self.root_node = word

    def search(self, word: str) -> bool:
        if word == self.root_node:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return self.root_node.startswith(prefix)
