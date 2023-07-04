# https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
def can_construct(ransom_note: str, magazine: str) -> bool:
    for letter in ransom_note:
        if letter not in magazine:
            return False
        else:
            magazine = magazine.replace(letter, "")
    return True
