'''
54. Spiral Matrix
Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution:

    # [[ 1, 2, 3 ],
    #  [ 4, 5, 6 ],
    #  [ 7, 8, 9 ]]
    # Each loop goes to 4 directions

    # Time O(MN) Space O(MN)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if matrix is None: return None
        if matrix == []: return []

        spiralOrder = []
        i, j = 0, 0
        length = len(matrix)
        rowLength = len(matrix[0])

        minI = 0
        maxI = length - 1
        minJ = 0
        maxJ = rowLength - 1
        while minI <= maxI and minJ <= maxJ:

            for j in range(minJ, maxJ + 1):
                spiralOrder.append(matrix[i][j])
            minI += 1

            for i in range(minI, maxI + 1):
                spiralOrder.append(matrix[i][j])
            maxJ -= 1

            if minI <= maxI and minJ <= maxJ:
                for j in range(maxJ, minJ - 1, -1):
                    spiralOrder.append(matrix[i][j])
                maxI -= 1

            if minI <= maxI and minJ <= maxJ:
                for i in range(maxI, minI - 1, -1):
                    spiralOrder.append(matrix[i][j])
                minJ += 1

        return spiralOrder


