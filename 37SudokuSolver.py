'''
37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9
3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique
solution.
The given board size is always 9x9.
'''


class Solution:

    # box index = row//3 * 3
    #         0   1   2   3   4   5
    #     0
    #     1
    #     2
    #     3               x   x   x
    #     4               x   x   x
    #     5               x   x   x

    # Time O(9!) Space O(1), runtime = 720 ms
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def can_place(r, c, value):

            for i in range(size):
                if board[r][i] == value:
                    return False
                if board[i][c] == value:
                    return False

            n = size // 3
            for i in range(n):
                for j in range(n):
                    if board[r // 3 * 3 + i][c // 3 * 3 + j] == value:
                        return False

            return True

        def sudoku():

            for i in range(9):
                for j in range(9):
                    if board[i][j] == empty:
                        for num in range(1, 10):
                            if can_place(i, j, str(num)):
                                board[i][j] = str(num)
                                if sudoku(): return True
                                board[i][j] = empty

                        return False

            return True

        size = 9
        empty = '.'
        sudoku()
