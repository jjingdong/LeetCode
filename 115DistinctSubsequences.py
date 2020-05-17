'''
115. Distinct Subsequences
Hard

Given a string S and a string T, count the number of distinct subsequences of S which equals T.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
It's guaranteed the answer fits on a 32-bit signed integer.
Example 1:
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
'''


class Solution:

    # Solution I: Brute Force --- Time Limit Exceeded
    #
    # Solution II: Memorization
    #
    # Solution III: Tabulation

    # Time O(MN) Space O(MN), using memorization
    def numDistinct(self, s: str, t: str) -> int:

        cache = {}

        def find(i, j):

            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if (i, j) in cache:
                return cache[i, j]

            result = find(i + 1, j)

            if s[i] == t[j]:
                result += find(i + 1, j + 1)

            cache[i, j] = result
            return result

        return find(0, 0)


'''
    # Time O(MN) Space O(MN), Using Brute Force
    def numDistinct(self, s: str, t: str) -> int:

        def find(i, j):

            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if s[i] == t[j]:
                return find(i+1, j) + find(i+1, j+1)
            else:
                return find(i+1, j)

        return find(0,0)
'''
