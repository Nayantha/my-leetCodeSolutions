# https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

def is_palindrome(s: str) -> bool:
    # processed_str = "".join([letter.lower() for letter in s if letter.isalnum()])
    processed_str = [letter.lower() for letter in s if letter.isalnum()]
    return processed_str == processed_str[::-1]


def is_palindrome_two_pointers(s: str) -> bool:
    processed_str = [letter.lower() for letter in s if letter.isalnum()]
    left = 0
    right = len(processed_str) - 1
    while left <= right:
        if processed_str[left] != processed_str[right]:
            return False
        left += 1
        right -= 1
    return True
