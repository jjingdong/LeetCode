'''
289. Game of Life
Medium

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
	1.	Any live cell with fewer than two live neighbors dies, as if caused by under-population.
	2.	Any live cell with two or three live neighbors lives on to the next generation.
	3.	Any live cell with more than three live neighbors dies, as if by over-population..
	4.	Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
Example:
Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:
	1.	Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
	2.	In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

'''


class Solution:

    # Time O(MN) Space O(1), runtime = 36 ms
    def gameOfLife(self, board: List[List[int]]) -> None:

        size = len(board)
        col_size = len(board[0])
        dir = {(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)}

        live_to_die = -1
        die_to_live = 2
        for i in range(size):
            for j in range(col_size):
                sum = 0
                for d1, d2 in dir:
                    r = i + d1
                    c = j + d2
                    if r >= 0 and r < size and c >= 0 and c < col_size:
                        if board[r][c] == 1 or board[r][c] == live_to_die:
                            sum += 1

                if (board[i][j] == 1 or board[i][j] == live_to_die) and (sum < 2 or sum > 3):
                    board[i][j] = live_to_die
                elif (board[i][j] == 0 or board[i][j] == die_to_live) and sum == 3:
                    board[i][j] = die_to_live

        for i in range(size):
            for j in range(col_size):
                if board[i][j] == live_to_die:
                    board[i][j] = 0
                elif board[i][j] == die_to_live:
                    board[i][j] = 1

        return board


'''   
    # Time O(MN) Space O(MN), runtime = 32 ms
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def calculate(row, col):
            sum = 0
            for d1, d2 in dir:
                r = row + d1
                c = col + d2
                if r >= 0 and r < size and c >= 0 and c < col_size:
                    sum += b2[r][c]

            if b2[row][col] == 1:
                if sum < 2 or sum > 3:
                    return 0
                elif sum == 2 or sum == 3:
                    return 1
            elif b2[row][col] == 0 and sum == 3:
                return 1
            else:
                return b2[row][col]


        size = len(board)
        col_size = len(board[0])
        b2 = [[board[row][col] for col in range(col_size)] for row in range(size)]
        dir = {(0,1), (1,0), (-1,0), (0,-1), (-1,1), (1,-1), (1,1), (-1,-1)}

        for i in range(size):
            for j in range(col_size):
                board[i][j] = calculate(i,j)

        return board
'''
