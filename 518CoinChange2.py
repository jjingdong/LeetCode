'''
518. Coin Change 2
Medium

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
	•
 
Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:
Input: amount = 10, coins = [10]
Output: 1
 
Note:
You can assume that
	•	0 <= amount <= 5000
	•	1 <= coin <= 5000
	•	the number of coins is less than 500
	•	the answer is guaranteed to fit into signed 32-bit integer
'''


class Solution:

    #         0   1   2   3   4   5

    #     1   1   1   1   1   1   1
    #     2   1   1   2   2   3   3
    #     5   1   1   1   1   1   4

    #     dp[i][j] = dp[i-1][j] + dp[i][j-c]

    #     dp[i] = dp[i] + dp[i-c]
    #     dp[0] = 1

    # Time O(MN) Space O(N), runtime = 144 ms
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = dp[i] + dp[i - c]

        return dp[-1]

