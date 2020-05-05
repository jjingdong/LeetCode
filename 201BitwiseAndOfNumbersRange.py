'''
201. Bitwise AND of Numbers Range
Medium

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
Example 1:
Input: [5,7]
Output: 4
Example 2:
Input: [0,1]
Output: 0
'''


class Solution:

    # E.g.
    # 0 = 0
    # 1 = 1
    # 0 and 1 = 1
    #
    # E.g
    # 5 = 101
    # 6 = 110
    # 7 = 111
    # 101 and 110 and 111 = 100 = 4
    # common prefix
    # common prefix of start and end
    #
    # Solution I: bit shift
    #
    # Solution II: Brian Kernighan's algorithm
    # num and (num-1) ---> the rightmost bit of one of num would be turned off

    # Time O(1) Space O(1)
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        if m is None or n is None: return None

        count = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            count += 1

        value = n << count
        return value


'''
    # Time O(1) Space O(1)
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        while m < n:
            n = n & (n-1)
        return m & n  
'''

