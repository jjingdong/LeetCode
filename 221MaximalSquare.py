'''
221. Maximal Square
Medium

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Example:
Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''


class Solution:

    # Dynamic Programming
    # dp(i,j) = min(dp(i-1), dp(i-1, j-1), dp(i, j-1)) + 1
    # 1. dp[i][j] = int(matrix[i][j]), if i == 0 or j ==0
    # 2. dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1, if matrix[i][j] == '1'

    # Time O(MN) Space O(MN)
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if matrix is None: return None
        if matrix == []: return 0

        maxValue = 0
        sums = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if i == 0 or j == 0:
                    sums[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        sums[i][j] = min(sums[i - 1][j], sums[i][j - 1], sums[i - 1][j - 1]) + 1

                maxValue = max(maxValue, sums[i][j])
        return maxValue ** 2


