'''
787. Cheapest Flights Within K Stops
Medium

There are n cities connected by m flights. Each flight starts from city u and arrives
at v with a price w.

Now given all the cities and flights, together with starting city src and the destination
dst, your task is to find the cheapest price from src to dst with up to k stops. If
there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red
in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked
blue in the picture.


Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
'''


class Solution:

    # Solution I: DFS
    #
    # Solution II: DFS + Memorization
    #
    # Solution III: BFS
    #
    # Solution III: Dijkstra's Algorithm

    #     Eg.1
    #     f_dict = {0: {1: 100, 2: 500}, 1: {2: 100}})
    #     heap = [(100, 1, 1), (500, 2, 1)]
    #     min = (100, 1, 1)
    #     heap = [(200, 2, 2), (500, 2, 1)]
    #     output: 200
    #
    #     Eg.2
    #     f_dict = {0: {1: 100, 2: 500}, 1: {2: 100}})
    #     heap = [(100, 1, 1), (500, 2, 1)]
    #     min = (100, 1, 1)
    #     output: 500

    # Time O(), sapce O(), runtime = 100 ms
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        f_dict = collections.defaultdict(dict)
        for u, v, w in flights:
            f_dict[u][v] = w

        heap = [(0, src, 0)]
        while heap:
            price, city, stop = heapq.heappop(heap)
            if city == dst:
                return price
            if stop <= K:
                for j in f_dict[city]:
                    heapq.heappush(heap, (price + f_dict[city][j], j, stop + 1))
        return -1


'''    
    # Time, there is a bug on this
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        if not flights: return None

        c_dict = collections.defaultdict(list)
        for [u,v,w] in flights:
            c_dict[u].append((v,w))

        prices = [float('inf') for _ in range(n)]    
        prices[src] = (0)

        level = 0
        queue = collections.deque([(src,level)])
        while queue:
            start, level = min(queue, key=lambda x: prices[x[0]])
            queue.remove((start,level))
            while queue and start not in c_dict:
                start, level = min(queue, key=lambda x: prices[x[0]])
                queue.remove((start,level))

            if level > K + 1: break

            for end, price in c_dict[start]:
                if prices[start] + price < prices[end]:
                    prices[end] = prices[start] + price
                queue.append((end, level+1))

        if prices[dst]== float('inf'): return -1
        return prices[dst]
'''

'''   
    # Time O() Space O(), Using DFS, Time Limit Exceeded
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        if not flights: return None

        c_dict = collections.defaultdict(list)
        for [u,v,w] in flights:
            c_dict[u].append((v,w))

        # print(c_dict)

        # dfs
        def dfs(start, price, level, path):
            nonlocal count

            # print(f'start = {start} price = {price} level = {level} path = {path}')

            if level > K + 1:
                return

            if start == dst:
                count = min(count, price)
                return

            if start in c_dict:
                for v,w in c_dict[start]:
                    path.append(u)
                    dfs(v, price+w, level+1, path)-
                    path.pop()

        count = float('inf')
        dfs(src, 0, 0, [])


        if count == float('inf'): return -1 
        return count
'''

'''
    # Note. floyd Warshall algorithm won't working here, since it require input k stops
    # Time O(N^3) Space O(N^2)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
    
        for u, v, w in flights:
            matrix[u][v] = w
    
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
    
        return matrix[src][dst]
'''