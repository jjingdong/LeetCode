'''
694. Number of Distinct Islands
Medium

Given a non-empty 2D array grid of 0's and 1's, an island is a group of
1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same
as another if and only if one island can be translated (and not rotated or
reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
'''


class Solution:

    # Time O(MN) Space O(MN)
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

#         11011
#         10000
#         00001
#         11011

#         *11
#          1

#         for i...n:
#             for j...n:
#                 cell

#         cell -> dfs, mark 1 to 0, count no. of islands

#         1. save index of the island, then check the index diff
#         2. save index diff from start index of the island.

#         *3. save the path of the island. e.g. udlrudlr  ---> better approach


