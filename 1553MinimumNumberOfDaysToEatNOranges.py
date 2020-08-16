'''
1553. Minimum Number of Days to Eat N Oranges
Hard

There are n oranges in the kitchen and you decided to eat some of these
oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat
n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat
2*(n/3) oranges.
You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.



Example 1:

Input: n = 10
Output: 4
Explanation: You have 10 oranges.
Day 1: Eat 1 orange,  10 - 1 = 9.
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1.
Day 4: Eat the last orange  1 - 1  = 0.
You need at least 4 days to eat the 10 oranges.
Example 2:

Input: n = 6
Output: 3
Explanation: You have 6 oranges.
Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
Day 3: Eat the last orange  1 - 1  = 0.
You need at least 3 days to eat the 6 oranges.
Example 3:

Input: n = 1
Output: 1
Example 4:

Input: n = 56
Output: 6


Constraints:

1 <= n <= 2*10^9
'''


class Solution:

    # Time Limit Exceeded when input = 9209408
    def minDays(self, n: int) -> int:

        #         Eat one orange.
        #         If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
        #         If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.

        #                             10
        #                     /               |               \
        #                 9                   5                   X
        #           /    |   \            /    |   \
        #         8      X    3          4     X   X
        #     /|\            /|\
        # 7   4  X          1 X 1
        # /|\ /|\          /|\  /|\
        #                 0        0

        # index = 0 1 2 3 4 5 6 7 8 9 10
        #     1     1 2 3 4 5 6 7 8 9 10
        #   n/2     x x x   x.  x   x
        #           1 2 3 3 4 4 5 4 5 5   ---> how many ways to get to 10
        # 2*(n/3)   x x   x.x   x x   x
        #           1 2 2 3 4 3 4 4 3 4

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            if i % 2 == 0 and i % 3 == 0:
                dp[i] = min(dp[i // 2], dp[(i // 3)], dp[i - 1]) + 1
            elif i % 2 == 0:
                dp[i] = min(dp[i - 1], dp[i // 2]) + 1
            elif i % 3 == 0:
                dp[i] = min(dp[i - 1], dp[(i // 3)]) + 1
            else:
                dp[i] = dp[i - 1] + 1

        return dp[-1]
