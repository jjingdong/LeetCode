'''
441. Arranging Coins
Easy

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.
Example 1:
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''


class Solution:

    #                n = 8
    #
    # ¤              1     level = 1
    # ¤ ¤            2     level = 2
    # ¤ ¤ ¤          3     level = 3
    # ¤ ¤
    #
    #         1 + 2 + 3 + 4 >= 8
    # level   1   2   3
    #
    # If each stair is full, total = 1 + 2 + 3 + 4 + ... = k * (k+1) // 2
    #                            k = 1   2   3   4
    #   k * (k+1) // 2 >= n
    #
    #

    # Time O(logN) Space O(1), runtime = 36 ms
    def arrangeCoins(self, n: int) -> int:

        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * (mid + 1) // 2 == n:
                return mid
            if mid * (mid + 1) // 2 > n:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi


'''
    def arrangeCoins(self, n: int) -> int:
        # sum of 1 to k is (k+1)k/2
        # n = (k^2 + k)/2, floored, solve for k
        # essentially find root of (2n), floor it then verify
        k = int(sqrt(2.0 * n))
        if k * (k+1)/2 <= n:
            return k
        return k-1
'''

'''
    # Time O(level) Space O(1)
    def arrangeCoins(self, n: int) -> int:

        if n < 0: return -1

        level = 1
        while n >= level:
            n = n - level
            level += 1

        return level - 1
'''

'''
    # Time O(level) Space O(1), runtime = 832 ms
    def arrangeCoins(self, n: int) -> int:
        num, level, total = 0, 0, 0
        while total < n:
            num += 1
            total += num
            level += 1

        if total == n: return level
        return level - 1
'''
