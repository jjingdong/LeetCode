'''
1277. Count Square Submatrices with All Ones
Medium

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
 
Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:
Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.
 
Constraints:
	•	1 <= arr.length <= 300
	•	1 <= arr[0].length <= 300
	•	0 <= arr[i][j] <= 1
'''


class Solution:

    # Solution I: Dynamic Programming (half way) --- Time Limit Exceeded
    # [[0,1,1,1],
    # [1,1,1,1],
    # [0,1,1,1]]
    # side 1: d[i,j] = matrix[i,j]
    # side 2: d[i,j] = matrix[i-1,j] or matrix[i,j-1] or matrix[i-1,j-1] or matrix[i,j]
    # side 3: d3[i,j] = d[i-1,j] or d[i,j-1] or d[i-1,j-1] or d[i,j]
    # side 4: d4[i,j] = d3[i-1,j] or d3[i,j-1] or d3[i-1,j-1] or d3[i,j]
    #
    # Solution II: Dynamic Programming
    # [[0,1,1,1],
    # [1,1,1,1],
    # [0,1,1,1]]
    # dp[i,j] = min(matrix[i-1,j], matrix[i,j-1], matrix[i-1,j-1]) + 1, if dp[i,j] != 0

    # Time O(MN), Space O(1)
    def countSquares(self, matrix: List[List[int]]) -> int:

        count = 0
        size = len(matrix)
        col_size = len(matrix[0])
        for i in range(0, size):
            for j in range(0, col_size):
                if matrix[i][j] != 0 and i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                count += matrix[i][j]
        return count


'''
    # Time O(MNS), M=row, N=col,S=side, Space O(MN)
    def countSquares(self, matrix: List[List[int]]) -> int:
        import copy

        count = 0
        dp = matrix
        size = len(matrix)
        col_size = len(matrix[0])
        for i in range(size):
            for j in range(col_size):
                if dp[i][j] == 1:
                    count += 1         
        for side in range(1, len(matrix)):
            newdp = copy.deepcopy(dp)
            for i in range(side, size):
                for j in range(side, col_size):
                    if dp[i][j] != 0:
                        newdp[i][j] = dp[i-1][j] and dp[i][j-1] and dp[i-1][j-1]
                        if newdp[i][j] == 1:
                            count += 1
            dp = newdp

        return count
'''


