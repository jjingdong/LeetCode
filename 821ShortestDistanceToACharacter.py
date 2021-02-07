'''
821. Shortest Distance to a Character
Easy

Given a string s and a character c that occurs in s, return an array of integers
answer where answer.length == s.length and answer[i] is the shortest distance from
 s[i] to the character c in s.



Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]


Constraints:

1 <= s.length <= 104
s[i] and c are lowercase English letters.
c occurs at least once in s.

'''


class Solution:

    # index = 0   1   2   3   4   5   6   7   8   9   10  11
    #         l   o   v   e   l   e   e   t   c   o    d   e,    c = "e"
    #         [3, 2,  1   0,  1,  0,  0,  1,  2,  2,  1,  0]

    # array, hashmap

    #         [None, None, None, None, ...]

    #         l   o   v   e   l   e   e   t   c   o    d   e
    #         |
    #         1
    #             |
    #         2   1
    #                 |
    #         3   2   1
    #                      |
    #                      0
    #                         |
    #                         1
    #                             |
    #                             0
    #                                 |
    #                                 0
    #                                     |
    #                                     1
    #                                         |
    #                                         2
    #                                             |
    #                                             3
    #                                                 |
    #                                                 4
    #                                     1,4 2,3, 3,2 4,1 |
    #                                                      0

    # Time O(N) Space O(1)
    def shortestToChar(self, s: str, c: str) -> List[int]:

        if not s or not c: return None

        result = [float('inf') for _ in range(len(s))]

        pre_index = None
        find_first_c = False
        for index, char in enumerate(s):

            if find_first_c == False:
                if char == c:
                    result[index] = 0
                    pre_index = index
                    find_first_c = True
                    for i in range(0, index):
                        result[i] = index - i

            else:
                if char != c:
                    result[index] = index - pre_index

                else:
                    result[index] = 0
                    for i in range(pre_index + 1, index):
                        result[i] = min(result[i], index - i)
                    pre_index = index

        return result

