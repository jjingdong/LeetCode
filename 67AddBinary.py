'''
67. Add Binary
Easy

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
	•	Each string consists only of '0' or '1' characters.
	•	1 <= a.length, b.length <= 10^4
	•	Each string is either "0" or doesn't contain any leading zero.
'''


class Solution:

    # Time O(M+N) Space O(1), runtime = 32 ms
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b: return ''

        ans = int(a, 2) + int(b, 2)

        return bin(ans)[2:]
