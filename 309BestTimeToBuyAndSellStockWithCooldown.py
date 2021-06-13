'''
309. Best Time to Buy and Sell Stock with Cooldown
Medium

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
	•	You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
	•	After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:
Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''


class Solution:

    #          [  1,  2,  3,  0,  2]

    # profits  [  0,  0,  0,  0,  0]

    # max_diff [  -1,  1,  1,  -3,  -2]

    # cool_down [   0,  0,  1,  -3,  -2]

    # Time O(N) Space O(1), runtime = 64 ms
    def maxProfit(self, prices: List[int]) -> int:

        if not prices: return 0

        profits = [0] * len(prices)
        max_diff = -prices[0]

        for i in range(1, len(prices)):
            profits[i] = max(profits[i - 1], prices[i] + max_diff)
            cooldown = 0 if i - 2 < 0 else profits[i - 2]
            max_diff = max(max_diff, cooldown - prices[i])

        return profits[-1]


def maxProfit(self, prices: List[int]) -> int:

    if not prices: return 0

    profit = [0] * len(prices)
    diff = -prices[0]

    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        cooldown = 0 if i - 2 < 0 else profit[i - 1]
        profit[i] = max(profit[i - 1], cooldown + diff)
    return profit[-1]




'''   
    # Time O(N) Space O(1), runtime = 44 ms
    # From solution
    def maxProfit(self, prices: List[int]) -> int:

        sold = float('-inf')
        held = float('-inf')
        reset = 0

        for price in prices:

            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)
'''

''' 
    # Time O(N2) Space O(N), runtime = 3128 ms
    # From solution
    def maxProfit(self, prices: List[int]) -> int:

        size = len(prices)
        DP = [0] * (size + 2)

        for i in range(size-1, -1, -1):

            c1 = 0
            for sell in range(i+1, size):
                profit = prices[sell] - prices[i] + DP[sell + 2]
                c1 = max(profit, c1)

            c2 = DP[i+1]

            DP[i] = max(c1, c2)

        return DP[0]
'''

