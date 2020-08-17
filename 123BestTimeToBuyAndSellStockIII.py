'''
123. Best Time to Buy and Sell Stock III
Hard

Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete at most
two transactions.

Note: You may not engage in multiple transactions at the same time (i.e.,
you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3),
profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4),
             profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5),
profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell
             them later, as you are
             engaging multiple transactions at the same time. You must
             sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


class Solution:

    #        make maximum profit
    #         no. transactions = 0, 1, 2
    #         each day only sell or buy
    #
    #             3,  3,  5,  0,  0,  3,  1,  4
    #     index = 0   1   2   3   4   5   6   7
    #    
    #     if no of transactions are not limited:
    #
    #         5 - 3 = 2
    #         3 - 0 = 3
    #         4 - 1 = 3
    #
    #     that will be the same as 122. Best Time to Buy and Sell Stock II
    #
    #     if no of transactions is 0, 1:
    #         4 - 0 = 4
    #     that will be the same as 121. Best Time to Buy and Sell Stock
    #
    #             3,  3,  5,  0,  0,  3,  1,  4
    #     index = 0   1   2   3   4   5   6   7
    #                     |           |       |
    #                     p           p       p
    #
    # max_value   0   0   2   2   2   5   5   6
    #                     pick this day as peak or not

    # Time O(N) Space O(1), runtime = 72 ms
    def maxProfit(self, prices: List[int]) -> int:

        if not prices: return 0

        t1_price, t2_price = float('inf'), float('inf')
        t1_max_profit, t2_max_profit = 0, 0
        for p in prices:
            t1_price = min(t1_price, p)
            t1_max_profit = max(t1_max_profit, p - t1_price)

            t2_price = min(t2_price, p - t1_max_profit)
            t2_max_profit = max(t2_max_profit, p - t2_price)

        return t2_max_profit


'''
121. Best Time to Buy and Sell Stock

    # Time O(N) Space O(1), runtime = 
    def maxProfit(self, prices: List[int]) -> int:

        bottom_price = float('inf')
        max_profit = 0
        for p in prices:
            bottom_price = min(bottom_price, p)
            max_profit = max(max_profit, p - bottom_price)

        return max_profit


'''

'''
122. Best Time to Buy and Sell Stock II

    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff

        return profit
'''