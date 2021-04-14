'''
1335. Minimum Difficulty of a Job Schedule
Hard

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work
on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule
is the sum of difficulties of each day of the d days. The difficulty of a day is
the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the
i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for
the jobs return -1.



Example 1:


Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15
Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843


Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
'''

#         day 1            day 2
#          0               i
#         [6,5,4,3,2   |   1], d = 2
#              6           1            -> 7
#                  j
#         -------------------->

#         6,     |      5,4,3,2,1
#         6                 5    ----> 11
#         6, 5    |     4,3,2,1
#         6                 4   --> 10


#         [9,9,9], d = 4
#         invalid ----------> -1


#         [1,|     1,    |     1], d = 3


#         [7,1,7,1,     |       7,       | 1], d = 3
#            7                  7          1       = 15


#         [11,  |  111,|  22 |  222 |33,   |   333,44,444], d = 6
#         11 + 111+22+222+33+444 = 843


#              index =        0 1 2 3 4 5
#                             6,5,4,3,2,1        d=3

#     j
# xxxxx|1                                  xxxx|21     xxx|321     xx|4321    x|54321                  d=2
#    //\\                                                            /

#   xxxx|2|1  xxx|32|1 xx|432|1  x|5432|1                         x|5|4321                             d=1


# index
#         0           j j+1  index
#         XXXXXXXXXXXXX|XXXXXX   size,d
#                       ------
#            d-1          1

#         -------------  + max(cost of finish j+1 to index in one day)


#                         d=1    d=2   d=3
# index =0 item =6        6      X
# index = 1               6      11
# index =2                6            6,5,4 -> 3 days     65|4    6|54    10 or 11
# index = 3               6
# index =4                6
# index = 5               6            6,5,4,3,2,1   ----> 3 days       6,5,4,3,2,|1    in 2 days
#                                                                       ----------
#                                                                       6,5,4,3,|2,1    in 2 days
#                                                                       -------
#         max_cost from r to c

# index =        0 1 2 3 4 5   c
#                6,5,4,3,2,1        d=3

#    r           6 6 6 6 6 6
#                  5 5 5 5 5
#                    4 4 4 4
#                      3 3 3
#                        2 2
#                          1


#         helper(d, index):
#             result = inf
#             for j in range(0, index):
#                    result = min(result, helper(d-1, j) + max_cost(j+1,index))

#             return result

    #         6,5,4,3,2,1 d = 2
    #             6,5,4,3,2 | 1
    # difficulty = 5          1
    # total = 5+1 = 6
    #
    #         9,9,9 d = 4
    #         invalid input
    #
    #              1,1,1 d = 3
    # difficulty = 1 1 1
    # totoal =     1+1+1 = 3
    #
    #         7,1,7,1,7,1    d = 3
    #              7,1,7,1  |  7  |  1
    # difficulty =    7        7     1
    # totoal =        7+7+1 = 15
    #
    #         11,111,22,222,33,333,44,444, d = 6
    #              11 | 111 | 22 | 222 | 33 | 333,44,444
    # difficulty = 11   111   22   222   33   444
    # totoal =     11+111+22+222+33+44 = 843

    #         6,5,4,3,2,1
    #
    #         6,5,4,3,2       1     d=2
    #
    # index = 0                        j   j+1   i
    #         xxxxxxxxxxxxxxxxxxxxxxxxxx | xxxxxxx
    #                     d-1                 1
    #
    #         dp[j][d-1] + max_cost[j+1][i]
    #         dp[i][d] = min(dp[i][d], dp[j][d-1] + max_cost[j+1][i])
    #   i = 0.......size
    #   j = 0.......i
    #   d_index = 1.......d

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        if not jobDifficulty: return None
        if not d or d < 0: return None

        size = len(jobDifficulty)
        if size < d: return -1

        @lru_cache(None)
        def max_cost(index1, index2):
            if index1 == index2:
                return jobDifficulty[index1]
            return max(jobDifficulty[index1:index2+1])


        @lru_cache(None)
        def helper(index, day):
            if day == 1:
                return max_cost(0, index)
            res = float("inf")
            for j in range(index):
                res = min(res, helper(j, day - 1) + max_cost(j+1, index))
            return res

        res = helper(size-1, d)
        return res

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        size = len(jobDifficulty)

        if d > size:
            return -1

        max_cost = [[0 for _ in range(size)] for _ in range(size)]
        for r in range(size):
            for c in range(r, size):
                if r == c:
                    max_cost[r][c] = jobDifficulty[r]
                else:
                    max_cost[r][c] = max(jobDifficulty[r:c + 1])

        # print(max_cost)

        dp = [[float('inf') for _ in range(d)] for _ in range(size)]
        for i in range(size):
            dp[i][0] = max_cost[0][i]

        # print(dp)
        for i in range(size):
            for j in range(i):
                for d_index in range(1, d):
                    dp[i][d_index] = min(dp[i][d_index], dp[j][d_index - 1] + max_cost[j + 1][i])

        # print(dp)

        return dp[-1][-1]


    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        if not jobDifficulty: return None
        if not d or d < 0: return None

        size = len(jobDifficulty)
        if size < d: return -1

        @lru_cache(None)
        def oneDayDifficulty(index1, index2):
            if index1 + 1 == index2:
                return jobDifficulty[index1]
            return max(jobDifficulty[index1:index2])

        @lru_cache(None)
        def helper(index, day):
            if day == 1:
                return oneDayDifficulty(0, index)
            res = float("inf")
            for j in range(1, index):
                res = min(res, helper(j, day - 1) + oneDayDifficulty(j, index))
            return res

        res = helper(size, d)
        return -1 if res == float('inf') else res



