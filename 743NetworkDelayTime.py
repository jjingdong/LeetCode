'''
743. Network Delay Time
Medium

You are given a network of n nodes, labeled from 1 to n. You are also given times,
 a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the
 source node, vi is the target node, and wi is the time it takes for a signal to
 travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n
 nodes to receive the signal. If it is impossible for all the n nodes to receive
 the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1


Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

'''


# Solution II: Dijkstra
# Time O() Space O()
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    t_dict = collections.defaultdict(dict)
    for u, v, w in times:
        t_dict[u][v] = w

    queue = [(0, k)]
    visited = {}
    while queue:

        weight, node = heapq.heappop(queue)

        if node not in visited:
            visited[node] = weight

        if len(visited) == n:
            return max(visited)

        for next_node in t_dict[node]:
            heapq.heappush(queue, (t_dict[node][next_node], next_node))

    if all_max != float('inf'):
        return all_max

    return -1





class Solution:

    #         u -------> v
    #              w

    # Time O(N^3) Space O(N^2)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

        for u, v, w in times:
            matrix[u - 1][v - 1] = w
        for i in range(n):
            matrix[i][i] = 0

        for index in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] > matrix[i][index] + matrix[index][j]:
                        matrix[i][j] = matrix[i][index] + matrix[index][j]

        max_time = max(matrix[k - 1])
        if max_time != float('inf'):
            return max_time
        return -1

