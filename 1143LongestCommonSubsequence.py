'''
1143. Longest Common Subsequence
Medium

Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with
some characters (can be none) deleted without changing the relative order of the
 remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''


class Solution:

    # Solution I: Brute Force
    #
    # Solution II: Dynamic Programming - Memorization
    #
    # Solution III: Dynamic Programming - Tabulation

    #     Eg1. abcde
    #          ace
    #          output = ace
    #
    #     Eg2. abc
    #          abc
    #          output = abc
    #
    #     Eg3. abc
    #          def
    #          output = 0

    #         for i in range(1,size1):
    #             for j in range(1, size2):
    #                 if text1[i] == text2[j]:
    #                     dp[i][j] = dp[i-1][j-1] + 1
    #                 else:
    #                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Time O(MN) Space O(MN)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # m, n = len(text1),len(text2)
        # dp = [ [0]*(n+1) for i in range(m+1)]
        # # fill out the 2D table
        # for i in range(m):
        #     for j in range(n):
        #         if text1[i]==text2[j]:
        #             dp[i+1][j+1]=dp[i][j]+1
        #         else:
        #             dp[i+1][j+1]= max(dp[i+1][j],dp[i][j+1])
        # return int(dp[m][n])

        if not text1 or not text2: return None

        col_size = len(text1)
        size = len(text2)

        dp = [[0 for _ in range(col_size + 1)] for _ in range(size + 1)]

        for i in range(size):
            for j in range(col_size):
                if text2[i] == text1[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        # print(dp)
        # text1 = 'abcde'
        # text2 = 'ace'
        # dp = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 2, 2, 2], [0, 1, 1, 2, 2, 3]]

        return dp[-1][-1]