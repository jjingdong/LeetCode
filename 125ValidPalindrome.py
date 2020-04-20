# 125. Valid Palindrome
# Easy
#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
#
# Input: "race a car"
# Output: false

class Solution:

    # Input: "A man, a plan, a canal: Panama"
    #         i = 0
    #                                      j = len - 1
    # Output: true

    # Time O(N/2)
    # Space O(1)
    def isPalindrome(self, s: str) -> bool:

        if s is None: return False
        if s == []: return True
        if len(s) == 1: return True

        length = len(s)

        i = 0
        j = length - 1
        while i <= j:

            curI = s[i]  # 0
            curJ = s[j]  # p

            if not curI.isalnum():
                i += 1  # i = 1
            elif not curJ.isalnum():
                j -= 1
            elif curI.lower() != curJ.lower():
                return False
            elif curI.lower() == curJ.lower():
                i += 1
                j -= 1

        return True