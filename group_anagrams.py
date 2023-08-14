# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
def group_anagrams(strs: list[str]) -> list[list[str]]:
    res: list[list[str]] = []
    letters_used_in_each_word = list()
    for word in strs:
        letters_used = sorted([letter for letter in word])
        if letters_used not in letters_used_in_each_word:
            letters_used_in_each_word.append(letters_used)
        try:
            res[letters_used_in_each_word.index(letters_used)].append(word)
        except IndexError:
            res.insert(letters_used_in_each_word.index(letters_used), [word])
    return res
