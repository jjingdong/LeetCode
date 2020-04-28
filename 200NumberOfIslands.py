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
    # Solution is not done
    # Time O(MN) Space O(1) -> no extra space used
    def numIslands(self, grid: List[List[str]]) -> int:

        if grid is None: return None
        if grid == []: return 0

        length = len(grid)
        rowLen = len(grid[0])

        def traverse(r, c):
            # nonlocal length
            # nonlocal rowLen

            if r < 0 or c < 0 or r >= length or c >= rowLen:
                return
            elif grid[r][c] == 0 or grid[r][c] == 2:
                return
            else:
                grid[r][c] = 2
                traverse(r - 1, c)
                traverse(r, c - 1)
                traverse(r + 1, c)
                traverse(r, c + 1)

        sum = 0
        for i in range(length):
            for j in range(rowLen):
                print("here")
                print('i' + str(i) + 'j' + str(j))
                print(grid)
                if grid[i][j] == '1':
                    print('i' + str(i) + 'j' + str(j))
                    traverse(i, j)
                    sum += 1

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







