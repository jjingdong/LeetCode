'''
1631. Path With Minimum Effort
Medium

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows
 x columns, where heights[row][col] represents the height of cell (row, col). You are situated
  in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1)
   (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that
   requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells
of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells,
which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.


Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
'''


class Solution:

    # Solution I: Using DFS
    # Time O(3^(MN)) Space O(MN), Time Limit Exceeded
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def dfs(r, c, max_diff, precell):
            nonlocal global_max

            if f'{r}_{c}' in visited:
                return

            if r < 0 or r >= size or c < 0 or c >= col_size:
                return

            value = abs(heights[r][c] - precell)
            max_diff = max(max_diff, value)

            if r == size - 1 and c == col_size - 1:
                global_max = min(max_diff, global_max)
                return

            if max_diff > global_max:
                return

            id = f'{r}_{c}'
            visited.add(id)
            dfs(r + 1, c, max_diff, heights[r][c])
            dfs(r - 1, c, max_diff, heights[r][c])
            dfs(r, c + 1, max_diff, heights[r][c])
            dfs(r, c - 1, max_diff, heights[r][c])
            visited.remove(id)

        size = len(heights)
        col_size = len(heights[0])
        visited = set()
        global_max = float('inf')
        dfs(0, 0, 0, heights[0][0])
        return global_max


