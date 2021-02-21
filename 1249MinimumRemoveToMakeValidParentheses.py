'''
1249. Minimum Remove to Make Valid Parentheses
Medium

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
 so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.

'''


class Solution:

    #         l  e  e  (  t  (  c  )  o  )  d  e  )
    #                  1     2     1     0       -1
    #                                             |
    #                                          remove

    #         a   )   b   (   c   )   d
    #             -1
    #             |
    #             remove
    #                     1       0

    #         )   )   (   (
    #         -1
    #         |
    #       remove
    #            -1
    #             |
    #             remove
    #                 1   2
    #                 -----    remove

    #         )   d   )   c   (   b   (   a   (
    #         1       2       1       0       -1

    # Time O(N) Space O(N)
    def minRemoveToMakeValid(self, s: str) -> str:

        def helper(lb, rb, input_str):
            count = 0
            result = ''

            for char in input_str:
                if char == lb:
                    count += 1
                    result += char
                elif char == rb:
                    count -= 1
                    if count > -1:
                        result += char
                    else:
                        count = 0
                else:
                    result += char

            return count, result

        # remove ')'
        count, result = helper('(', ')', s)
        if count == 0:
            return result

        # remove rightmost '('
        new = result[::-1]
        count, result = helper(')', '(', new)

        return result[::-1]
