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
    #
    # Solution is done
    # Code is not done
    #

    # My solution
    # Time O() Space O()
    def minPathSum(self, grid: List[List[int]]) -> int:

        size = len(grid)
        rowSize = len(grid[0])

        matrix = [[-1 for x in range(size)] for y in range(rowSize)]
        sum = 0

        def traverse(curRow, curCol, value):

            # if curCol == size -1 and curRow == rowSize -1:
            #     return
            if curCol == size or curRow == rowSize:
                return

            if matrix[curRow][curCol] == -1:
                matrix[curRow][curCol] = grid[curRow][curCol] + value
            else:
                matrix[curRow][curCol] = min(matrix[curRow][curCol], grid[curRow][curCol] + value)

            traverse(curRow, curCol + 1, matrix[curRow][curCol])
            traverse(curRow + 1, curCol, matrix[curRow][curCol])

        traverse(0, 0, 0)

        print(matrix)
        return matrix[size - 1][rowSize - 1]

