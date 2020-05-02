'''
1167. Minimum Cost to Connect Sticks
Medium

You have some sticks with positive integer lengths.
You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.
Return the minimum cost of connecting all the given sticks into one stick in this way.
 
Example 1:
Input: sticks = [2,4,3]
Output: 14
Example 2:
Input: sticks = [1,8,3,5]
Output: 30
 
Constraints:
	•	1 <= sticks.length <= 10^4
	•	1 <= sticks[i] <= 10^4
'''


class Solution:

    # Use heapq -> minHeap
    # heapq is a binary heap, with O(log n) push and O(log n) pop

    # Time O(NlogN) Space O(N)
    def connectSticks(self, sticks: List[int]) -> int:

        if sticks is None: return 0
        if sticks == []: return 0
        if len(sticks) == 1: return 0

        sum = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            one = heapq.heappop(sticks)
            two = heapq.heappop(sticks)
            cost = one + two
            sum += cost
            heapq.heappush(sticks, cost)

        return sum



