# 509 Fibonacci Number
# Easy
# https://leetcode.com/problems/fibonacci-number/
#
# F(0) = 0, F(1) = 1
# F(N) = F(N - 1) + F(N - 2),
# for N > 1.
#     Given
#     N, calculate
#     F(N).
#
# Example
# 1:
#
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example
# 2:
#
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example
# 3:
#
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

class Solution:

    # Time O(N)
    # Space O(1)
    def fib(self, N: int) -> int:

        if N == 0: return 0
        if N == 1: return 1

        a = 0
        b = 1
        N = N - 2
        while N >= 0:
            a = a + b
            b = a + b
            N = N - 2

        if N % 2 == 0:
            return a
        return b

    '''
    #Time O(2^N)
    #Space O(1)
    def fib(self, N: int) -> int:

        if N == 0: return 1
        if N == 1: return 1

        return self.fib(N-1) + self.fib(N-2)
    '''

    '''
    # Time O(N) Space O(N)
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0 : 0, 1 : 1}
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]
    '''

    '''
    def fib(self, N: int) -> int:
        if N <= 1: return N
        self.cache = {0:0, 1:1}
        return self.memoize(N)   

    def memoize(self, N: int) -> {}:
        if N in self.cache[N]
            return self.cache[N]
        self.cache[N] = self.memoize(N-1) + self.memoize(N-2)
        return self.memoize(N)
    '''
