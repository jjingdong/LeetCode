# 122. Best Time to Buy and Sell Stock II
# Easy
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as
# you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell
# the stock before you buy again).
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:

    # [7, 1, 5, 3, 6, 4]
    #     v  p  v  p

    # [7, 6, 5, 4, 3, 2]
    #                 v

    # [1, 2, 3, 4, 5, 6]
    #  v              p

    # Time O(N)
    # Space O(1)
    def maxProfit(self, prices: List[int]) -> int:

        if prices is None: return None
        if prices == []: return 0

        result = 0

        v = prices[0]
        p = prices[0]
        diff = 0
        after = 0

        for i in range(0, len(prices)):

            diff = prices[i] - prices[i - 1]
            if i == len(prices) - 1:
                after = 0
            else:
                after = prices[i + 1] - prices[i]

            if diff < 0:
                v = prices[i]

            if diff >= 0:
                if i == len(prices) - 1:
                    p = prices[i]
                    result += p - v
                elif after < 0:
                    p = prices[i]
                    result += p - v

                # print("v = " + str(v) + "p = " + str(p))

        return result



