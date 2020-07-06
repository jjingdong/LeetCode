'''
66. Plus One
Easy

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''


class Solution:

    #          9 9 9
    #        1 0 0 0
    #
    #          9 9 10
    #          9 10 0
    #          10 0 0
    #         1 0 0 0

    # Time O(N) Space O(1), runtime = 20 ms
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            value = digits[i] + carry
            carry, digits[i] = divmod(value, 10)

        if carry == 1:
            return [1] + digits
        else:
            return digits





