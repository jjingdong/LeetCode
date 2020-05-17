'''
242. Valid Anagram
Easy

Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Note: You may assume the string contains only lowercase alphabets.
Follow up: What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''


class Solution:

    # Time O(N) Space O(1)
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        anagram = collections.Counter(s)

        for c in t:
            if c in anagram:
                anagram[c] -= 1
            else:
                return False

        for v in anagram.values():
            if v != 0:
                return False

        return True

