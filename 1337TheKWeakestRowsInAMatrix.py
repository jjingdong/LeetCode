'''
1337. The K Weakest Rows in a Matrix
Easy

Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians),
return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of
soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are
always stand in the frontier of a row, that is, always ones may appear first and then zeros.

Example 1:

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers for each row is:
row 0 -> 2
row 1 -> 4
row 2 -> 1
row 3 -> 2
row 4 -> 5
Rows ordered from the weakest to the strongest are [2,0,3,1,4]
Example 2:

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers for each row is:
row 0 -> 1
row 1 -> 4
row 2 -> 1
row 3 -> 1
Rows ordered from the weakest to the strongest are [0,2,3,1]


Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
'''


class Solution:

    # vertical check
    # Time O(RC) Space O(1)
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        if not mat: return None

        size = len(mat)
        col_size = len(mat[0])
        index = [-1] * k

        count = 0
        for c in range(col_size):
            for r in range(size):

                if mat[r][c] == 0:
                    if c == 0 or (c > 0 and mat[r][c - 1] != 0):
                        index[count] = r
                        count += 1

                        if count == k:
                            return index

        # if there is not enough rows
        for r in range(size):
            if mat[r][c] == 1:
                index[count] = r
                count += 1
                if count == k:
                    return index

        return index

    # dict + sort
    # Time O(RC + RlogR) Space O(R)
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        if not mat: return None

        size = len(mat)
        col_size = len(mat[0])
        index = [0] * size
        for i in range(size):
            count = 0
            for j in range(col_size):
                count += mat[i][j]
            index[i] = (count, i)

        index = sorted(index, key=lambda x: x[0])[0:k]
        return [x[1] for x in index]


