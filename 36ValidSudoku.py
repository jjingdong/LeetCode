'''
36. Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits
1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily
solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.

'''


class Solution:

    #     0   1   2   3   4   5   6   7   8   9

    # 0               c=3, r=0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

    # Solution I
    # Time O(MN) Space O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def three(i, j):

            num_set = set()
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    cur = board[r][c]
                    if cur != '.':
                        if cur in num_set:
                            return False
                        else:
                            num_set.add(cur)

        # each row
        for r in range(9):
            num_set = set()
            for c in range(9):
                cur = board[r][c]
                if cur != '.':
                    if cur in num_set:
                        return False
                    else:
                        num_set.add(cur)

        # each col
        for c in range(9):
            num_set = set()
            for r in range(9):
                cur = board[r][c]
                if cur != '.':
                    if cur in num_set:
                        return False
                    else:
                        num_set.add(cur)

        # each 3x3
        for rr in range(3):
            for cc in range(3):
                if three(rr * 3, cc * 3) == False:
                    return False

        return True

    # Solution II
    # Time O(MN) Space O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen_row = set()
        seen_col = set()
        seen_three = set()
        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == '8':
                    a = 0
                if cur != '.':
                    if cur + 'row' + str(r) in seen_row:
                        return False
                    else:
                        seen_row.add(cur + 'row' + str(r))

                    if cur + 'col' + str(c) in seen_col:
                        return False
                    else:
                        seen_col.add(cur + 'col' + str(c))

                    if cur + 'three' + str(r // 3) + '_' + str(c // 3) in seen_three:
                        return False
                    else:
                        seen_three.add(cur + 'three' + str(r // 3) + '_' + str(c // 3))

        return True

