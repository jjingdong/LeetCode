'''
79. Word Search
Medium

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 
Constraints:
	•	board and word consists only of lowercase and uppercase English letters.
	•	1 <= board.length <= 200
	•	1 <= board[i].length <= 200
	•	1 <= word.length <= 10^3
Accepted
'''


class Solution:

    # Time O(MN * 4^K), K=len(word), Space O(K), runtime = 372 ms
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row, col, index):
            nonlocal found

            if index == len(word):
                found = True
                return
            if row < 0 or col < 0 or row >= size or col >= col_size:
                return
            if board[row][col] != word[index]:
                return
            if found:
                return

            board[row][col] = '#'
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for i, j in dirs:
                dfs(row + i, col + j, index + 1)
            board[row][col] = word[index]

        if not board or not word: return False

        found = False
        size = len(board)
        col_size = len(board[0])
        for i in range(size):
            for j in range(col_size):
                dfs(i, j, 0)

        return found