'''
476. Number Complement
Easy

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
 
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 
Note:
	1.	The given integer is guaranteed to fit within the range of a 32-bit signed integer.
	2.	You could assume no leading zero bit in the integer’s binary representation.
	3.	This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
'''


class Solution:

    # XOR
    # 0 XOR x = x
    # 1 XOR x = 1 - x -------> flip
    #
    # XOR definition:    (a not b) or (not a and b)
    # bool(a) ^ bool(b)
    #
    # Solution I: flip bit by bit
    # E.g. 5 = 1 0 1
    #          1 0 0
    #          1 1 0
    #          0 1 0
    #
    # Solution II: compute bit length and construct 1 bits bitmask
    # E.g. 5 = 1 0 1
    #     XOR  1 1 1
    #          0 1 0
    #
    # Solution III: built-in functions to construct 1-bits bitmask
    #
    # Solution IV: highestOneBit OpenJDK algorithm from Hacker's delight
    # Note. I don't understand this solution

    # Time O(1) Space O(1)
    def findComplement(self, num: int) -> int:
        # Same as num ^ ((1 << num.bit_length()) - 1)
        return (1 << num.bit_length()) - 1 - num


'''
    # Time O(1) Space O(1)
    def findComplement(self, num: int) -> int:

        bit_length = floor(log2(num)) + 1
        # bitmask = 111
        bitmask = (1 << bit_length) - 1
        return num ^ bitmask
'''

'''
    # Time O(1) Space O(1)
    def findComplement(self, num: int) -> int:

        bit = 1
        todo = num
        while todo != 0:
            num = num ^ bit
            bit = bit << 1
            todo = todo >> 1

        return num
'''

