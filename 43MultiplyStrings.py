'''
43. Multiply Strings
Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
Note:
	1.	The length of both num1 and num2 is < 110.
	2.	Both num1 and num2 contain only digits 0-9.
	3.	Both num1 and num2 do not contain any leading zero, except the number 0 itself.
	4.	You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:

    # '123' * '456'
    #   1   2   3
    #   4   5   6
    # * ------------
    #       1   8
    #   1   2
    #   6
    #  ------------
    # '123' * '456' = 123 * 6 + 123 * 50 + 123 * 400
    #               = 3 * 6 + 20 * 6 + 100 * 6 + .........

    # Time O(N^2) Space O(N)
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == '0' or num2 == '0': return '0'

        int_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        sum = 0
        for i in range(len(num1) - 1, -1, -1):

            a = int_dict[num1[i]]
            for j in range(len(num2) - 1, -1, -1):
                b = int_dict[num2[j]]
                aa = a * (10 ** (len(num1) - i - 1))
                bb = b * (10 ** (len(num2) - j - 1))
                sum += aa * bb

        return str(sum)



