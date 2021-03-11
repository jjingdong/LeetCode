'''
246. Strobogrammatic Number
Easy

Given a string num which represents an integer, return true if num is a
strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true


Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
'''


class Solution:

    #   609 -> 906 -> 609

    # Time O(N) Space O(N)
    def isStrobogrammatic(self, num: str) -> bool:

        n_dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        result = ''
        reversed = num[::-1]
        for n in reversed:
            if n in n_dict:
                n = n_dict[n]
                result += n
            else:
                return False

        return result == num

