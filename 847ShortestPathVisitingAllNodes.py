'''
847. Shortest Path Visiting All Nodes
Hard

An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given
as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only
if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and
 stop at any node, you may revisit nodes multiple times, and you may reuse edges.



Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]


Note:

1 <= graph.length <= 12
0 <= graph[i].length < graph.length
'''


class Solution:


    def shortestPathLength(self, graph: List[List[int]]) -> int:

        # Step 1: Floyd-Warshall Time O(N^3) Space O(N^2)
        size = len(graph)
        matrix = [[float('inf') for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for node in graph[i]:
                matrix[i][node] = 1
                matrix[node][i] = 1
        for i in range(size):
            matrix[i][i] = 0

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]

        # for i in range(size):
        #     print(matrix[i])

        # Step 2: DP Time O(2^size * size^2) Space O(2^size * size)
        state_size = 1 << size
        dp = [[float('inf') for _ in range(size)] for _ in range(state_size)]
        for i in range(size):
            dp[1 << i][i] = 0

        for i in range(state_size):
            print(dp[i])

        for i in range(state_size):
            for j in range(size):
                if (i & (1 << j)) != 0:
                    for k in range(size):
                        row = i | (1 << k)
                        dp[row][k] = min(dp[row][k], dp[i][j] + matrix[j][k])

        for i in range(state_size):
            print(dp[i])

        return min(dp[-1])

