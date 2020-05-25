'''
96. Unique Binary Search Trees
Medium

Share
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''


class Solution:

    # Solution I: Recursion ------ Time Limit Exceeded
    # node = i
    # 1 ... (i-1) on the left
    # (i+1) ... n on the right
    #
    # Solution II: Dynamic programming, tabulation

    # Time O(N^2) Space O(N)
    def numTrees(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        count = 0
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]


'''        
    # Time O(N) Space O(2^N), using recursion
    def numTrees(self, n: int) -> int:

        self.cache = {}
        if n == 0: return 1
        elif n == 1: return 1
        elif n == 2: return 2
        elif n in self.cache:
            return self.cache[n]

        count = 0
        for i in range(1, n+1):
            count += self.numTrees(i-1) * self.numTrees(n-i)
        self.cache[n] = count
        return count
'''