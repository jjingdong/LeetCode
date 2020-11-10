'''
1478. Allocate Mailboxes
Hard

Given the array houses and an integer k. where houses[i] is the location of the ith house along a street,
your task is to allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:

Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5
Example 2:

Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
Example 3:

Input: houses = [7,4,6,1], k = 1
Output: 8
Example 4:

Input: houses = [3,6,14,10], k = 4
Output: 0


Constraints:

n == houses.length
1 <= n <= 100
1 <= houses[i] <= 10^4
1 <= k <= n
Array houses contain unique integers.
'''


class Solution:


# Time O(N^3) Space O(N^2)
def minDistance(self, houses: List[int], k: int) -> int:
    if not houses: return None
    if k < 1: return None

    size = len(houses)
    if k >= size: return 0
    houses = sorted(houses)

    # cost table
    cost = [[0 for row in range(size)] for col in range(size)]
    for row in range(size):
        for col in range(size):
            # if odd no. the median index
            # if even no. between 2 median index
            median_index = (row + col) // 2
            for index in range(row, col + 1):
                cost[row][col] += abs(houses[index] - houses[median_index])
    # cost for eg.1 = [[0, 3, 7, 13, 25], [0, 0, 4, 6, 18], [0, 0, 0, 2, 12], [0, 0, 0, 0, 10], [0, 0, 0, 0, 0]]
    # cost for eg.2 = [[0, 1, 3, 12, 25], [0, 0, 2, 9, 22], [0, 0, 0, 7, 13], [0, 0, 0, 0, 6], [0, 0, 0, 0, 0]]
    # print(f'cost = {cost}')

    dp = [[float('inf') for row in range(k)] for col in range(size)]
    for i in range(size):
        dp[i][0] = cost[0][i]
    # print(dp)

    # DP table
    for i in range(size):
        for j in range(i):
            for mb in range(1, k):
                dp[i][mb] = min(dp[i][mb], dp[j][mb - 1] + cost[j + 1][i])
                # print(f'cost = {cost[j+1][i]} i = {i} j = {j}')

    # print(f'dp = {dp}')3,
    # dp for eg.1 = [[0, inf, inf], [3, 0, inf], [7, 3, 0], [13, 5, 2], [25, 13, 5]]
    # dp for eg.2 = [[0, inf], [1, 0], [3, 1], [12, 3], [25, 9]]

    return dp[-1][-1]