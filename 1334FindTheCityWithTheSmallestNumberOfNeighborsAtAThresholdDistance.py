'''
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
Medium

355

25

Add to List

Share
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] =
[fromi, toi, weighti] represents a bidirectional and weighted edge between cities
fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some
 path and whose distance is at most distanceThreshold, If there are multiple such
 cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of
the edges' weights along that path.



Example 1:



Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to
return city 3 since it has the greatest number.
Example 2:



Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],
distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1]
City 1 -> [City 0, City 4]
City 2 -> [City 3, City 4]
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
The city 0 has 1 neighboring city at a distanceThreshold = 2.


Constraints:

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
'''


class Solution:

    # Floyd-warshall
    #     Eg1.
    #         0   1   2   3
    #     0   0   3   4   5
    #     1   3   0   1   2
    #     2   4   1   0   1
    #     3   5   2   1   0
    #
    #     distanceThreshold = 4
    #     {0: [1,2], 1:[0,2,3], 2:[0,1,3], 3:[1,2]}
    #     0 and 3 has 2 neighbors, return 3
    #
    #     Eg2.
    #         0   1   2   3   4
    #     0   0   2   5   L   L
    #     1   2   0   3   L   2
    #     2   L   3   0   1   2
    #     3   L   L   1   0   1
    #     4   8   2   2   1   0
    #
    #     distanceThreshold = 2
    #     {0: [1], 1:[0,4], 2:[3,4], 3:[2,4], 4:[1,2,3]}
    #     0 has 1 neighbor, return 0
    #
    #     output:
    #         (1) one city: has minimum number of cities can reach, with in distanceTreshold
    #         (2) if multiple answer, return the city with the largest city no.

    # Time O(V^3) Space O(V^2), runtime = 440 ms, 85.47%
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        if not edges: return None

        dis = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dis[i][i] = 0

        for u, v, w in edges:
            dis[u][v] = w
            dis[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(i + 1, n):
                    if dis[i][k] < distanceThreshold and dis[k][j] < distanceThreshold:
                        dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
                        dis[j][i] = dis[i][j]

        min_count = float('inf')
        max_city = float('-inf')
        for i in range(n):
            count = 0
            for j in range(n):
                if 0 < dis[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_count:
                if (i == 3): print(count)
                min_count = count
                max_city = max(i, max_city)

        return max_city
