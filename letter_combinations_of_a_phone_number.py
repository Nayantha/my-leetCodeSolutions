# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
def letter_combinations(digits: str) -> list[str]:
    digit_to_letter_dict = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }
    combination_list = []

    def backtrack(i: int, current_str):
        if len(current_str) == len(digits):
            combination_list.append(current_str)
            return
        for letter in digit_to_letter_dict[int(digits[i])]:  # str
            backtrack(i + 1, current_str + letter)

    if digits:
        backtrack(0, "")
        return combination_list
    else:
        return []
