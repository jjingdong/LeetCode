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

    # Time O(logN) Space O(1)
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        k = None
        curr = None
        while left <= right:

            k = (right + left) // 2
            curr = k * (k + 1) // 2
            print(f'left = {left} right = {right} k = {k} curr = {curr}')
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right


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