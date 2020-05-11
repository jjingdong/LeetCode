'''
73. Set Matrix Zeroes
Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:
	•	A straight forward solution using O(mn) space is probably a bad idea.
	•	A simple improvement uses O(m + n) space, but still not the best solution.
	•	Could you devise a constant space solution?
'''


class Solution:

    # Solution I
    #
    # Solution II

    # Time O(MN) Space O(1), Solution II
    def setZeroes(self, matrix: List[List[int]]) -> None:

        if matrix is None: return None

        size = len(matrix)
        col_size = len(matrix[0])
        clear_first_col = False

        for i in range(size):
            if matrix[i][0] == 0:
                clear_first_col = True
            for j in range(1, col_size):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for c in range(1, col_size):
            if matrix[0][c] == 0:
                for r in range(size):
                    matrix[r][c] = 0

        for r in range(size):
            if matrix[r][0] == 0:
                matrix[r] = [0] * col_size

        if clear_first_col == True:
            for i in range(size):
                matrix[i][0] = 0


'''
    # Time O(MNK), K = M+N Space O(1), Solution I
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        size = len(matrix)
        col_size = len(matrix[0])

        for i in range(size):
            for j in range(col_size):
                if matrix[i][j] == 0:

                    # Modify
                    for r in range(size):
                        if matrix[r][j] != 0:
                            matrix[r][j] = None
                    for c in range(col_size):
                        if matrix[i][c] != 0:
                            matrix[i][c] = None

        for i in range(size):
            for j in range(col_size):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
'''





