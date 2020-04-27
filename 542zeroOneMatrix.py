'''
542. 01 Matrix
Medium

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
 
Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 '''


class Solution:

    # Input:
    # [[0,0,0],
    #  [0,1,0],
    #  [1,1,1]]
    #
    # Output:
    # [[0,0,0],
    #  [0,1,0],
    #  [1,2,1]]
    #
    # Note. 2 passes is enough, because it's in a loop

    # Time O() Space O()
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        length = len(matrix)
        rowLen = len(matrix[0])

        # Note. i is the row length
        dis = [[float('inf') for i in range(rowLen)] for j in range(length)]

        for i in range(length):
            for j in range(rowLen):
                if matrix[i][j] == 0:
                    dis[i][j] = 0
                else:
                    if i > 0:
                        # look top
                        dis[i][j] = min(dis[i][j], dis[i - 1][j] + 1)
                    if j > 0:
                        # look left
                        dis[i][j] = min(dis[i][j], dis[i][j - 1] + 1)

        for i in range(length - 1, -1, -1):
            for j in range(rowLen - 1, -1, -1):
                if i < length - 1:
                    # look down
                    dis[i][j] = min(dis[i][j], dis[i + 1][j] + 1)
                if j < rowLen - 1:
                    # look right
                    dis[i][j] = min(dis[i][j], dis[i][j + 1] + 1)

        return dis


