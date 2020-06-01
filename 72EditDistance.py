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

    # Time O(MN) Space O(MN), using tabulation, runtime = 204 ms
    def minDistance(self, word1: str, word2: str) -> int:

        if not word1 and not word2: return 0
        if not word1: return len(word2)
        if not word2: return len(word1)

        size, col_size = len(word1), len(word2)
        dp = [[None for _ in range(col_size + 1)] for _ in range(size + 1)]

        for i in range(size + 1):
            dp[i][0] = i
        for j in range(col_size + 1):
            dp[0][j] = j

        for i in range(1, size + 1):
            for j in range(1, col_size + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[-1][-1]


'''    
    # Time O(MN), Space O(MN), 
    # runtime = 236 ms
    # Using cache
    def minDistance(self, word1: str, word2: str) -> int:

        def operation(i, j):

            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            key = (i,j)
            if key in cache:
                return cache[key]
            else:
                if word1[i] == word2[j]:
                    return operation(i+1, j+1)
                else:
                    insert = 1 + operation(i, j+1)
                    delete =  1 + operation(i+1, j)
                    replace = 1 + operation(i+1, j+1)
                    cache[key] = min(insert, delete, replace)
                return cache[key]

        if not word1 and not word2: return 0
        # cache = {(i,j)}: count}
        cache = {}
        return operation(0, 0)
'''

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

