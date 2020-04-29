'''
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


class Solution:

    # [ [1, 3, 1],
    #   [1, 5, 1],
    #   [4, 2, 1] ]
    #
    # [ [1,4,5],
    #   [2,7,6],
    #   [6,8,7] ]
    #
    # Brute Force:
    # cost(i,j) = grid[i][j] + min(cost(i+1, j), cost(i, j+1))
    # Time O(2^m+n)
    #
    # Dynamic Programming:
    # dp(i,j)=grid(i,j)+min(dp(i+1,j),dp(i,j+1))
    # Using additinal matrix
    # Time O(MN) Space O(MN)
    #
    # Dynamic Programming:
    # grid(i,j)=grid(i,j)+min(grid(i+1,j),grid(i,j+1))
    # Using grid to track the results, no additional space
    # Time O(MN) Space O(1)

    # My solution
    # Time O(MN) Space O(1)
    def minPathSum(self, grid: List[List[int]]) -> int:

        def traverse(r, c):

            if r >= len(grid) or c >= len(grid[0]):
                return
            if r == 0 and c == 0:
                grid[r][c] = grid[r][c]
            elif r == 0:
                grid[r][c] += grid[r][c - 1]
            elif c == 0:
                grid[r][c] += grid[r - 1][c]
            else:
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                traverse(i, j)

        return grid[len(grid) - 1][len(grid[0]) - 1]

