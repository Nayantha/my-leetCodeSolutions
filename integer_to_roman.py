# https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
def int_to_roman(num: int) -> str:
    result_str = ""
    int_to_roman_dict = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }
    for roman_mirror_int in list(int_to_roman_dict.keys())[::-1]:
        while num >= roman_mirror_int:
            result_str += int_to_roman_dict[roman_mirror_int]
            num -= roman_mirror_int
    return result_str
