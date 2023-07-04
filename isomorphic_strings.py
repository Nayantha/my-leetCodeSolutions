# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150
def is_isomorphic(s: str, t: str) -> bool:
    if len(set(s)) != len(set(t)):
        return False
    hash_map = dict()
    for letter_in_s, letter_in_t in zip(s, t):
        dict_value = hash_map.get(letter_in_s, None)
        if not dict_value:
            hash_map[letter_in_s] = letter_in_t
        elif dict_value != letter_in_t:
            return False
    return True
