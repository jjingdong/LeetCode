'''
258. Add Digits
Easy

Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''


class Solution:

    # Time O(N^2) Space O(N^2), runtime = 36 ms
    def addDigits(self, num: int) -> int:

        def add_d(num):

            result = 0
            while num:
                num, digit = divmod(num, 10)
                result += digit

            return result

        if not num: return num
        value = add_d(num)
        while value > 9:
            value = add_d(value)

        return value


'''
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
'''

'''
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
'''

