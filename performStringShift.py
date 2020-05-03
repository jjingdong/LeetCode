'''
Perform String Shifts
Solution
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.



Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
'''


class Solution:

    # Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
    # Output: "efgabcd"

    # Time O(N+K) Space O(1)
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        if shift is None: return None
        if shift == []: return s

        value = 0
        for i in range(len(shift)):
            if shift[i][0] == 0:
                shift[i][0] = -1
            value += shift[i][1] * shift[i][0]

        value = value % len(s)

        print('value = ' + str(value))
        if value == 0:
            return s
        else:
            # also: s[left_shifts:] + s[:left_shifts]
            return s[len(s) - value:len(s)] + s[0:-value]
