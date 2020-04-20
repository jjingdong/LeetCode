# 62. Unique Paths
# Medium
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
#  Above is a 7 x 3 grid. How many possible unique paths are there?
# Note: m and n will be at most 100.
# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:
# Input: m = 7, n = 3
# Output: 28

class Solution:

    # Dynamic Programming:
    # Tabulation:
    # 3 x 2:
    # [
    # [0,0]
    # [0,0]
    # [0,0]]

    # Path: 1, 1
    #       1, 2
    #       1, 3

    # matrix[0][] = 1
    # matrix[][0] = 1
    # matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    def uniquePaths(self, m: int, n: int) -> int:

        matrix = [[1 for i in range(n)] for j in range(m)]
        print(matrix)

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]

# ------------------------------------------------------
# Solution II
# m: row
# n: column
# m x n: row x column
# 2 x 2: [[0, 0],
#         [0, 0]]
# 3 x 2: [[0,0][0,0][0,0]]
# matrix[3][2] = 0
# matrix.size = 3
# matrix[0].size = 2

# Time O(NM)
# Space O(NM)

#     def uniquePaths(self, m: int, n: int) -> int:

#         matrix = [[0 for i in range(m)] for j in range(n)]

#         def traverse(m, n):

#             if m < 0 or m >= len(matrix) or n < 0 or n >= len(matrix[0]):
#                 return 0

#             if m == len(matrix) - 1 and n == len(matrix[0]) - 1:
#                 return 1

#             if matrix[m][n] == 1:
#                 return 0

#             sum = 0

#             matrix[m][n] = 1
#             sum += traverse(m+1, n)
#             sum += traverse(m, n+1)
#             matrix[m][n] = 0

#             return sum


#         return traverse(0,0)

