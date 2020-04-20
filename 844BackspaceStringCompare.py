'''
844. Backspace String Compare
Easy

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:
	1.	1 <= S.length <= 200
	2.	1 <= T.length <= 200
	3.	S and T only contain lowercase letters and '#' characters.
'''


class Solution:

    # Time O(N) Space O(N)
    def backspaceCompare(self, S: str, T: str) -> bool:

        def getStr(string):

            newStr = ''
            skip = 0
            for c in reversed(string):
                if c == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    newStr += c

            return newStr

        return getStr(S) == getStr(T)


'''
    # Time O(N) Space O(N)
    def backspaceCompare(self, S: str, T: str) -> bool:

        def getStr(string):

            newStr = ''
            for c in string:
                if c == '#':
                    if len(newStr) > 0:
                        newStr = newStr[:-1]
                else:
                    newStr += c

            return newStr

        return getStr(S) == getStr
'''
    def backspaceCompare(self, S: str, T: str) -> bool:

        def getStr(string):
            lst = []
            for c in string:
                if c == '#':
                    if len(lst) > 0:
                        lst.pop()
                else:
                    lst.append(c)

            return ''.join(lst)

        return getStr(S) == getStr(T)
'''


