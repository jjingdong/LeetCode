'''
72. Edit Distance
Hard

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
	1.	Insert a character
	2.	Delete a character
	3.	Replace a character
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''


class Solution:

    # solution I: Brute Force  --- Time Limit Exceeded
    #
    # solution II: Dynamic Programming - cache
    #
    # solution III: Dynamic Programming - tabulation
    # Levenshtein distance
    #
    #     horse
    #     ros
    #     horse -> rorse -> rose -> ros
    #     output = 3
    #
    #     intention
    #     execution
    #     intention -> inention -> enention -> exention -> exection -> execution
    #     output = 5
    #
    #    s: XXXXXXX i
    #    t: YYYYYYY j

    #           h  o  r  s  e
    #      [[0, 1, 2, 3, 4, 5],
    # r     [1, 1, 2, 2, 3, 4],
    # o     [2, 2, 1, 2, 3, 4],
    # s     [3, 3, 2, 2, 2, 3]]


    # Time O(MN) Space O(MN)
    def minDistance(self, word1: str, word2: str) -> int:

        if not word1 and not word2: return 0

        col_size = len(word1)
        size = len(word2)
        dp = [[0 for _ in range(col_size + 1)] for _ in range(size + 1)]

        for i in range(size + 1):
            dp[i][0] = i

        for c in range(col_size + 1):
            dp[0][c] = c

        for r in range(1, size + 1):
            for c in range(1, col_size + 1):
                if word1[c - 1] == word2[r - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1

        # print(dp)
        return dp[-1][-1]



    # Time O(MN), M = length of word1, N = length of word2
    # Space O(MN)
    def minDistance(self, word1: str, word2: str) -> int:

        def helper(i, j):
            # base case
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            # recursive case
            key = (i, j)
            if key in cache:
                return cache[key]

            if word1[i] == word2[j]:
                cache[(i, j)] = helper(i + 1, j + 1)
                return cache[(i, j)]
            else:
                insert = 1 + helper(i, j + 1)
                delete = 1 + helper(i + 1, j)
                replace = 1 + helper(i + 1, j + 1)
                cache[(i, j)] = min(insert, delete, replace)
                return cache[(i, j)]

        cache = {}
        # cache = {(i,j): counter}
        return helper(0, 0)


'''
    # Time O(MN), Space O(MN), 
    # runtime = 288 ms
    # Using cache
    def minDistance(self, word1: str, word2: str) -> int:
        def operation(w1, w2):

            if not w1 and not w2:
                return 0
            if not w1:
                return len(w2)
            if not w2:
                return  len(w1)

            key = w1 + '_' + w2
            if key in cache:
                return cache[key]
            else:
                if w1[0] == w2[0]:
                    return operation(w1[1:], w2[1:])
                else:
                    insert = 1 + operation(w1, w2[1:])
                    delete =  1 + operation(w1[1:], w2)
                    replace = 1 + operation(w1[1:], w2[1:])
                    cache[key] = min(insert, delete, replace)
                return cache[key]

        # cache = {'word1_word2': count}
        cache = {}
        return operation(word1, word2)
'''

'''    
    # Time O(3^N) Space O(3^N), 
    # Using Brute Force, time limit exceeded
    def minDistance(self, word1: str, word2: str) -> int:

        def operation(w1, w2):

            if not w1 and not w2:
                return 0
            if not w1:
                return len(w2)
            if not w2:
                return  len(w1)
            if w1[0] == w2[0]:
                return operation(w1[1:], w2[1:])
            else:
                insert = 1 + operation(w1, w2[1:])
                delete =  1 + operation(w1[1:], w2)
                replace = 1 + operation(w1[1:], w2[1:])
                return min(insert, delete, replace)

        return operation(word1, word2)
'''

