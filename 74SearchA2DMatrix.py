'''
74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
	•	Integers in each row are sorted from left to right.
	•	The first integer of each row is greater than the last integer of the previous row.
Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''


class Solution:

    # index =    0    1    2    3    4   5    6    7    8    9    10   11
    #           [1,   3,   5,   7,  10,  11,  16,  20,  23,  30,  34,  50]
    # row,col = 0,0  0,1  0,2  0,3  1,0  1,1  1,2  1,3  2,0  2,1  2,2  2,3
    # index = 4, row = 4/rowSize = 4/4 = 1, col = 4%4 = 0
    # index = 5, row = 5/rowSize = 5/4 = 1, col = 5%4 = 1

    # Time O(logMN) Space O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix is None: return None
        if matrix == []: return False

        size = len(matrix)
        rowSize = len(matrix[0])
        lowI = 0
        highI = size * rowSize - 1

        while lowI <= highI:

            midI = (highI + lowI) // 2
            row, col = divmod(midI, rowSize)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                highI = midI - 1
            else:
                lowI = midI + 1

        return False
