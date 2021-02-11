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

    # Time O(N) Space O(N)
    def isAnagram(self, s: str, t: str) -> bool:

        if s is None or t is None: return None

        if len(s) != len(t): return False

        c_dict = collections.Counter(s)
        for tt in t:
            c_dict[tt] -= 1
            if c_dict[tt] < 0:
                return False

        return True

