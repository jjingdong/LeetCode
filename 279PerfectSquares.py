'''
279. Perfect Squares
Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''


class Solution:

    #       index = 0 1 2 3 4 5 6 7 8 9 10 11 12 13
    #          1    0 1 2 3 4 5 6 7 8 9 10 11 12 13
    #          4    0 1 2 3 1 2 3 4 2 3  4  5  3  4
    #          9    0 1 2 3 1 2 3 4 2 1  2  3  4  2
    #          16
    # dp[i][j]  = min(dp[i-1][j], dp[i][j-c] + 1)
    # dp[j] = min(dp[j], dp[j-c] + 1)

    # Time O(MN) Space O(N), time = 5042 ms
    def numSquares(self, n: int) -> int:

        # lst = [1, 4, 9, 16, 25]
        lst = [x ** 2 for x in range(1, int(n ** 0.5) + 1)]
        dp = list(range(n + 1))

        for i in range(1, len(lst)):
            coin = lst[i]
            for j in range(1, n + 1):
                if j > coin - 1:
                    dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[-1]


'''
    # Time O(MN) Space O(N), time = 5276 ms
    def numSquares(self, n: int) -> int:

        # lst = [1, 4, 9, 16, 25]
        def getSquare(number):
            a = 1
            while a ** 2 <= number:
                lst.append(a**2)
                a += 1

        if not n: return 0

        lst = []
        getSquare(n)
        dp = [float('inf')] * (n+1)
        for j in range(n+1):
            dp[j] = j

        for i in range(1, len(lst)):
            coin = lst[i]
            for j in range(1, n+1):
                if j > coin - 1:
                    dp[j] = min(dp[j], dp[j-coin] + 1)

        return dp[-1]
'''

'''    
    # Time O(MN) Space O(MN), Time Limit Exceeded
    def numSquares(self, n: int) -> int:

        # lst = [1, 4, 9, 16, 25]
        def getSquare(number):
            a = 1
            while a ** 2 <= number:
                lst.append(a**2)
                a += 1

        if not n: return 0

        lst = []
        getSquare(n)
        dp = [[float('inf') for _ in range(n+1)] for _ in range(len(lst))]
        for j in range(n+1):
            dp[0][j] = j
        for i in range(len(lst)):
            dp[i][0] = 0

        for i in range(1, len(lst)):
            coin = lst[i]
            for j in range(1, n+1):
                if j > coin - 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coin] + 1)
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
'''
