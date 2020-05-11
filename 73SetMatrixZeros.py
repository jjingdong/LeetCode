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

    # Time O(MNK), K = M+N Space O(1)
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


