'''
1216. Valid Palindrome III
Hard

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by
removing at most k characters from it.

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Example 2:

Input: s = "abbababa", k = 1
Output: true


Constraints:

1 <= s.length <= 1000
s consists of only lowercase English letters.
1 <= k <= s.length
'''


class Solution:

    #         s = abcdeca  k= 2
    #
    #             l     r, count = 0
    #             abcdeca
    #              /              \
    #         s[l]=s[r]       s[l]!=s[r] -> X remove
    #         l++
    #         r--
    #         l   r
    #         bcdec
    #          /              \
    #         s[l]=s[r]       s[l]!=s[r]
    #                         count ++
    #                         /       \
    #                 l  r               l  r
    #                 bcde->X               cdec
    #                                     /       \
    #                             s[l]=s[r]       s[l]!=s[r] -> X remove
    #                              l++
    #                              r--
    #                              lr
    #                              de
    #                           /                     \
    #                 s[l]=s[k] -> X remove      s[l]!=s[k]
    #                                             count += 0
    #                                                 /\
    #                                               d    e

    # s = 'abcd'
    # [0,     1,      2,      3]
    # [inf,   0,      1,      2]
    # [inf,   inf,    0,      1]
    # [inf,   inf,    inf,    0]

    # s = 'abcd'
    # dp = [0, 1, 2, 3]

    #     #Time O(N^2) Space O(N)
    #     Note. this is not the solution
    #     Didn't implement 1D DP
    #     def isValidPalindrome(self, s: str, k: int) -> bool:

    #         size = len(s)
    #         dp = [0] * size

    #         for i in range(size-2, -1, -1):
    #             for j in range(i+1, size):
    #                 if s[i] == s[j]:
    #                     dp[j] = dp[j-1]
    #                 else:
    #                     dp[j] = min(dp[j], dp[j-1]) + 1

    #         print(dp)
    #         return dp[size-1] <= k

    # Time O(N^2) Space O(N^2)
    def isValidPalindrome(self, s: str, k: int) -> bool:

        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            dp[i][i] = 0

        for i in range(size - 2, -1, -1):
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

        # for i in range(size):
        #     print(dp[i])

        return dp[0][size - 1] <= k


'''
    # Time O(2^N) Space O(N), time limit exceeded
    def isValidPalindrome(self, s: str, k: int) -> bool:

        def helper(l,r,count):
            nonlocal result

            # print(f'l = {l} r = {r} count = {count}')


            if result == True:
                return True

            if count > k:
                return False

            if l >= r:
                result = True
                return True

            if s[l] == s[r]:
                return helper(l+1, r-1, count)

            else:
                return helper(l+1,r,count+1) or helper(l,r-1,count+1)

        result = False
        helper(0, len(s)-1,0)
        return result     
'''
