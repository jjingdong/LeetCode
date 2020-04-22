'''
1046. Last Stone Weight
Easy

We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
	•	If x == y, both stones are totally destroyed;
	•	If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
 
Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 
Note:
	1.	1 <= stones.length <= 30
	2.	1 <= stones[i] <= 1000
'''
import heapq


class Solution:

    # [2, 7, 4, 1, 8, 1]
    # 7 vs 8  [2, 4, 1, 1, 1]
    # 2 vs 4  [2, 1, 1, 1]
    # 2 vs 1  [1, 1, 1]
    # 1 vs 1  [1]
    #
    # Use heap
    # Python heapq is minHeap
    # Java Priority Queue is minHeap
    # Solution: * (-1) to make it maxHeap
    # Note: Donot think of

    # Time O(NlogN) Space O(1)
    # Python, converting a list to a heap is done in-place, so O(1)
    def lastStoneWeight(self, stones: List[int]) -> int:

        if stones is None: return None

        if stones == []: return 0
        if len(stones) == 1: return stones[0]
        if len(stones) == 2: return abs(stones[0] - stones[1])

        for i in range(len(stones)):
            stones[i] *= -1

        while len(stones) > 1:
            heapq.heapify(stones)
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            value = -abs(s1 - s2)

            if value != 0:
                heapq.heappush(stones, value)

        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0




