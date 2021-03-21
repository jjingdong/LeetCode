'''
727. Minimum Window Subsequence
Hard

Given strings S and T, find the minimum (contiguous) substring W of S,
so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return
the empty string "". If there are multiple such minimum-length windows,
return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.


Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
'''


class Solution:

    #         S = "abcdebdde", T = "bde"
    #         W = minimum substring of S = "bcde"
    #         delete chars from T -> make T

    #      a  b  c  d  e  b  d  d  e
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # b   [0, 1, 1, 2, 3, 4, 1, 2, 3, 4]
    # d   [0, 1, 2, 3, 3, 4, 5, 2, 3, 4]
    # e   [0, 1, 2, 3, 4, 4, 5, 6, 7, 4]

    # This is not done
    # Time O() Space O()
    def minWindow(self, S: str, T: str) -> str:

        size = len(T)
        col_size = len(S)
        dp = [[float('inf') for _ in range(col_size + 1)] for _ in range(size + 1)]
        for r in range(size + 1):
            dp[r][0] = 0
        for c in range(1, col_size + 1):
            dp[0][c] = 0

        # for i in range(size+1):
        #     print(dp[i])

        for i in range(1, size + 1):
            for j in range(1, col_size + 1):
                if T[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1] + 1

        if dp[-1][-1] == float('inf'):
            return ''

        for r in range(size + 1):
            print(dp[r])
        print(dp[-1][-1])
        start = 0
        end = col_size - 1
        for r in range(1, size + 1):
            for c in range(1, col_size + 1):
                if dp[r][c] == dp[-1][-1]:
                    start = r
                    end = c
                    break

        return S[start:end]