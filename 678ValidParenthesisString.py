'''
678. Valid Parenthesis String
Medium

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
	1.	Any left parenthesis '(' must have a corresponding right parenthesis ')'.
	2.	Any right parenthesis ')' must have a corresponding left parenthesis '('.
	3.	Left parenthesis '(' must go before the corresponding right parenthesis ')'.
	4.	'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
	5.	An empty string is also valid.

Example 1: 
Input: "()"
Output: True

Example 2: 
Input: "(*)"
Output: True

Example 3: 
Input: "(*))"
Output: True

Note: 
	1.	The string size will be in the range [1, 100].
'''


class Solution:

    # (   )   _
    # 1. -1.  0
    # # (   *   *   *   )
    # # 1.  2   3   4
    #       0   1   2
    #       1   2   3
    #           1   .
    #           -1  .
    #           0   .
    #           2   .
    #           0   .
    #           1   .

    # [lo, hi] = [1, 1], [0, 2], [0, 3], [0, 4]

    # Time O(N) Space O(1)
    def checkValidString(self, s: str) -> bool:

        lo = 0
        hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1

            if hi < 0:
                return False
            lo = max(lo, 0)

        return lo == 0

    # Time O(N) Space O(N)
    def checkValidString(self, s: str) -> bool:

        def helper(index, lo, hi):

            if index == size:
                if hi < 0: return False
                if lo < 0: lo = 0
                return lo == 0

            if hi < 0:
                return False
            if lo < 0:
                lo = 0

            cur = s[index]
            if cur == '(':
                return helper(index + 1, lo + 1, hi + 1)
            elif cur == ')':
                return helper(index + 1, lo - 1, hi - 1)
            else:
                return helper(index + 1, lo - 1, hi + 1)

        size = len(s)
        return helper(0, 0, 0)

