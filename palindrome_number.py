# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        rev_x = x[::-1]
        if x == rev_x:
            return True
        return False
        # x = str(x)
        # len_x = len(x)
        # for i in range(int(len_x / 2)):
        #     if x[i] != x[len_x - 1 - i]:
        #         return False
        # return True


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x = list(str(x))
#         rev_x = x[::-1]
#         if x == rev_x:
#             return True
#         return False
