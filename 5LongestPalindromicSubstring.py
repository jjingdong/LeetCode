'''
5. Longest Palindromic Substring
Medium

6175

500

Add to List

Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution:

    # Note this is not done

    # This is not the solution!!
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(s: str) -> str:
            reverseS = "".join(reversed(s))
            if reverseS == s:
                return True
            return False

        i, j = 0, len(s)
        range = s[i:j]
        if isPalindrome(range):
            return range
        else:
            return self.longestPalindrome(s[i + 1:j]) or self.longestPalindrome(s[i:j - 1])










