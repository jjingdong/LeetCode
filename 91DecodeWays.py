'''
91. Decode Ways
Medium

A message containing letters from A-Z can be encoded into numbers using the following
 mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into
letters using the reverse of the mapping above (there may be multiple ways). For
example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F'
since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.



Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2
'''


class Solution:

    #         A A J F -> 1 1 10 6
    #         K J F -> 11 10 6

    #         1 2
    #           |
    #           B
    #         1 2
    #           |
    #           L

    #         dict = {'A': 1, 'B': 2, ...}
    #         r_dict = {1:'A', 2:'B', ...}

    #                       226
    #                         | i = 2
    #                       /    \
    #                 22 6(F)      2   26(Z)
    #                  |i =1       |i=0
    #             /      \               /
    #        2 26(BF)     226(VF)      226(BZ)
    #        |i=0        |i=-1        |i=-1
    #         |
    #         226(BBF)
    #        |i=-1

    #     1D DP
    #     index = -1  0   1   2
    #                 2   2   6
    #              1
    #                     i
    #                    dp[i] = dp[i-1] + dp[i-2] with condition

    #         a b
    #             i
    #         ------

    # Time O(N) Space O(1)
    # Tabulation
    def numDecodings(self, s: str) -> int:

        size = len(s)
        prepre = 1
        pre = 1

        for index in range(1, size + 1):

            i = index - 1

            count1 = 0
            if int(s[i]) > 0:
                count1 = pre

            count2 = 0
            if i > 0:
                if 9 < int(s[i - 1:i + 1]) < 27:
                    count2 = prepre

            cur = count1 + count2
            prepre = pre
            pre = cur

        return cur


'''
    # Time O(N) Space O(N)
    # Tabulation
    def numDecodings(self, s: str) -> int:

        size = len(s)
        dp = [0] * size
        dp[0] = 1

        for index in range(1, size+1):

            i = index - 1

            digit = int(s[i])
            count1 = 0
            if digit > 0:
                count1 = dp[i-1]

            count2 = 0
            if i > 0:
                digits = int(s[i-1:i+1])
                if 9 < digits < 27:
                    count2 = dp[i-2]

            dp[i] = count1 + count2

        return dp[-1]
'''

'''
    # Time O(N) Space O(N)
    # Recursion + Memorization
    def numDecodings(self, s: str) -> int:

        def helper(i):

            if i == -1:
                return 1

            if i in cache:
                return cache[i]


            digit = int(s[i])
            count1 = 0
            if digit > 0:
                count1 = helper(i-1)

            count2 = 0
            if i > 0:
                digits = int(s[i-1:i+1])
                if 9 < digits < 27:
                    count2 = helper(i-2)

            cache[i] = count1 + count2
            return cache[i]

        cache = {}
        return helper(len(s)-1)
'''

'''
    # Time Limit Exceeded
    # Recursion
    def numDecodings(self, s: str) -> int:

        def helper(i):
            nonlocal count

            if i == -1:
                count += 1
                return

            digit = int(s[i])
            if digit > 0:
                helper(i-1)

            if i > 0:
                digits = int(s[i-1:i+1])
                if 9 < digits < 27:
                    helper(i-2)

        count = 0
        helper(len(s)-1)

        return count
'''

'''
    # Time Limit Exceeded
    # Recursion
    def numDecodings(self, s: str) -> int:

        def helper(i, build):

            if i == -1:
                result.append(build)
                return

            digit = int(s[i])
            if digit > 0:
                build = r_dict[digit] + build
                helper(i-1, build)

            if i > 0:
                digits = int(s[i-1:i+1])
                if 9 < digits < 27:
                    build += r_dict[digits]
                    helper(i-2, build)


        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r_dict = {}
        for i in range(len(chars)):
            r_dict[i+1] = chars[i]
        result = []

        helper(len(s)-1, '')

        # print(result)
        return len(result)
'''
