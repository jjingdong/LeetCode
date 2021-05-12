'''
Question Prompt (1 of 1)
Problem Statement
You’re developing a one-player game for people to pass the time with.
The player is given a grid of tiles from 0 to 9 like this:
4 4 4 4
5 5 5 4
2 5 7 5
The player selects one of these tiles, and that tile will disappear,
along with all the connected tiles of the same number. Tiles can be
connected adjacently up, down, left, or right.
Write a function that takes in a grid of tiles, and the row and column
indexes of a selected tile on the grid, and returns the number of tiles
that will disappear.
The grid is guaranteed to be rectangular. All values in the grid will
be integers between 0 and 9. The input row and column are zero-indexed
integers, and will always be on the grid.
Example Input
Given the grid above, say that the 4 in the upper left corner (row 0
and column 0) was selected. In that case, 5 tiles would disappear as
shown below.
 [4] >4< >4< >4<
  5   5   5  >4<
  2   5   7   5
If the 5 just below it is selected (row 1 and column 0), these four
tiles disappear. Note that tiles are not connected diagonally, so
\the 5 in the bottow right does not disappear. We would output 4.
  4   4   4   4
 [5] >5< >5<  4
  2  >5<  7   5
Finally, if no tiles around the selected tile have the same number,
only the selected tile disappears. Here, if we choose the 7 at row 2
column 2, we return 1.
  4   4   4   4
  5   5   5   4
  2   5  [7]  5
Public test 1
Input:
1 4
0 3 3 3 3 3 3
0 1 1 1 1 1 3
0 2 2 0 2 1 4
0 1 2 2 2 1 3
0 1 1 1 1 1 3
0 0 0 0 0 0 0
Expected Output:
13
Public test 2
Input:
1 1
0 3 3 3 3 3 3
0 1 1 1 1 1 3
0 2 2 0 2 1 4
0 1 2 2 2 1 3
0 1 1 1 1 1 3
0 0 0 0 0 0 0
Expected Output:
13
Public test 3
Input:
3 0
0 3 3 3 3 3 3
0 1 1 1 1 1 3
0 2 2 0 2 1 4
0 1 2 2 2 1 3
0 1 1 1 1 1 3
0 0 0 0 0 0 0
Expected Output:
12
 Public test 4
Input:
0 0
0 3 3 3 3 3 3
0 1 1 1 1 1 3
0 2 2 0 2 1 4
0 1 2 2 2 1 3
0 1 1 1 1 1 3
0 0 0 0 0 0 0
Expected Output:
12
 Public test 5
Input:
2 0
4 4 4 4
5 5 5 4
2 5 7 5
Expected Output:
1

'''

def game(row, col, matrix) -> int:
    def helper(r, c):
        nonlocal total

        if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
            return

        if matrix[r][c] != target:
            return

        if matrix[r][c] == target:
            total += 1
            matrix[r][c] = '#'

        helper(r - 1, c)
        helper(r, c - 1)
        helper(r + 1, c)
        helper(r, c + 1)

    total = 0
    target = matrix[row][col]
    helper(row, col)

    return total


'''
Test
'''
r = 1
c = 4
matrix = [[0, 3, 3, 3, 3, 3, 3],
        [0, 1, 1, 1, 1, 1, 3],
        [0, 2, 2, 0, 2, 1, 4],
        [0, 1, 2, 2, 2, 1, 3],
        [0, 1, 1, 1, 1, 1, 3],
        [0, 0, 0, 0, 0, 0, 0]]
output = 13
print(game(r, c, matrix))

