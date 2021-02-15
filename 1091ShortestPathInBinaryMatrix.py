'''
1091. Shortest Path in Binary Matrix
Medium

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of
cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and
share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such
a path does not exist, return -1.



Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4



Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
'''


class Solution:

    # BFS
    # Time O(MN) Space O(MN)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid: return -1
        size = len(grid)
        col_size = len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        queue = collections.deque([])
        queue.append((0, 0, 0))
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        while queue:
            r, c, step = queue.popleft()
            if r == size - 1 and c == col_size - 1:
                return step + 1

            grid[r][c] = 1
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < size and 0 <= new_c < col_size and (new_r, new_c) and grid[new_r][new_c] == 0:
                    queue.append((new_r, new_c, step + 1))
                    grid[new_r][new_c] = 1

        return -1


'''
    # Note. this is not done
    # Using DFS is very complicated ----> this question shouldn't use BFS
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def traverse(r,c,step,path):
            nonlocal count

            if r < 0 or r >= size or c < 0 or c >= col_size:
                return
            if grid[r][c] == 1:
                return
            if r == size - 1 and c == col_size - 1:
                count = min(count, step)
                return
            if step > count:
                return

            grid[r][c] = 1
            dirs = [(0,1), (1,0), (-1, 0), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
            for dr,dc in dirs:
                traverse(r+dr, c+dc, step+1,path)


        if not grid: return -1
        size = len(grid)
        col_size = len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        count = float('inf')
        traverse(0,0,1)
        if count != float('inf'):
            return count
        return -1
'''

