# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
def word_pattern(pattern: str, s: str) -> bool:
    letter_to_word_map = dict()
    words_in_s = s.split()
    for i, letter in enumerate(pattern):
        word = words_in_s[i]
        mapped_word_to_letter = letter_to_word_map.get(letter)
        if not mapped_word_to_letter:
            letter_to_word_map[letter] = word
            continue
        if mapped_word_to_letter != word:
            return False
        flipped_dict = {v: k for k, v in letter_to_word_map.items()}
        print(flipped_dict, letter_to_word_map)
        print({v: k for k, v in flipped_dict.items()}, letter_to_word_map)
        if {v: k for k, v in flipped_dict.items()} != letter_to_word_map:
            return False
    return True
