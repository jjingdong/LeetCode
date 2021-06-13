'''
392. Is Subsequence

Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
Follow up: If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
Credits: Special thanks to @pbrother for adding this problem and creating all test cases.
 
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:
	•	0 <= s.length <= 100
	•	0 <= t.length <= 10^4
	•	Both strings consists only of lowercase characters.

'''


class Solution:

    # Solution I, My own solution is simple and clear
    #         s = "abc",
    #              | |
    #         t = "ahbgdc"
    #              |    |
    #         s = "b",
    #              |
    #         t = "hbgd"
    #              |  |
    #
    # Solution II
    #

    # Time O(T) Space O(1), runtime = 48 ms
    def isSubsequence(self, s: str, t: str) -> bool:

        size_s, size_t = len(s), len(t)
        ss, tt = 0, 0
        while ss < size_s and tt < size_t:
            if s[ss] == t[tt]:
                ss += 1
            tt += 1

        return ss == size_s

    def isSubsequence(self, s: str, t: str) -> bool:

        for char in s:
            if char not in iter(t):
                return False
        return True


'''
    # Time O(T) Space O(1), runtime = 36 ms
    def isSubsequence(self, s: str, t: str) -> bool:

        def find(ss, tt):    
            if ss == '':
                return True
            if tt == '':
                return False
            if len(ss) > len(tt):
                return False
            if len(ss) == 1:
                return ss in tt
            if len(ss) == len(tt):
                return ss == tt

            one, two = None, None
            for i in range(len(tt)):
                if tt[i] == ss[0]:
                    one = i
                    break       
            for j in range(len(tt)-1, -1, -1):
                if tt[j] == ss[-1]:
                    two = j
                    break

            if one != None and two != None and one < two:
                return find(ss[1:-1], tt[one+1:two])
            else:
                return False

        return find(s,t)
'''
