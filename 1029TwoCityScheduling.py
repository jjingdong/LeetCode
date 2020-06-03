'''
1029. Two City Scheduling
Easy

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
 
Example 1:
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 
Note:
	1.	1 <= costs.length <= 100
	2.	It is guaranteed that costs.length is even.
	3.	1 <= costs[i][0], costs[i][1] <= 1000

'''


class Solution:

    #                A   B
    #   person 0   [[10,20],    ---> 10 A
    #   person 0    [30,200],   ---> 30 A
    #   person 0    [400,50],   ---> 50 B
    #   person 0    [30,20]]    ---> 20 B
    #
    # Attempt: backtracking -------> Not a solutjion
    #           p0, p1, p2, p3
    #           /             \
    #        a0b1              b0a1                  p0, p1
    #       /    \           /    \
    # a0b1a2b3 a0b1b2a3 a0b1a2b3 a0b1b2a3              p2, p3
    #
    # Solution I: Heap
    #
    # Solution II: Sort

    # Time O(NlogN) Space O(1), runtime = 40 ms
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        if not costs: return 0

        count = 0
        costs = sorted(costs, key=lambda cost: cost[0] - cost[1])
        for i in range(len(costs) // 2):
            count += costs[i][0]

        for i in range(len(costs) // 2, len(costs)):
            count += costs[i][1]
        return count


'''
    # Time O(NlogN) Space O(N), runtime = 44 ms
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        if not costs: return 0

        count = 0
        lst = []
        for i in range(len(costs)):
            # min cost for city A
            diff = costs[i][0] - costs[i][1]
            heapq.heappush(lst, (diff, i))

        for j in range(len(costs)//2):
            diff, index = heapq.heappop(lst)
            count += costs[index][0]

        for j in range(len(costs)//2):
            diff, index = heapq.heappop(lst)
            count += costs[index][1]

        return count
'''
