'''
367. Valid Perfect Square
Easy

Given a positive integer num, write a function which returns True if num is
a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false


Constraints:

1 <= num <= 2^31 - 1
'''

class Solution:

    # x * x = num
    # x = (1.......x)
    # 1^1=1, 2^2=4, 3^3=9, 4^4=16
    #
    # Solution I: Binary Search
    #
    # Solution II: Newton's method
    # Xn+1 = Xn - f(x)/f'(x)
    # f(Xn) = X^m - num
    # f'(Xn) = m * X^(m-1)
    # Xn+1 = (1 - 1/m) * Xn + num * Xn / m * Xn^m

    # Time O(logN) Space O(1)
    def isPerfectSquare(self, num: int) -> bool:

        if num is None or num < 0: return None
        if num <= 1: return True

        i, j = 2, num / 2
        while i <= j:
            mid = i + (j - i) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                i = mid + 1
            else:
                j = mid - 1

        return False


'''
    # Time O(logN) Space O(1)
    # Xn+1 = Xn - f(x)/f'(x)
    # f(Xn) = X^m - num
    # f'(Xn) = m * X^(m-1)
    # # Xn+1 = (Xn + num/Xn)/2
    def isPerfectSquare(self, num: int) -> bool:

        if num is None or num < 0: return None
        if num <= 1: return True

        #Xk+1 = (Xk + num/Xk)/2
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2

        if x * x == num:
            return True
        return False
'''

'''
    # Time O(logN) Space O(1)
    # Xn+1 = Xn - f(x)/f'(x)
    # f(Xn) = X^m - num = X^3 - num
    # f'(Xn) = m * X^(m-1) = 3 * X^2
    # Xn+1 = 2/3*X + num /(3 * X^2)
    def isPerfectCube(self, num: int) -> bool:

        if num is None or num < 0: return None
        if num <= 1: return True

        # Xn+1 = 2/3*X + num /(3 * X^2)
        x = num // 3
        while x * x * x > num:
            x = 2/3*x + num /(3 * x * x)

        print(x)
        if x * x == num:
            return True
        return False
'''

