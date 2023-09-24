# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class TrieNode:
    def __init__(self):
        self.letter_collections = {}
        self.is_last_letter = False


class Trie:

    def __init__(self):
        self.root_node: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        current_node: TrieNode = self.root_node
        for letter in word:
            if letter not in current_node.letter_collections:
                current_node.letter_collections[letter] = TrieNode()

    def search(self, word: str) -> bool:
        if word == self.root_node:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return self.root_node.startswith(prefix)
