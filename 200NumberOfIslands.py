'''
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input:
11110
11010
11000
00000

Output: 1
Example 2:
Input:
11000
11000
00100
00011

Output: 3
'''


class Solution:

    # DFS
    # Time O(MN) Space O(1)
    def numIslands(self, grid: List[List[str]]) -> int:

        if grid is None: return None
        if grid == []: return 0

        def traverse(r, c):

            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'
            traverse(r - 1, c)
            traverse(r, c - 1)
            traverse(r + 1, c)
            traverse(r, c + 1)

        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    sum += 1
                    traverse(i, j)

        return sum


# 11000
# 11000
# 00100
# 00011
#
# check up and left
# this won't work when the island looks like:
# 111
# 010
# 111
# This question is checking the number of islands, not the number of rectangle islands
'''
 def numIslands(self, grid: List[List[str]]) -> int:

        if grid is None: return None
        if grid == [[]]: return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1':

                    left = j-1 < 0 or grid[i][j-1] == '0'
                    top = i-1 < 0 or grid[i-1][j] == '0'

                    if left and top:
                        count +=1

        return count
'''











