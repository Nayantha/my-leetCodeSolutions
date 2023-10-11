# https://leetcode.com/problems/design-add-and-search-words-data-structure/
from implement_trie import TrieNode
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        current_node = self.root
        for letter in word:
            if letter not in current_node.letter_collections:
                current_node.letter_collections[letter] = TrieNode()
            current_node = current_node.letter_collections[letter]
        current_node.is_last_letter = True

    def search(self, word: str) -> bool:
        def dfs(j: int, root: TrieNode):
            current_node = root
            for i in range(j, len(word)):
                letter = word[i]
                if letter == ".":
                    for letter_collection in current_node.letter_collections.values():
                        if dfs(i + 1, letter_collection):
                            return True
                    return False
                else:
                    if letter not in current_node.letter_collections:
                        return False
                    current_node = current_node.letter_collections[letter]
            return current_node.is_last_letter

        return dfs(0, self.root)
