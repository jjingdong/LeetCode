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

    # Time O(N), N = 30, Space O(N) Note. can set the array to size 31. But I haven't implement
    # runtime = 48 ms
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        a = 0




'''
    # Time O(N), N = last day to travel + 1, Space O(N)
    # runtime = 48 ms
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = [float('inf')] * (days[-1]+1)
        for j in range(0, days[0]):
            dp[j] = 0

        temp = float('inf')
        for i in range(days[0], days[-1]+1):
            if i in days:

                b = dp[i-7]+costs[1] if i > 7 else costs[1]
                c = dp[i-30]+costs[2] if i > 30 else costs[2]

                dp[i] = min(dp[i], dp[i-1]+costs[0], b, c)
                temp = dp[i]
            else:
                dp[i] = temp

        return dp[-1]
'''

'''
        Note. I couldnot come up with recursive solution    
        def ticket(amount, day_index):
            nonlocal min_amount

            print(f'day = {day}, amount = {amount}')


            # if day >= days[-1]:
            #     min_amount = min(min_amount, amount)
            #     return

            ticket(day+1, amount+costs[0], day_index+1)
            ticket(day+7, amount+costs[1], day_index+1)
            ticket(day+30, amount+costs[2], day_index+1)


        if not days: return 0

        min_amount = float('inf')
        pass_1, pass_7, pass_30 = 1, 7, 30
        for i in range(len(days)):
            ticket(day_index)
        return min_amount
'''



