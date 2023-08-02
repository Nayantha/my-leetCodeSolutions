# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150
def reverse_words(s: str) -> str:
    return " ".join(s.strip().split()[::-1])


def reverse_words_ii(s: str) -> str:
    res = []
    word = ""
    for letter in s:
        if letter == " ":
            if not word:
                res.append(word)
            word = ""
        word += letter
    return " ".join(res[::-1])
