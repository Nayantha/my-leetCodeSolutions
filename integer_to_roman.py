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


def int_to_roman_ii(num: int) -> str:
    result_str = ""
    while num > 0:
        if num >= 1000:
            num -= 1000
            result_str += "M"
        elif num >= 900:
            num -= 900
            result_str += "CM"
        elif num >= 500:
            num -= 500
            result_str += "D"
        elif num >= 400:
            num -= 400
            result_str += "CD"
        elif num >= 100:
            num -= 100
            result_str += "C"
        elif num >= 90:
            num -= 90
            result_str += "XC"
        elif num >= 50:
            num -= 50
            result_str += "L"
        elif num >= 40:
            num -= 40
            result_str += "XL"
        elif num >= 10:
            num -= 10
            result_str += "X"
        elif num >= 9:
            num -= 9
            result_str += "IX"
        elif num >= 5:
            num -= 5
            result_str += "V"
        elif num >= 4:
            num -= 4
            result_str += "IV"
        else:
            num -= 1
            result_str += "I"
    return result_str
