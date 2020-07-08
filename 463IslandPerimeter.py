'''
463. Island Perimeter
Easy

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
 
Example:
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
'''


class Solution:

    #         4 * 7 = 28
    #         horizontal:
    #             4         -> -2
    #             12        -> -2
    #             4         -> -2
    #             8
    #
    #         vertical:
    #             -4  -2
    #
    #         28 - 12 = 26

    # Time O(MN) Space O(1), runtime = 724 ms
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        if not grid: return 0

        size = len(grid)
        col_size = len(grid[0])
        perimeter = 0
        for i in range(size):
            for j in range(col_size):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i != size - 1 and grid[i + 1][j] == 1:
                        perimeter -= 2
                    if j != col_size - 1 and grid[i][j + 1] == 1:
                        perimeter -= 2

        return perimeter
