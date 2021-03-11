'''
7. Reverse Integer
Easy

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-231 <= x <= 231 - 1
'''


class Solution:

    #        1 -> 1
    #        23 -> 32
    #        l23 -> 321

    #           result=0, num=12345
    #                   |
    #           result=5, num=1234
    #                   |
    #           result=45, num = 123

    # Time O(logN) Space O(1)
    def reverse(self, x: int) -> int:

        def helper(result, num):

            # print(f'result = {result} num = {num}')

            if num == 0:
                return result

            a, b = divmod(num, 10)
            return helper(result * 10 + b, a)

        if x is None: return None
        res = helper(0, abs(x))
        if res > pow(2, 31) - 1 or res < -pow(2, 31):
            return 0

        if x >= 0:
            return res
        else:
            return -res

