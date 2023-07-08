# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
def word_pattern(pattern: str, s: str) -> bool:
    letter_to_word_map = dict()
    words_in_s = s.split()
    for i, letter in enumerate(pattern):
        mapped_word_to_letter = letter_to_word_map.get(letter)
        if not mapped_word_to_letter:
            letter_to_word_map[letter] = words_in_s[i]
            continue
        if mapped_word_to_letter != words_in_s[i]:
            return False
    return True
