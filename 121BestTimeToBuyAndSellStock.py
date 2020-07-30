'''
121. Best Time to Buy and Sell Stock
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:

    # Time O(N)
    # Space O(1)
    def maxProfitII(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit


'''
    #Time O(N)
    #Space O(N)
    def maxProfit(self, prices: List[int]) -> int:

        globalMax = 0

        for i in range(len(prices)):
            curPrice = prices[i]

            if i == 0:
                localDiff = 0
                globalDiff = 0
                output = 0
                globalMax = 0
            else:
                localDiff = curPrice - prices[i-1]

            globalDiff = max(localDiff, globalDiff + localDiff) 
            globalMax = max(globalMax, globalDiff)

        return globalMax
'''

