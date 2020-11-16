'''
832. Flipping an Image
Easy

Given a binary matrix A, we want to flip the image horizontally, then invert it, and
return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For
example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
'''


class Solution:

    #         [[1,1,0],
    #          [1,0,1],
    #          [0,0,0]]
    #         flip horizontally:
    #         [[0,1,1],
    #          [1,0,1],
    #          [0,0,0]]
    #         invert:
    #         [[1,0,0],
    #          [0,1,0],
    #          [1,1,1]]

    # Time O(MN) Space O(1)
    # runtime = 52 ms
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        if not A: return A

        size = len(A)
        col_size = len(A[0])

        for r in range(size):
            for c in range(col_size // 2):
                A[r][c], A[r][col_size - c - 1] = A[r][col_size - c - 1] ^ 1, A[r][c] ^ 1
            if col_size % 2 == 1:
                A[r][col_size // 2] = A[r][col_size // 2] ^ 1

        return A
