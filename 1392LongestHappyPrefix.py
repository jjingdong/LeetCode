'''
1392. Longest Happy Prefix
Hard

A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.



Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el",
"vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
Example 3:

Input: s = "leetcodeleet"
Output: "leet"
Example 4:

Input: s = "a"
Output: ""


Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
'''


class Solution:

    #         l   e   v   e   l
    #         -1  -1  -1  -1  0
    #
    # index = 0   1   2   3   4   5
    #         a   b   a   b   a   b
    #         -1  -1  0   1   2   3
    #
    # index = 0   1   2   3   4   5   6   7   8   9   10  11
    #         l   e   e   t   c   o   d   e   l   e   e   t
    #  j =    -1  -1  1   -1  -1  -1  -1  1   0   1   2   3

    # Time O(N) Space O(N), runtime = 248 ms
    # Using KMP, Knuth Morri Pratt
    def longestPrefix(self, s: str) -> str:

        if not s: return ""

        size = len(s)
        kmp = [-1] * size
        i = 0
        j = 1

        while j < len(s):
            if s[i] == s[j]:
                kmp[j] = i
                i += 1
                j += 1
            elif i > 0:
                i = kmp[i - 1] + 1
            else:
                j += 1

        if kmp[-1] == -1: return ''
        return s[:kmp[-1] + 1]




