'''
1192. Critical Connections in a Network
Hard

There are n servers numbered from 0 to n-1 connected by undirected server-to-server
connections forming a network where connections[i] = [a, b] represents a connection
between servers a and b. Any server can reach any other server directly or indirectly
through the network.

A critical connection is a connection that, if removed, will make some server unable
to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
'''


class Solution:

    #     # Time O() Space O(), runtime = 2280
    #     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

    #         if not n or not connections: return None

    #         graph = collections.defaultdict(list)

    #         for u,v in connections:
    #             graph[u].append(v)
    #             graph[v].append(u)

    #         disc = [None for _ in range(n)]
    #         low_link = [None for _ in range(n)]
    #         cur_time = 0
    #         result = []

    #         def dfs(node, parent):
    #             nonlocal cur_time

    #             if disc[node] == None:
    #                 disc[node] = cur_time
    #                 low_link[node] = cur_time
    #                 cur_time += 1

    #                 for neighbor in graph[node]:

    #                     if neighbor != parent:
    #                         dfs(neighbor, node)

    #                         low_link[node] = min(low_link[node], low_link[neighbor])

    #         dfs(0, None)

    #         for u,v in connections:
    #             if low_link[u] > disc[v] or low_link[v] > disc[u]:
    #                 result.append([u,v])

    #         return result

    # Time O(E+V)
    # Space O(E+5V), V=traverse, V=recursion stack, V=low_link, V=disc, E+V=dictionary
    # runtime = 2180 ms, 96.47%
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        if not n or not connections: return None

        graph = collections.defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [None for _ in range(n)]
        low_link = [None for _ in range(n)]
        cur_time = 0
        result = []

        def dfs(node, parent):
            nonlocal cur_time

            if disc[node] is None:
                disc[node] = cur_time
                low_link[node] = cur_time
                cur_time += 1

                for neighbor in graph[node]:

                    if neighbor != parent:
                        dfs(neighbor, node)

                        if low_link[neighbor] > disc[node]:
                            result.append((node, neighbor))

                        low_link[node] = min(low_link[node], low_link[neighbor])

        dfs(0, None)

        return result


'''
    # Time O() Space O(), runtime = 2352 ms
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        if not n or not connections: return None

        graph = collections.defaultdict(list)

        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [None for _ in range(n)]
        low_link = [None for _ in range(n)]

        result = []
        cur_dis = 0

        def dfs(node, parent):
            nonlocal cur_dis

            if disc[node] is None:
                disc[node] = cur_dis
                low_link[node] = cur_dis
                cur_dis += 1

                for neighbor in graph[node]:
                    if not disc[neighbor]:
                        dfs(neighbor, node)

                if parent is not None:
                    l = min([low_link[i] for i in graph[node] if i!=parent]+[low_link[node]])
                else:
                    l = min(low_link[i] for i in graph[node]+[low_link[node]])
                low_link[node] = l

        dfs(0, None)

        for u,v in connections:
            if low_link[u] > disc[v] or low_link[v] > disc[u]:
                result.append([u,v])

        return result
'''