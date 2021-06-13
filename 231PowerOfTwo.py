'''
231. Power of Two
Easy

Given an integer, write a function to determine if it is a power of two.
Example 1:
Input: 1
Output: true
Explanation: 20 = 1
Example 2:
Input: 16
Output: true
Explanation: 24 = 16
Example 3:
Input: 218
Output: false
'''


class Solution:

    # Solution I:
    # 218/2 = 109
    # 16/2 = 8/2 = 4/2 = 2/2 = 1
    # 1/2 = 1
    #
    # Solution II:  Brain Kernighan's algorithm a & (a-1)
    #
    # Solution III: Get the rightmost 1-bit a & (-a)

    # Time O(1) Space O(1), runtime = 32 ms
    def isPowerOfTwo(self, n: int) -> bool:

        if not n or n < 1: return False
        if n == 1: return True

        return n & (n - 1) == 0

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return n % 2 == 0 and self.isPowerOfTwo(n / 2)

    def isPowerOfTwo(self, n: int) -> bool:

        if n < 1: return False

        a = 1
        while a < n:
            a = a << 1

        return n == a

'''
    # Time O(1) Space O(1), runtime = 24 ms
    def isPowerOfTwo(self, n: int) -> bool:

        if not n or n < 1: return False
        if n == 1: return True

        return n == n & (-n)
'''

'''
    # Time O(logN) Space O(1), runtime = 40 ms
    def isPowerOfTwo(self, n: int) -> bool:

        if not n or n < 1: return False
        if n == 1: return True

        carry = 0
        while carry == 0 and n >= 2:
            n, carry = divmod(n,2)

        if carry != 0: return False
        return True
'''