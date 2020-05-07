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

    # Note this is not done --------------> I need to use Dynamic Programming, instead of cacheing!!@@@@@
    def longestPalindrome(self, s: str) -> str:

        def find(i, j):
            nonlocal max_count, start

            if cache[i][j] != 0:
                return cache[i][j]
            elif i == j:
                cache[i][j] = 1
                if max_count < cache[i][j]:
                    max_count = cache[i][j]
                    start = i
                return cache[i][j]
            elif i == j - 1 and s[i] == s[j]:
                cache[i][j] = 2
                if max_count < cache[i][j]:
                    max_count = cache[i][j]
                    start = i
                return cache[i][j]
            elif s[i] == s[j]:
                cache[i][j] = 2 + find(i + 1, j - 1)
                if max_count < cache[i][j]:
                    max_count = cache[i][j]
                    start = i
                return cache[i][j]

            find(i + 1, j)
            find(i, j - 1)

        if s is None: return None
        if s == '': return ''

        max_count = 0
        start = 0
        cache = [[0 for x in range(len(s))] for y in range(len(s))]
        find(0, len(s) - 1)

        # print(cache)
        # print(max_count)
        # print(start)

        return s[start: start + max_count]

#     # This is not the solution!!
#     def longestPalindrome(self, s: str) -> str:

#         def isPalindrome(s: str) -> str:
#             reverseS = "".join(reversed(s))
#             if reverseS == s:
#                 return True
#             return False

#         i, j = 0, len(s)
#         range = s[i:j]
#         if isPalindrome(range):
#             return range
#         else:
#             return self.longestPalindrome(s[i+1:j]) or self.longestPalindrome(s[i:j-1])





















