'''
1197. Minimum Knight Moves
Medium

In an infinite chess board with coordinates from -infinity to +infinity, you have
 a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two
squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].
It is guaranteed the answer exists.



Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]


Constraints:

|x| + |y| <= 300

'''


class Solution:

    # 0,0 -> [2,1],[1,2],[-1,2],[-2,1],[2,-1],[-1,-2],[1,-2],[2,-1]

    # x,y -> [x+2,y+1], [x+1,y+2], [x-1,y+2].....

    # DP[i][j] = min(DP[i-1][j-2],.....)

    # symmetric, 1/8 of the grid repeat 8 times

    #     -2  -1  0   1   2 = col
    # 2   4   1   2    1   4
    # 1   1   2   3   2   1
    # 0   2   3   0   3   2
    # -1  1   2   3   2   1
    # -2  4   1   2   1   4
    # row

    # Time O(2^N) Space O(2^N)
    # runtime = 64 ms
    def minKnightMoves(self, x: int, y: int) -> int:

        @lru_cache
        def helper(r, c):

            if r == 0 and c == 0:
                return 0
            elif (abs(r) == 2 and abs(c) == 1) or (abs(r) == 1 and abs(c) == 2):
                return 1
            # position (1,1), (2,0), (0,2) is calculated outside this +pos,+pos rectangle area
            elif abs(r) + abs(c) == 2:
                return 2

            return min(helper(abs(r - 2), abs(c - 1)), helper(abs(r - 1), abs(c - 2))) + 1

        if x is None or y is None: return None
        return helper(abs(x), abs(y))


'''
    # Time Limit Exceeded
    def minKnightMoves(self, x: int, y: int) -> int:

        def helper(r, c):

            if r == 0 and c == 0:
                return 0
            elif abs(r) + abs(c) == 3:
                return 1
            elif abs(r) + abs(c) == 2:
                return 2

            a = None
            if (abs(r-2), abs(c-1)) in cache:
                a = cache[(abs(r-2), abs(c-1))]
            else:
                a = helper(abs(r-2), abs(c-1))

            b = None
            if (abs(r-1), abs(c-2)) in cache:
                b = cache[(abs(r-1), abs(c-2))]
            else:
                b = helper(abs(r-1), abs(c-2))

            return min(a, b) + 1

        if x is None or y is None: return None

        cache = {(0,0): 0, (2,1):1, (1,2):1, (1,1):2}
        return helper(abs(x), abs(y))
'''

'''
    # Note. this is not a working solution.
    # Reason. Cannot use a DP table, since the iteration doesn't build up by i increase, then j increase
    def minKnightMoves(self, x: int, y: int) -> int:

        size = max(abs(x), abs(y))
        dp = [[float('inf') for _ in range(2*size+1)] for _ in range(2*size+1)]

        dp[0][0] = 0
        dp[2][1] = 1
        dp[1][2] = 1
        # position (1,1), (2,0), (0,2) is calculated outside this +pos,+pos rectangle area
        dp[1][1] = 2
        dp[2][0] = 2
        dp[0][2] = 2


        for i in range(size):
            for j in range(size):
                dp[i][j] = min(dp[i][j],dp[i-1][j-2],dp[i-2][j-1])+1

        print(dp)

        return dp[abs(x)][abs(y)]
'''
