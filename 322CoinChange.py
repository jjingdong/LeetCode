'''
322. Coin Change
Medium

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:
Input: coins = [2], amount = 3
Output: -1
Note: You may assume that you have an infinite number of each kind of coin.
'''


class Solution:

    #         0 1 2 3 4 5 6 7 8 9 10 11
    #     1   0 1 2 3 4 5 6 7 8 9 10 11
    #     2   0 1 1 2 2 3 3 4 4 5 5  6
    #     5   0 1 1 2 2 1
    #     dp[i][j] = min(dp[i-1][j], dp[i][j-c] + 1)

    # Time O(N^2) Space O(N), runtime = 1260 ms
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[-1] == float('inf'): return -1
        return dp[-1]


'''
    # Time O(N^2) Space O(N^2), runtime = 2432 ms
    def coinChange(self, coins: List[int], amount: int) -> int:

        size = len(coins)
        dp = [[float('inf') for _ in range(amount+1)] for _ in range(size)]
        for j in range(size):
            dp[j][0] = 0

        for i in range(size):
            c = coins[i]
            for j in range(1, amount+1):
                if j >= c:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-c] + 1)
                else:
                    dp[i][j] = dp[i-1][j]

        if dp[-1][-1] == float('inf'): return -1         
        return dp[-1][-1]                
'''

