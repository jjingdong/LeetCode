'''
695. Max Area of Island
Medium

You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the
grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''


# Time O(MN) Space O(N), N = max lenghth of island
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def dfs(r, c):
        nonlocal max_area

        # base case
        if r < 0 or r > size - 1 or c < 0 or c > col_size - 1:
            return 0

        if grid[r][c] == 0:
            return 0

        grid[r][c] = 0
        # recursive case
        area = 0
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)
        return area + 1

    size = len(grid)
    col_size = len(grid[0])
    max_area = 0
    for row in range(size):
        for col in range(col_size):
            if grid[row][col] == 1:
                max_area = max(max_area, dfs(row, col))

    return max_area