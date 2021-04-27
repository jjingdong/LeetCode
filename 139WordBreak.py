'''
139. Word Break
Medium

Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

'''

    # Solution I, recursion top-down
    # Time(2^N) Space O(N), Time Limit Exceeded
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(i):

            if s[0:i + 1] in wordDict:
                return True

            for j in range(0, i):
                if s[j + 1:i + 1] in wordDict:
                    if helper(j):
                        return True

            return False

        size = len(s)
        return helper(size - 1)

    # Solution II, recursion + memorization top-donw
    # Time(N^2*N) Space O(N), Time Limit Exceeded
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def helper(i):

            if i in cache:
                return True

            # print(f's[0:i+1] = {s[0:i+1]}')
            if s[0:i + 1] in wordDict:
                return True

            for j in range(0, i):

                # print(f'substr = {s[j+1:i+1]}')
                if s[j + 1:i + 1] in wordDict:
                    # print(f'j = {j}')
                    if helper(j):
                        cache[j] = True
                        return True

            return False

        cache = {}
        size = len(s)
        return helper(size - 1)

    # 2d dp
    # Time O() Space O()
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]

        for i in range(size):
            if s[0:i + 1] in wordDict:
                dp[0][i] = True

        for i in range(size):
            for j in range(i):
                print(f'i = {i} j = {j} dp[0][j] = {dp[0][j]}, s[j+1:i+1] = {s[j + 1:i + 1]}')
                if dp[0][j] and s[j + 1:i + 1] in wordDict:
                    dp[0][i] = True
                    break

        # for r in range(size):
        #     print(dp[r])
        return dp[0][-1]


    # 1d dp for LeetCode
    # Time O(N^2*N) Space O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False for _ in range(size)]

        for i in range(size):
            if s[0:i + 1] in wordDict:
                dp[i] = True

        for i in range(size):
            for j in range(i):
                # print(f'i = {i} j = {j} dp[j] = {dp[j]}, s[j+1:i+1] = {s[j+1:i+1]}')
                if dp[j] and s[j + 1:i + 1] in wordDict:
                    dp[i] = True
                    break

        # print(dp)
    return dp[-1]

'''
---------------------------------------------------------------------------------------------
'''


# recursion + memo, Time Limit Exceeded
# Time(N^2*N) Space O(N), Time Limit Exceeded
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def helper(i):

        if i in cache:
            return True

        if i == -1:
            return True

        for j in range(-1, i + 1):

            # print(f'substr = {s[j+1:i+1]}')
            if s[j + 1:i + 1] in wordDict:
                # print(f'j = {j}')
                if helper(j):
                    cache[j] = True
                    return True

        return False

    cache = {}
    size = len(s)
    return helper(size - 1)
    # 2d DP
    # Time O(N^2*N) Space O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [[False for _ in range(size + 1)] for _ in range(size + 1)]

        for r in range(size + 1):
            dp[r][0] = True

        for i in range(1, size + 1):
            for j in range(i):
                # print(f'i = {i} j = {j} dp[0][j] = {dp[0][j]}, s[j+1:i+1] = {s[j+1:i+1]}')
                if dp[0][j] and s[j:i] in wordDict:
                    dp[0][i] = True
                    break

        # for r in range(size):
        #     print(dp[r])
        return dp[0][-1]

    # 1d dp
    # Time O() Space O()
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        size = len(s)
        dp = [False for _ in range(size+1)]
        dp[0] = True

        for i in range(1, size+1):
            result = False
            for j in range(i):
                # print(f'i = {i} j = {j} dp[j] = {dp[j]}, s[j+1:i+1] = {s[j+1:i+1]}')
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break


        # print(dp)
        return dp[-1]



