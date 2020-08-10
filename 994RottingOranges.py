'''
994. Rotting Oranges
Medium

In a given grid, each cell can have one of three values:
	•	the value 0 representing an empty cell;
	•	the value 1 representing a fresh orange;
	•	the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
 
Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Note:
	1.	1 <= grid.length <= 10
	2.	1 <= grid[0].length <= 10
	3.	grid[i][j] is only 0, 1, or 2.

'''


class Solution:

    # Solution I: BFS
    #
    # Solution II: BFS optimize Space O(1)

    # Time O(MN) Space O(1), runtime = 52 ms
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid: return None

        no_fresh = 0
        pre_level = -1

        size, col_size = len(grid), len(grid[0])
        queue = collections.deque([])
        for r in range(size):
            for c in range(col_size):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    grid[r][c] = 1
                if grid[r][c] == 1:
                    no_fresh += 1

        if no_fresh == 0:
            return 0

        while queue:
            r, c, level = queue.popleft()
            if grid[r][c] == 1:
                grid[r][c] = 2
                no_fresh -= 1

                if pre_level != level:
                    pre_level += 1

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for d1, d2 in directions:
                    next_r, next_c = r + d1, c + d2
                    if 0 <= next_r < size and 0 <= next_c < col_size:
                        queue.append((next_r, next_c, level + 1))

        return pre_level if no_fresh == 0 else -1
