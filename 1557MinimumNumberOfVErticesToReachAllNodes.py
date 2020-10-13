'''
1557. Minimum Number of Vertices to Reach All Nodes
Medium

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array
edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to
node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable.
It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.



Example 1:



Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0
we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
Example 2:



Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node,
so we must include them. Also any of these vertices can reach nodes 1 and 4.


Constraints:

2 <= n <= 10^5
1 <= edges.length <= min(10^5, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi < n
All pairs (fromi, toi) are distinct.
'''


class Solution:

    #     - topological sort (not neccessary)
    #
    #     todo = [] 2
    #     result = []
    #         0: [1,2], 3:[4], 1:[], 4:[2] 2:[5], 5:[]
    #         0: [1,2,5], 3:[4,2,5], 1:[], 4:[2,5] 2:[5],5:[]
    #         reverse_dict = {0: [], 1: [0], 2: [0, 4], 3: [], 4: [3], 5: [2]}

    #
    #     output = [0,3]
    #
    #     - topological sort in reverse order
    #
    #     todo = []
    #     result = []
    #        {0: [], 1: [0], 2: [0, 4], 3: [], 4: [3], 5: [2]}
    #
    #     - Floyd-Warshall (not neccessary)
    #         0   1   2   3   4   5
    #     0   1   1   1   0   0   0
    #     1   0   1   0   0   0   0
    #     2   0   0   1   0   0   1
    #     3   0   0   1   1   1   1
    #     4   0   0   1   0   1   0
    #     5   0   0   0   0   0   1
    #
    #     - directed acyclic graph
    #         1. directed graph
    #         2. no cycle
    #         3. has topological order
    #
    #         so all the node without in-degree node is in the final answer
    #         reverse_dict = {0: [], 1: [0], 2: [0, 4], 3: [], 4: [3], 5: [2]}

    # Time O(), Space O(), runtime =
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        if not edges: return None

        seen = set()
        for u, v in edges:
            seen.add(v)

        all_nodes = set([x for x in range(n)])
        return all_nodes ^ seen


'''
    # Time O(V+E), Space O(V), runtime = 1176 ms, 94.67%
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        if not edges: return None

        g_dict = {key:[] for key in range(n)}
        for u,v in edges:
            g_dict[v].append(u)

        result = []
        for k,v in g_dict.items():
            if not v:
                result.append(k)
        return result
'''