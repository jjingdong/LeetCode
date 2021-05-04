'''
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
'''

#         arr = un iq ue, no. of combination = 3+3+1, (k * n!/(k!(n-k)!))????

#             un  iq  ue  uniq    ique    unue      unique
#             2   2   2   4       4       0         0
#         output = 4


#         arr = "cha","r","act","ers"
#             cha r act ers
#             3   1   3   3
#                 char    chaact  chaers  ract    rers    acters
#                 4               6       4               6


#         index   0       1       2       3
#                 cha     r       act     ers


#                 cha         r        act         ers

#         cha     chacha-0    char-4   charact-0   charers-0
#         r
#         act
#         ers

#             cha     r       act     ers
#             r


#     # Time O() Space O()
#     # result = ['', 'un', 'iq', 'uniq', 'ue', 'unue', 'ique', 'unique']
#     def maxLength(self, arr: List[str]) -> int:

#         def helper(build, index):

#             result.append(build)

#             for i in range(index+1):
#                 helper(arr[i]+build, i-1)

#         result = []
#         size = len(arr)
#         helper('', size-1)


#     # Time O() Space O()
#     # result = ['', 'un', 'iq', 'uniq', 'ue', 'unue', 'ique', 'unique']
#     def maxLength(self, arr: List[str]) -> int:

#         def helper(build, index):

#             if index == -1:
#                 # print(f'build = {build} index = {index}')
#                 result.append(build)
#                 return

#             helper(build, index-1)
#             helper(arr[index] + build, index-1)

#         result = []
#         size = len(arr)
#         helper('', size-1)
#         # print(result)

def maxLength(self, arr: List[str]) -> int:
    size = len(arr) + 1
    dp = [[('', 0) for _ in range(size)] for _ in range(size)]

    for r in range(size):
        dp[r][0] = ('', 0)

    for c in range(size):
        dp[0][c] = ('', 0)

    # for r in range(size):
    #     if arr[r-1] == len(set(arr[r-1])):
    #         dp[r][r] = (arr[r-1], len(arr[r-1]))
    #     else:
    #         string = ', '.join(str(e) for e in set(arr[r-1]))
    #         dp[r][r] = (string, 0)

    for r in range(1, size):
        for c in range(r + 1, size):
            # print(f'r = {r} c = {c}')

            if set(arr[c - 1]) & set(dp[r][c - 1][0]):
                print('here')
                dp[r][c] = (dp[r][c - 1][0], dp[r][c - 1][1])
            else:
                dp[r][c] = (dp[r][c - 1][0] + arr[c - 1], len(dp[r][c - 1][0] + arr[c - 1]))

    for r in range(size):
        print(dp[r])

    max_value = 0
    for r in range(size):
        for c in range(size):
            max_value = max(max_value, dp[r][c][1])

    return max_value

    def maxLength(self, arr: List[str]) -> int:

        size = len(arr)
        dp = [[('', 0) for _ in range(size)] for _ in range(size)]

        for r in range(0, size):
            for c in range(r, size):
                # print(f'r = {r} c = {c}')

                if set(arr[c - 1]) & set(dp[r][c - 1][0]):
                    print('here')
                    dp[r][c] = (dp[r][c - 1][0], dp[r][c - 1][1])
                else:
                    dp[r][c] = (dp[r][c - 1][0] + arr[c - 1], len(dp[r][c - 1][0] + arr[c - 1]))

        for r in range(size):
            print(dp[r])

        max_value = 0
        for r in range(size):
            for c in range(size):
                max_value = max(max_value, dp[r][c][1])

        return max_value