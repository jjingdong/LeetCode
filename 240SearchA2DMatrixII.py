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

    #         [[1,    4,  7,  11, 15],
    #          [2,    5,  8,  12, 19],
    #          [3,    6,  9,  16, 22],
    #          [10,   13, 14, 17, 24],
    #          [18,   21, 23, 26, 30]]

    #         binary search
    #         target = 5
    #         9 -> 5

    #         binary search II
    #         target = 24
    #         18 -> 21 -> 23 -> 26 -> 17 -> 24

    # Time O(M+N) Space O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix: return None
        size = len(matrix)
        col_size = len(matrix[0])

        r = size - 1
        c = 0
        while c < col_size and 0 <= r:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                c += 1
            else:
                r -= 1

        return False


'''    
    # Note. This is not done.
    # There is a better solution to this
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix: return None
        size = len(matrix)
        col_size = len(matrix[0])

        lo_r, hi_r = 0, size-1
        lo_c, hi_c = 0, col_size - 1
        while lo_r+1 < hi_r and lo_c +1 < hi_c:

            mid_r = (lo_r + hi_r)//2
            mid_c = (lo_c + hi_c)//2

            if target == matrix[mid_r][mid_c]:
                return True
            elif target < matrix[mid_r][mid_c]:
                hi_r = mid_r
                hi_c = mid_c
            else:
                lo_r = mid_r
                lo_c = mid_c

        return False
'''
