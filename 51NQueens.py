'''
51. N-Queens
Hard

The n-queens puzzle is the problem of placing n queens on an n×n
chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens
puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution:

    # Fill the board from top to bottom
    # 1. reach bottom: solved
    # 2. backtrack + recursion
    #
    # diagonals: r+c = r1+c1, r-c = r1-c1
    #
    # one way: when place a pickeupdate the Queen, and row, col the diagonal arrays
    # another way: when place a piece to nothing. When checking availability, check diagonals, row and col

    # Time O(N!) Space O(N^2), runtime = 304 ms
    def solveNQueens(self, n: int) -> List[List[str]]:

        def can_place(r, c):

            if matrix[r][c] == queen:
                return False

            for i in range(n):
                if matrix[r][i] == queen or matrix[i][c] == queen:
                    return False

            for i in range(n):
                for j in range(n):
                    if i != r and j != c and matrix[i][j] == queen and (i + j == r + c or i - j == r - c):
                        return False

            return True

        def p():
            lst = []
            for i in range(n):
                row = ''
                for j in range(n):
                    row += matrix[i][j]
                lst.append(row)

            return lst

        def nqs(row):

            if row == n:
                result.append(p())
                return

            for col in range(n):
                if can_place(row, col):
                    matrix[row][col] = queen
                    nqs(row + 1)
                    matrix[row][col] = empty

        queen, empty = 'Q', '.'
        matrix = [[empty for _ in range(n)] for _ in range(n)]
        result = []
        nqs(0)

        return result