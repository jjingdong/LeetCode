'''
1092. Shortest Common Supersequence
Hard

Given two strings str1 and str2, return the shortest string that has both str1
and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters
from T (possibly 0, and the characters are chosen anywhere from T) results in
the string S.)

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.


Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
'''


class Solution:

    #         str1 = "abac", str2 = "cab"
    #         result = "cabac"   -> shortest

    #                  abac, cab, result=""
    #                 /                       \
    #         bac, cab, result="a"            abac, ab, result="c"
    #                     /           \
    # ac, cab, result="ab"            bac, ab, result="ac"
    #     /                       \
    # c, cab, result="aba"      ac,ab, result="abc"
    #                                   |
    #                         c,b, result="abca" (only 1 branch if str[i]==str[j]), i++, j++

    #                 j=0
    #                         c       a       b
    #                ''       c       ca      cab
    #     i       a  a        ac      aca     acab
    #             b  ab
    #             a  aba
    #             c  abac

    #             dp[0][0] = ''
    #             if char_1 == char_2:
    #                 str[i-1] == str[j-1]

    #                 dp[i][j] = dp[i-1][j-1] + str[i-1]
    #             else:
    #                 dp[i][j] = min(
    #                             dp[i-1][j]) + str[i-1]
    #                             dp[i][j-1] + str[j-1])

    # Time O() Space O()
    # This is not done
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        if str1 == '': return str2
        if str2 == '': return str1

        size = len(str1)
        col_size = len(str2)
        dp = [['*' for _ in range(col_size + 1)] for _ in range(size + 1)]

        for r in range(size + 1):
            for c in range(col_size + 1):
                if r == 0 and c == 0:
                    dp[r][c] = ''
                elif r == 0:
                    dp[r][c] = dp[r][c - 1] + str2[c - 1]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c] + str1[r - 1]
                else:
                    if str1[r - 1] == str2[c - 1]:
                        dp[r][c] = dp[r - 1][c - 1] + str1[r - 1]
                    else:
                        dp[r][c] = min(dp[r - 1][c] + str1[r - 1], dp[r][c - 1] + str2[c - 1])

        for r in range(size + 1):
            print(dp[r])

        return dp[-1][-1]

