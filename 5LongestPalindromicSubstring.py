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

    # Solution: DP
    #
    # Solution: DP optimized. Note. I didn't implement
    #
    # Note. this question is similar to 516. Longest Palindromic Subsequence

    # Time O(MN) Space O(MN)
    # Runtime 3532 ms
    def longestPalindrome(self, s: str) -> str:

        if s is None: return None
        if s == '': return ''

        cache = [[None for x in range(len(s))] for y in range(len(s))]
        count = 0
        start = 0

        for i in range(len(s)):
            cache[i][i] = True
            count = 1
            start = i

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                cache[i][i + 1] = True
                count = 2
                start = i

        for j in range(len(s)):
            for i in range(0, j - 1):
                if s[i] == s[j] and cache[i + 1][j - 1] == True:
                    cache[i][j] = True
                    if count < j - i + 1:
                        count = j - i + 1
                        start = i

        return s[start: start + count]


'''
    # Time O(MN) Space O(MN)
    # Note this runtime is 9596 ms
    def longestPalindrome(self, s: str) -> str:

        def is_palindrome(i, j):
            nonlocal start, count

            if cache[i][j] is not None:
                return cache[i][j]
            elif i == j: 
                if count < 1:
                    count = 1
                    start = i
                cache[i][j] = True
            elif j == i + 1 and s[i] == s[j]: 
                if count < 2:
                    count = 2
                    start = i
                cache[i][j] = True
            elif s[i] == s[j]:
                cache[i][j] = is_palindrome(i+1, j-1)
                if cache[i][j] == True:
                    if count < j - i + 1:
                        count = j - i + 1
                        start = i
            else:
                cache[i][j] = False

            return cache[i][j]


        if s is None: return None
        if s == '': return ''

        cache = [[None for x in range(len(s))] for y in range(len(s))]
        count = 0
        start = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                is_palindrome(i, j)

        return s[start: start+count]
'''
