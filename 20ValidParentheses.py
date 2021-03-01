'''
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution:

    # Time: O(N), Space: O(N)
    def isValid(self, s: str) -> bool:

        if not s: return False
        if len(s) % 2 != 0: return False
        b_dict = {"}": "{", "]": "[", ")": "("}
        if s[0] not in b_dict.values(): return False

        stack = []
        for i in range(len(s)):

            cur = s[i]
            if cur in b_dict:
                value = b_dict[cur]
                if not stack:
                    return False
                elif value == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(cur)

        return len(stack) == 0
