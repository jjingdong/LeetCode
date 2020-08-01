'''
516. Longest Palindromic Subsequence
Medium

Given a string s, find the longest palindromic subsequence's
length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".


Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''


class Solution:


# bbbab
# |   |
# l   r
# A. left == right:
#     bba
#     | |
#     l r
#     B. left != right:
#         bb    or    ba
#         ||          ||
#         lr          lr
# Solution I: recursion
#
# Solution II: DP memorization
#
# Solution III: DP tabulation

# Time O() ----> this is not done
def longestPalindromeSubseq(self, s: str) -> int:
    #         b b b a b
    #         0 1 2 3 4
    #     0   1 2 3 3 4
    #     1     1 2 2 3
    #     2       1 1 3
    #     3         1 1
    #     4           1
    #
    #          b b b a b
    #     dp   0 1 2 3 4
    #
    #         dp[i][j] = 2 + dp[i+1][j-1]
    #         dp[i] = 2 + dp[i+1] from previous
    #
    #         dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    #         dp[i] = max(dp[i+1], dp[i])

    size = len(s)
    dp = [1] * size

    for i in range(size - 1, -1, -1):

        for j in range(i + 1, size):

            if s[i] == s[j]:
                dp[i] = 2 + dp[i + 1]
            else:
                dp[i] = max(dp[i + 1], dp[i])

    print(dp)
    return dp[0]


'''
    # Time O(n^2) Space O(N), runtime = 2456 ms
    def longestPalindromeSubseq(self, s: str) -> int:

#         b b b a b
#         0 1 2 3 4
#     0   1 2 3 3 4
#     1     1 2 2 3
#     2       1 1 3
#     3         1 1
#     4           1
#         dp[i][j]

        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, size):

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]
'''

''' 
    # Time O(N^2) Space O(N), Time Limit Exceeded
    def longestPalindromeSubseq(self, s: str) -> int:

        def subseq(l,r):

            if l > r:
                return 0
            if l == r:
                return 1

            if (l,r) in s_dict:
                return s_dict[(l,r)]

            left,right = s[l], s[r]   
            if left == right:
                s_dict[(l,r)] = 2 + subseq(l+1, r-1) 
            else:
                s_dict[(l,r)] = max(subseq(l+1, r), subseq(l, r-1))
            return s_dict[(l,r)]

        # {(i,j): value}
        s_dict = {}
        if not s: return 0
        return subseq(0,len(s)-1)
'''

'''
    # Time O(N^2) Space O(1), Time Limit Exceeded, using recursion
    def longestPalindromeSubseq(self, s: str) -> int:

        def subseq(l,r):

            if l > r:
                return 0
            if l == r:
                return 1
            left,right = s[l], s[r]   

            if left == right:
                return 2 + subseq(l+1, r-1)
            else:
                return max(subseq(l+1, r), subseq(l, r-1))

        if not s: return 0
        return subseq(0,len(s)-1)
'''

