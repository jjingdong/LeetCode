'''
50. Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''


class Solution:

    # Time O(logN), Space O(1) runtime = 40 ms
    def myPow(self, x: float, n: int) -> float:

        # x = 3
        # index = 0   1   2   3   4   5   6
        # result= 1   3   9   27
        #         a   b

        if n == 0: return 1
        if n == 1: return x

        if n < 0:
            x = 1 / x
            n = -n

        a = 1
        b = x
        while n > 0:
            if n % 2 == 1:
                a = a * b
            b = b * b

            n = n // 2

        return a


'''   
    # Time O(logN) Space O(), runtime = exceed the maximum memory
    #
    def myPow(self, x: float, n: int) -> float:

        if n == 0: return 1
        if n == 1: return x

        # maximum list is (4294967295 / 2) / 4 or 536870912
        dp = [1] * (abs(n)+1)
        dp[1] = x

        for i in range(2, abs(n)+1):
            if i % 2 == 0:
                dp[i] = dp[i//2] * dp[i//2]
            else:
                dp[i] = dp[i//2+1] * dp[i//2]

        if n < 0:
            return 1 / dp[abs(n)]

        return dp[n]
'''

'''    
    # Time O(logN) Space O(logN), runtime = 36 ms
    def myPow(self, x: float, n: int) -> float:

#         2^10
#         = 2^5 * 2^5
#         = 2^3 * 2^2 * 2^5
#         = 2^2 * 2^1 * 2^2 * 2^5
#       
#         cache = {1:0, 2:4, 3:8}

        def get_pow(n):

            if n == 0 : return 1
            if n == 1: return x

            if n in cache: return cache[n]

            if n % 2 == 0:
                cache[n] = get_pow(n/2) * get_pow(n/2)
                return cache[n]
            else:
                cache[n] = get_pow(n//2+1) * get_pow(n//2)
                return cache[n]

        cache = {0:1, 1:x}
        result = get_pow(abs(n))
        if n < 0:
            result = 1 / result

        return result
'''

'''
    # Time O(N) Space O(1), time limit exceeded
    def myPow(self, x: float, n: int) -> float:

        if n == 0: return 1

        result = x
        for i in range(abs(n) - 1):
            result *= x

        if n < 0:
            result = 1 / result

        return result
'''

'''    
    # Time O(1) Space O(1), runtime = 32 ms
    def myPow(self, x: float, n: int) -> float:

        return x ** n
'''
