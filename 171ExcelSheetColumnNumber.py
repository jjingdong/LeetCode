'''
171. Excel Sheet Column Number
Easy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
'''


class Solution:

    # Time O(N), n = length of the s, Space O(N), runtime = 28 ms
    def titleToNumber(self, s: str) -> int:
        value = ord('A') - 1
        number = 0
        for char in s:
            number = number * 26 + (ord(char) - value)

        return number


'''
    # Time O(N), n = length of the s, Space O(N), runtime = 28 ms
    def titleToNumber(self, s: str) -> int:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27 -> 26 + 1
#     AB -> 28 -> 26 + 2
#     AZ -> 52   -> 26 + 26

#     BA ->      -> 26 + 26 + 1
#     ...
#     AAA -> 26 + 26 + 1


        def get_number(char):

            alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if len(char) == 1:
                return alphas.index(char) + 1

            if len(char) > 1:
                return get_number(char[:-1])*26 + get_number(char[-1])

        return get_number(s)
'''
