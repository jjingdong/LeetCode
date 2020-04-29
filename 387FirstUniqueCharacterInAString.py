'''
387. First Unique Character in a String
Easy

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
'''


class Solution:

    # Use HashMap

    # Time O(N) Space O(N)
    #     def firstUniqChar(self, s: str) -> int:

    #         if s is None: return None
    #         if s == '': return -1

    #         import collections
    #         counts = collections.Counter(s)
    #         # Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})

    #         for index, char in enumerate(s):
    #             if counts[char] == 1:
    #                 return index

    #         return -1

    # Time O(N) Space O(N)
    def firstUniqChar(self, s: str) -> int:

        counts = {}
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        for index, char in enumerate(s):
            if counts[char] == 1:
                return index

        return -1






