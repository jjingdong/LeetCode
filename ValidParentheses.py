# 20. Valid Parentheses
# Easy
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 	1.	Open brackets must be closed by the same type of brackets.
# 	2.	Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1:
# Input: "()"
# Output: true
# Example 2:
# Input: "()[]{}"
# Output: true
# Example 3:
# Input: "(]"
# Output: false
# Example 4:
# Input: "([)]"
# Output: false
# Example 5:
# Input: "{[]}"
# Output: true

class Solution:

    # {[[]{}]}()()
    # Stack

    # Time: O(N)
    # Space: O(N)
    def isValid(self, s: str) -> bool:

        if s is None: return False
        if s == []: return True

        stack = []
        map = {"}": "{", "]": "[", ")": "("}

        for i in range(len(s)):

            cur = s[i]
            if cur in map:
                value = map[cur]
                if stack == []:
                    return False
                elif value == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(cur)

        if len(stack) == 0:
            return True

        return False