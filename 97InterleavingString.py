'''
97. Interleaving String
Hard

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving
of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided
into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lower-case English letters.
'''


class Solution:

    #         s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    #               i             j
    #                     k
    #                     a
    #             /           |           \
    #         k==i          k==j         k!=i and k!=j
    #        adbbcbcac
    #         vs
    #         abcc
    #      /  |   \
    # k==i
    # dbbcbcac
    # bcc

    # This is not done
    # Time O() Space O()
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        size = len(s1)
        col_size = len(s2)
        dp = [[False for _ in range(col_size + 1)] for _ in range(size + 1)]
        dp[0][0] = True

        # for r in range(size+1):
        #     print(dp[r])

        index = 0
        for r in range(size + 1):
            for c in range(col_size + 1):
                if r == 0:
                    if s3[index] == s1[r]:
                        dp[r][c] = dp[r - 1][c]
                    else:
                        dp[r][c] = False
                elif c == 0:
                    if s3[index] == s2[r]:
                        dp[r][c] = dp[r][c - 1]
                else:
                    if s3[index] != s1[r] and s3[index] != s2[r]:
                        dp[r][c] = False
                    else:
                        option1 = dp[r - 1][c] and s3[index] == s1[r]
                        option1 = dp[r][c - 1] and s3[index] == s2[r]
                        dp[r][c] = option1 or option2

        for r in range(size + 1):
            print(dp[r])

        return dp[-1][-1]


