'''
367. Valid Perfect Square
Easy

Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.
Example 1:
Input: 16
Output: true
Example 2:
Input: 14
Output: false
'''


class Solution:

    # x * x = num
    # x = (1.......x)
    # 1^1=1, 2^2=4, 3^3=9, 4^4=16

    # Time O(logN) Space O(1)
    def isPerfectSquare(self, num: int) -> bool:

        if num is None or num < 0: return None
        if num <= 1: return True

        i, j = 2, num / 2
        while i <= j:
            mid = i + (j - i) // 2
            print(mid)
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                i = mid + 1
            else:
                j = mid - 1

        return False




