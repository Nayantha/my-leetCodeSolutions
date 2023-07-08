# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
def word_pattern(pattern: str, s: str) -> bool:
    letter_to_word_map = dict()
    words_in_s = s.split()

    if len(pattern) != len(words_in_s):
        return False

    if len(set(pattern)) != len(set(words_in_s)):
        return False

    for i, letter in enumerate(pattern):
        word = words_in_s[i]
        mapped_word_to_letter = letter_to_word_map.get(letter)
        if letter not in letter_to_word_map and word not in letter_to_word_map.values():
            letter_to_word_map[letter] = word
            continue
        if mapped_word_to_letter != word:
            return False
    return True
