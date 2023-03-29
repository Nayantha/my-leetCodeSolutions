# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not (0 < len(strs) < 201):
            return ""
        if any(word for word in strs if not(-1 < len(word) < 201)):
            return ""
        strs = [word.lower() for word in strs]
        letters = len([*min(strs, key=len)])
        longest_common_prefix_word = ""
        for i in range(0, letters):
            same_index_letters = [word[i] for word in strs]
            if same_index_letters.count(same_index_letters[0]) == len(same_index_letters):
                longest_common_prefix_word += same_index_letters[0]
            else:
                return longest_common_prefix_word
        return longest_common_prefix_word
