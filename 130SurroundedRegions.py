'''
130. Surrounded Regions
Medium

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

'''


class Solution:

    # Time O(MN) Space O(K) K = no. of O, which is not captured
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(row, col):
            if row < 0 or col < 0 or row > size - 1 or col > col_size - 1:
                return

            if board[row][col] == 'X' or board[row][col] == 'A':
                return

            board[row][col] = 'A'

            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)

        if not board or not board[0]: return
        size = len(board)
        col_size = len(board[0])
        for i in range(col_size):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[size - 1][i] == 'O':
                dfs(size - 1, i)

        for i in range(1, size - 1):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][col_size - 1] == 'O':
                dfs(i, col_size - 1)

        for i in range(size):
            for j in range(col_size):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
