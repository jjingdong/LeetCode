'''
212. Word Search II
Hard

Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
 
Example:
Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 
Note:
	1.	All inputs are consist of lowercase letters a-z.
	2.	The values of words are distinct.

'''


class Solution:

    # Solution I: not use Trie: Time O(MNJ * 4^K) k=len of word j=no of word, Space O(KJ), time limit exceeded
    #
    # Solution II: use Trie
    #
    # words = ["oath",'ocean',"pea","eat","rain"]
    #   {'o':
    #        {'a':
    #             {'t':
    #                  {'h':
    #                       {'#': True}}},
    #         'c':
    #             {'e':
    #                  {'a':
    #                       {'n': {'#': True}}}}},
    #     'p':
    #         {'e':
    #              {'a':
    #                   {'#': True}}},
    #     'e':
    #         {'a':
    #              {'t':
    #                   {'#': True}}},
    #     'r':
    #         {'a':
    #              {'i':
    #                   {'n':
    #                        {'#': True}}}}}

    # Time O(MN * 4^K) Space O(M), K = length of word, M = no.of letters in Trie, time = 284 ms
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(row, col, a_dict, word):

            if '*' in a_dict and a_dict['*'] == True:
                result.append(word)
                a_dict['*'] = False
                if len(a_dict) == 1:
                    return

            if row < 0 or row > size - 1 or col < 0 or col > col_size - 1:
                return

            if board[row][col] not in a_dict:
                return

            char = board[row][col]
            a_dict = a_dict[board[row][col]]
            word += char

            board[row][col] = '#'
            dfs(row + 1, col, a_dict, word)
            dfs(row, col + 1, a_dict, word)
            dfs(row - 1, col, a_dict, word)
            dfs(row, col - 1, a_dict, word)
            board[row][col] = char

        if not board or not words: return []

        size = len(board)
        col_size = len(board[0])
        result = []
        trie_root = {}
        for word in words:
            w_dict = trie_root
            for c in word:
                if c not in w_dict:
                    w_dict[c] = {}
                w_dict = w_dict[c]
            w_dict['*'] = True

        for i in range(size):
            for j in range(col_size):
                if board[i][j] in trie_root:
                    dfs(i, j, trie_root, '')

        return result

