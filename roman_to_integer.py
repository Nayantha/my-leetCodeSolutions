# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def roman_to_int(self, s: str) -> int:
        s = s.upper()
        if len(s) > 15:
            s = s[:15]
        for letter in s:
            if letter not in ('I', 'V', 'X', 'L', 'C', 'D', 'M'):
                s = s.replace(letter, "")
        number = 0
        i = 0
        if "IV" in s:
            s = s.replace("IV", "")
            number += 4
        if "IX" in s:
            s = s.replace("IX", "")
            number += 9
        if "XL" in s:
            s = s.replace("XL", "")
            number += 40
        if "XC" in s:
            s = s.replace("XC", "")
            number += 90
        if "CD" in s:
            s = s.replace("CD", "")
            number += 400
        if "CM" in s:
            s = s.replace("CM", "")
            number += 900
        while i < len(s):
            if s[i] == "I":
                number += 1
            elif s[i] == "V":
                number += 5
            elif s[i] == "X":
                number += 10
            elif s[i] == "L":
                number += 50
            elif s[i] == "C":
                number += 100
            elif s[i] == "D":
                number += 500
            elif s[i] == "M":
                number += 1000
            i += 1
        return number
