'''
329. Longest Increasing Path in a Matrix
Hard

Given an m x n integers matrix, return the length of the longest increasing path
in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not
allowed).



Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''


class Solution:

    #         [[9,9,4],
    #          [6,6,8],
    #          [2,1,1]]

    #                4
    #              /  \
    #             9    8
    #                  /\
    #                 6  1

    # Time O(MN) Space O(MN)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(r, c):

            # base case
            if (r, c) in cache:
                return cache[(r, c)]

            # recursive case
            cache[(r, c)] = 0
            value = matrix[r][c]
            count = 0
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for rr, cc in dirs:
                new_r = r + rr
                new_c = c + cc

                if 0 <= new_r < size and 0 <= new_c < col_size:

                    # this is also correct:
                    # if matrix[new_r][new_c] < matrix[r][c]
                    if matrix[new_r][new_c] < matrix[r][c]:
                        cache[(r, c)] = max(cache[(r, c)], dfs(new_r, new_c))

            cache[(r, c)] += 1

            return cache[(r, c)]

        size = len(matrix)
        col_size = len(matrix[0])
        cache = {}
        max_count = 0
        for i in range(size):
            for j in range(col_size):
                max_count = max(max_count, dfs(i, j))

        return max_count

