'''
240. Search a 2D Matrix II
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
	•	Integers in each row are sorted in ascending from left to right.
	•	Integers in each column are sorted in ascending from top to bottom.
Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
'''


class Solution:

    # start i = size -1, j = 0
    # if cur > target: row -= 1
    # if cur < target: col+= 1

    # Time O(M+N) Space O(1), runtime = 44 ms
    def searchMatrix(self, matrix, target):

        if not matrix or not target: return False

        size, col_size = len(matrix), len(matrix[0])
        row, col = size - 1, 0
        while col < col_size and row >= 0:
            cur = matrix[row][col]
            if cur == target:
                return True
            elif cur < target:
                col += 1
            else:
                row -= 1

        return False


'''
    # This is not a solution
    # Time O() Space O()
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

# target = 20
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# matrix[mid_i][mid_j] = 9, lo_i = 0, hi_i = 4, lo_j = 0, hi_j = 4
# matrix[mid_i][mid_j] = 17, lo_i = 2, hi_i = 4, lo_j = 2, hi_j = 4, mid_i = 3, mid_j = 3
# if diff between lo and mid, mid and hi is 1: then create one/two lists


        if not matrix or not target: return False

        size = len(matrix)
        col_size = len(matrix[0])
        lo_i, hi_i, lo_j, hi_j = 0, size-1, 0, col_size-1
        while hi_i - lo_i > 1 and hi_j - hi_i > 1:
            mid_i, mid_j = lo_i + (hi_i-lo_i)//2, lo_j + (hi_j-lo_j)//2
            mid = matrix[mid_i][mid_j]
            if mid == target:
                return True
            elif mid < target:
                lo_i, lo_j = mid_i, mid_j    
            else:
                hi_i, hi_j = mid_i, mid_j

        print(f'{lo_i}, {hi_i}, {lo_j}, {hi_j}')
'''
