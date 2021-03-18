'''
983. Minimum Cost For Tickets
Medium

In a country popular for train travel, you have planned some train travelling
one year in advance.  The days of the year that you will travel is given as an
array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get
a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given
list of days.



Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.


Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
'''


class Solution:

    #         days = [1,4,6,7,8,20], costs = [2,7,15]
    #
    #         1 day pass
    #         7 day pass
    #         30 day pass
    #
    #                 1,  4,  6,  7,  8,  20
    #
    #        *day 1   2                               7                          15
    #         day 2                                   |
    #         day 3                                   |
    #        *day 4   2           7       15
    #         day 5               |       |           |
    #        *day 6               |       |       /   |   \
    #        *day 7               |       |       2   7   15
    #        *day 8               |       |
    #         day 9               |       |
    #
    #         recursion
    #
    #     days  0   1           4       6   7   8
    #     day = 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
    #
    #  cost 2   0   2           4       6   8   10                                              12
    #  cost 7   0   2           4       6   7   9                                               11
    #  cost 15  0   2           4       6   7   9                                               11
    #
    #                 dp[i][j] = min(dp[i-1][j], dp[i][j-s]+ costs[k])  if don't consider the date which is travelling
    #
    #                 dp[j] = min(dp[j], dp[j-s] + costs[k])
    #
    #     days  0                           7   8
    #     day = 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
    #
    #  cost 7   0                           7   14                                              21
    #  cost 2   0                           2   4                                               6
    #  cost 15  0

    #     days  0   1           4       6   7   8
    #     day = 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
    #
    #  cost 7   0   7           14      21  28  35
    #  cost 2   0   2           4       6   8   10
    #  cost 15  0



    # Time O(N),N=last day + 1 Space O(30)
    # reuse the 30 days range
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        size = 30
        dp = [float('inf')] * size
        for i in range(0, days[0]):
            dp[i % size] = 0
        # print(dp)

        # days = [1,4,6,7,8,20]
        # i = 0, 1, 2,3 , 4, 5, 6,7
        for i in range(days[0], days[-1] + 1):
            # travel
            # i = 1, 4, 6, 8, 20
            if i in days:
                a = costs[0]
                b = costs[1]
                c = costs[2]
                if i > 1:
                    a = dp[(i - 1) % size] + costs[0]
                if i > 7:
                    b = dp[(i - 7) % size] + costs[1]
                if i > 30:
                    c = dp[(i - 30) % size] + costs[2]

                # print(f'i={i} a={a} b={b} c={c}')
                dp[i % size] = min(a, b, c)

            # not travel
            else:
                dp[i % size] = dp[(i - 1) % size]

        # print(dp)

        return dp[(days[-1]) % size]


    # Time O(N) Space O(N)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        size = days[-1] + 1
        dp = [float('inf')] * size

        for i in range(0, days[0]):
            dp[i] = 0
        # print(dp)

        # days = [1,4,6,7,8,20]
        # i = 0, 1, 2,3 , 4, 5, 6,7
        for i in range(1, size):
            # travel
            # i = 1, 4, 6, 8, 20
            if i in days:
                a = dp[i - 1] + costs[0]
                b = costs[1]
                c = costs[2]
                if i > 7:
                    b = dp[i - 7] + costs[1]
                if i > 30:
                    c = dp[i - 30] + costs[2]

                dp[i] = min(a, b, c)

            # not travel
            else:
                dp[i] = dp[i - 1]

        # print(dp)

        return dp[-1]


