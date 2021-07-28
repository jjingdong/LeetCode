'''
59. Spiral Matrix II
Medium

Given a positive integer n, generate an n x n matrix filled with elements
from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        length = len(matrix)
        rowLength = len(matrix[0])

        minI = 0
        maxI = length - 1
        minJ = 0
        maxJ = rowLength - 1
        count = 0
        while minI <= maxI and minJ <= maxJ:

            for j in range(minJ, maxJ + 1):
                count += 1
                matrix[i][j] = count
            minI += 1

            for i in range(minI, maxI + 1):
                count += 1
                matrix[i][j] = count
            maxJ -= 1

            if minI <= maxI and minJ <= maxJ:
                for j in range(maxJ, minJ - 1, -1):
                    count += 1
                    matrix[i][j] = count
                maxI -= 1

            if minI <= maxI and minJ <= maxJ:
                for i in range(maxI, minI - 1, -1):
                    count += 1
                    matrix[i][j] = count
                minJ += 1

        result = []
        for r in range(n):
            row = []
            for c in range(n):
                row.append(matrix[r][c])
            result.append(row)

        return result
