'''
70. Climbing Stairs
Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
'''


class Solution:

    # Time O(N/2) Space O(1), runtime = 32 ms
    def climbStairs(self, n: int) -> int:

        # count = 1   2   3   4   5   6   7   8   9
        #         1   2   3   5   8   13  21  34  55
        #         a   b   a   b   a   b   a   b   a

        a, b = 1, 2
        count = 2
        while count < n:
            a = a + b
            b = a + b
            count += 2

        if n % 2 == 1:
            return a
        else:
            return b


'''   
    # Time O(N) Space O(N), runtime = 28 ms, using dynamic programming with cache
    def climbStairs(self, n: int) -> int:

        def stairs(n):

            if n in cache:
                return cache[n]

            if n == 1:
                return 1

            if n == 2:
                return 2

            cache[n] = stairs(n-1) + stairs(n-2)
            return cache[n]

        cache = {}
        return stairs(n)
'''

'''
    # Time O(N) Space O(N), runtime = 40 ms, using dynamic programming - cache
    def climbStairs(self, n: int) -> int:

#         0 1 2 3 4 5 6   7   8   9
#     1   1 1 1 1 1 1 1   1   1   1
#     2   1 1 2 3 5 8 12 21  34  55
#    
#     dp[i] = dp[i-1] + dp[i-2]

        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
'''

