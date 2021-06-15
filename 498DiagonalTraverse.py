'''
498. Diagonal Traverse
Medium

Given an m x n matrix mat, return an array of all the elements of the array
in a diagonal order.



Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105

'''


class Solution:

    #                 0 1 2
    #         mat = [[1,2,3,11],   0
    #                [4,5,6,22],   1
    #                [7,8,9,33]]   2

    #         0,0   r+c = 0
    #         0,1  1,0       r+c = 1
    #         0,2  1,1  2,0  r+c = 2
    #         0,3  1,2  2,1  r+c = 3
    #              1,3  2,2  r+c = 4 -> len(m)-1+len(n)+1
    #                   2,3
    #  {0: [(0, 0)], 1: [(0, 1), (1, 0)], 2: [(0, 2), (1, 1), (2, 0)],
    #   3: [(1, 2), (2, 1)], 4: [(2, 2)]})

    # Time O((M+N)log(M+N) + MN) Space O(M+N)
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        size = len(mat)
        col_size = len(mat[0])
        n_dict = collections.defaultdict(list)
        for r in range(size):
            for c in range(col_size):
                n_dict[r + c].append((r, c))

        # print(n_dict)
        result = []
        go_down = False
        for count in range(size + col_size - 1):
            value = n_dict[count]
            if go_down is False:
                value.sort(key=lambda x: -x[0])

            for v in value:
                r, c = v[0], v[1]
                result.append(mat[r][c])

            if go_down:
                go_down = False
            else:
                go_down = True

        return result
