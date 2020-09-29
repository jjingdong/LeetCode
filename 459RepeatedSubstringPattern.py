'''
459. Repeated Substring Pattern
Easy

Given a non-empty string check if it can be constructed by taking a
 substring of it and appending multiple copies of the substring together.
  You may assume the given string consists of lowercase English letters
   only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring
"abcabc" twice.)
'''


class Solution:

    # Solution I:
    #         s + s =  "abcabcabcabcabcabcabcabc"
    #
    #       s = abc
    #        bc abc abc ab
    #           -------

    # Solution II:
    # j     = 0   1   2   3   4   5   6   7   8   9   10  11
    #         a   b   c   a   b   c   a   b   c   a   b   c
    # i     = -1  -1  -1  0   1   2   3   4   5   6   7   8
    # length = 9, size - 9 = 3, 12%3 == 0
    #
    #   a   b
    #   -1  -1
    #   a   b   a
    #   -1  -1  0
    #   a   b   a   b
    #   -1  -1  0   1

    # Time O(N) Space O(N), runtime = 128 ms
    # Using KMP, Knuth-Morris-Pratt Algorithm
    def repeatedSubstringPattern(self, s: str) -> bool:

        size = len(s)
        kmp = [-1] * size
        j = 0
        i = 1
        while i < size:
            if s[i] == s[j]:
                kmp[i] = j
                j += 1
                i += 1
            elif j > 0:
                # go back one step
                j = kmp[j - 1] + 1
            else:
                i += 1

        print(kmp)
        length = kmp[-1] + 1
        return length != 0 and size % (size - length) == 0


'''
    # Time O(N) Space O(1), runtime = 32 ms
    def repeatedSubstringPattern(self, s: str) -> bool:

        if not s: return False

        return  s in (s+s)[1:-1]
'''






