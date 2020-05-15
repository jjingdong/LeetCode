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

    # Solution I: Brute Force
    #
    # Solution II: Dynamic Programming - Memorization
    #
    # Solution III: Dynamic Programming - Tabulation

    # Note. this is not finished
    # Time O() Space O()
    def coinChange(self, coins: List[int], amount: int) -> int:

        def change(cur_sum, coin):
            nonlocal count

            if cur_sum > amount:
                return
            if cur_sum == amount:
                count += 1
                return

            cur_sum += coin
            count += 1

            for c in coins:
                change(amount, c)

        count = 0
        change(0, 0)
        return count
