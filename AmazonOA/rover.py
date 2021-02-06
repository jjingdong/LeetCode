'''
Amazon Online Assessment: https://leetcode.com/discuss/interview-question/985703/Amazon-or-OA-or-Rover-Control

A Mars rover is directed to move within a square matrix. It accepts a sequence of
commands to move in any of the four directions from each cell: [UP, DOWN, LEFT or
RIGHT]. The rover starts from cell 0. and may not move diagonally or outside of
the boundary.

Each cell in the matrix has a position equal to:
(row * size) + column
where row and column are zero-indexed, size = row length of the matrix.

Return the final position of the rover after all moves.

Example
n = 4
commands = [RIGHT, UP, DOWN, LEFT, DOWN, DOWN]

The rover path is shown below.

0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15

RIGHT: Rover moves to position 1
UP: Position unchanged, as the move would take the rover out of the boundary.
DOWN: Rover moves to Position 5.
LEFT: Rover moves to position 4
DOWN: Rover moves to position 8
DOWN: The rover ends up in position 12.

The function returns 12.

Function Description
Complete the function roverMove in the editor below.
roverMove has the following parameter(s):
int n: the size of the square matrix
string cmds[m]: the commands

Returns
int: the label of the cell the rover occupies after executing all commands

Constraints
2 <= n <= 20
1 <= |cmds| <= 20

Input Format For Custom Testing

Input from stdin will be processed as follows and passed to the function.
The first line contains an integer, n, denoting the size of the square matrix.
The next line contains an integer, m, the number of commands to follow.
Each of the next m lines contains a command string, cmds[i].

Sample Input :
STDIN Function

4 → n = 4
5 → cmds [] size m = 5
RIGHT → cmds = ['RIGHT', 'DOWN', 'LEFT', 'LEFT', 'DOWN']
DOWN
LEFT
LEFT
DOWN

Sample Output:
8

Explanation:
0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15
Rover starts at position 0
RIGHT → pos 1
DOWN → pos 5
LEFT → pos 4
LEFT → pos 4, No effect
DOWN → pos 8
'''


# command = input()


def rover():
    size = 4
    matrix = [[None for _ in range(size)] for _ in range(size)]

    cmds = ['RIGHT', 'DOWN', 'LEFT', 'LEFT', 'DOWN']
    r, c = 0, 0
    pos = 0
    for direction in cmds:

        if direction == 'RIGHT' and c < size - 1:
            c += 1
        elif direction == 'LEFT' and c > 0:
            c -= 1
        elif direction == 'UP' and r > 0:
            r -= 1
        elif direction == 'DOWN' and r < size - 1:
            r += 1

        print(f'r = {r} c = {c}')

    pos = r * size + c

    return pos

'''
0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15
'''
def matrix_calculation():
    size = 4
    matrix = [[None for _ in range(size)] for _ in range(size)]
    for r in range(size):
        for c in range(size):
            matrix[r][c] = r * size + c

    for i in range(size):
        row = ' '.join([str(x) for x in matrix[i]])
        print(row)

    return pos

'''
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''
def matrix_calculation():
    size = 4
    matrix = [[None for _ in range(size)] for _ in range(size)]
    for r in range(size):
        for c in range(size):
            matrix[r][c] = r * size + c + 1

    for i in range(size):
        row = ' '.join([str(x) for x in matrix[i]])
        print(row)

    return pos


'''
13 14 15 16
9 10 11 12
5 6 7 8
1 2 3 4
'''
def matrix_calculation():
    size = 4
    matrix = [[None for _ in range(size)] for _ in range(size)]
    for r in range(size):
        for c in range(size):
            matrix[r][c] = (size - r - 1) * size + c + 1

    for i in range(size):
        row = ' '.join([str(x) for x in matrix[i]])
        print(row)

    return pos

'''
size = 4
16 15 14 13
9 10 11 12
8 7 6 5
1 2 3 4

size = 5
21 22 23 24 25
20 19 18 17 16
11 12 13 14 15
10 9 8 7 6
1 2 3 4 5
'''
def matrix_calculation():
    size = 4
    matrix = [[None for _ in range(size)] for _ in range(size)]
    for r in range(size):
        for c in range(size):
            if size % 2 == r % 2:
                matrix[r][c] = (size - r - 1) * size + (size - c - 1) + 1
            else:
                matrix[r][c] = (size - r - 1) * size + c + 1

    for i in range(size):
        row = ' '.join([str(x) for x in matrix[i]])
        print(row)

    return pos

'''
Test
'''

n = 4
m = 5
cmds = ['RIGHT', 'DOWN', 'LEFT', 'LEFT', 'DOWN']
expected_output = 8
output = rover()
print(output)
print(output == expected_output)





