# https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
def int_to_roman(num: int) -> str:
    result_str = ""
    while num > 0:
        if num > 1000:
            num -= 1000
            result_str += "M"
        elif num > 500:
            num -= 500
            result_str += "D"
        elif num > 100:
            num -= 100
            result_str += "C"
        elif num > 50:
            num -= 50
            result_str += "L"
        elif num > 10:
            num -= 10
            result_str += "X"
        elif num > 5:
            num -= 5
            result_str += "V"
        else:
            num -= 1
            result_str += "I"
    if "IIII" in result_str:
        result_str = result_str.replace("IIII", "IV")
    if "VIV" in result_str:
        result_str = result_str.replace("VIV", "IX")
    return result_str
