'''


'''
import collections


class Solution:

    # Time O(N) Space O(N), N is the length of the square, runtime = 100 ms
    # using BFS
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        if not board: return None

        size = len(board)

        # key = square, square
        b_dict = {}
        for r in range(size):
            for c in range(size):
                if board[r][c] != -1:
                    # if (size % 2 == 0 and r % 2 == 0) or (size % 2 == 1 and r % 2 == 1) :
                    if size % 2 == r % 2:
                        square = (size - r - 1) * size + (size - c - 1) + 1
                    else:
                        square = (size - r - 1) * size + c + 1
                    b_dict[square] = board[r][c]
        # print(b_dict)

        # start square, no. of turns
        start = 1
        end = size * size
        no_turns = 0
        visited = set()
        queue = collections.deque([(start, no_turns)])
        while queue:
            square, no_turns = queue.popleft()
            # if square == end:
            #     return no_turns

            for next_move in range(square + 1, square + 7):

                if next_move in b_dict:
                    next_move = b_dict[next_move]

                if next_move >= end:
                    return no_turns + 1

                if next_move not in visited:
                    visited.add(next_move)
                    queue.append((next_move, no_turns + 1))

        return -1






