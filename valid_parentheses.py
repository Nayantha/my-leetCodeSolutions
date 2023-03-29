# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def __init__(self):
        self.parentheses_dict = {
            "bracket": {
                "open" : '(',
                "close": ')'
            },
            "curley" : {
                "open" : '{',
                "close": '}'
            },
            "square" : {
                "open" : '[',
                "close": ']'
            }
        }
        self.parenthesis_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        self.parenthesis_list = ['(', ')', '{', '}', '[', ']']
        self.valid_parentheses = ["()", "{}", "[]"]
    
    def isValid(self, s: str) -> bool:
        if not (0 < len(s) < 10 ** 4):
            return False
        for letter in s:
            if letter not in self.parenthesis_list:
                return False
        
        return self.remove_parentheses(s=s)
    
    def remove_parentheses(self, s: str) -> bool:
        while True:
            if '()' in s:
                s = s.replace('()', '')
            elif '{}' in s:
                s = s.replace('{}', '')
            elif '[]' in s:
                s = s.replace('[]', '')
            else:
                return not s
