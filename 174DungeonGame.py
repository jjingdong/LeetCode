'''
174. Dungeon Game
Hard

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
 
Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
-2 (K)
-3
3
-5
-10
1
10
30
-5 (P)
 
Note:
	•	The knight's health has no upper bound.
	•	Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

'''


class Solution:

    #         7-2-3+3+1-5 = 1
    #         point <= 0: die
    #         minimum sum to travel from bottom right corner to [0][0]
    #
    #         brute force: dfs or bfs
    #         dynamic programming: only right and down

    # Time O() Space O()    ----> dp(1) is not done
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        if not dungeon or not dungeon[0]: return dungeon

        size = len(dungeon)
        col_size = len(dungeon[0])
        dp = [None] * size

        dp[size - 1] = max(1, dungeon[size - 1][col_size - 1] * (-1) + 1)
        # print(dp)
        for i in range(size - 2, -1, -1):
            for j in range(col_size - 2, -1, -1):
                dp[i] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])

        return dp[0]


'''   
    # Time O(MN) Space O(1), runtime = 76 ms
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        if not dungeon or not dungeon[0]: return dungeon

        size = len(dungeon)
        col_size = len(dungeon[0])   
        dungeon[size-1][col_size-1] = max(1, dungeon[size-1][col_size-1] * (-1) + 1)

        for j in range(col_size-2, -1, -1):
            dungeon[size-1][j] = max(1, dungeon[size-1][j+1] - dungeon[size-1][j])
        for i in range(size-2, -1, -1):
            dungeon[i][col_size-1] = max(1, dungeon[i+1][col_size-1] - dungeon[i][col_size-1])
        for i in range(size-2, -1, -1):
            for j in range(col_size-2, -1, -1):
                dungeon[i][j] = max(1, min(dungeon[i+1][j]-dungeon[i][j], dungeon[i][j+1]-dungeon[i][j]))

        return dungeon[0][0]
'''

