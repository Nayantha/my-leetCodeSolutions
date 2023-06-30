# https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

def is_palindrome(s: str) -> bool:
    # processed_str = "".join([letter.lower() for letter in s if letter.isalnum()])
    processed_str = [letter.lower() for letter in s if letter.isalnum()]
    return processed_str == processed_str[::-1]
