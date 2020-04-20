
'''
49. Group Anagrams
Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''


class Solution:

    # a  b  c  d  e  f  g  h  i  j  k  l  m  n
    # o  p  q  r  s  t  u  v  w  x  y  z

    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,

    # Time O(KN)
    # Space O(KN)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        primes = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31,
                  'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
                  'w': 83, 'x': 89, 'y': 97, 'z': 101}

        countMap = {}

        for word in strs:  # word
            count = 1
            for c in word:
                count *= primes[c]
            if count not in countMap:
                countMap[count] = [word]
            else:
                countMap[count].append(word)

        return countMap.values()


