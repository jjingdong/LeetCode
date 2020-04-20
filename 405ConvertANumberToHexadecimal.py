# 405. Convert a Number to Hexadecimal
# Easy
#
# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
# Note:
# 	1.	All letters in hexadecimal (a-f) must be in lowercase.
# 	2.	The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# 	3.	The given number is guaranteed to fit within the range of a 32-bit signed integer.
# 	4.	You must not use any method provided by the library which converts/formats the number to hex directly.
#
# Example 1:
# Input:
# 26
#
# Output:
# "1a"
# 
# Example 2:
# Input:
# -1
#
# Output:
# "ffffffff"



class Solution:

    # E.g.
    # 26 => '1f'
    # num/16 = 26/16 = 1
    # num%16 = 26%16 = 10 -> a

    # 254 => 'fe'
    # num/16 = 254/16 = 15 -> f
    # num%16 = 254%16 = 14 -> e

    # 1 => '1'
    # -1 => 'fffffffff'
    # Two's complement notation to represent negative numbers.
    # -1 => - 1
    # => - 00000001
    # =>  15 15 15 15 15 15 15 15
    # =>  15 15 15 15 15 15 15 15 => 16 ^ (8+1) -1

    # They are using two's complement notation to represent negative numbers. To get it, you start with your value, express it in binary, change all the 0's to 1's and vice versa, then add 1. You can do it directly in hex, subtracting each digit from 15, then adding 1.

    # Time O(logN)
    # Space O(logN)
    def toHex(self, num: int) -> str:

        def positiveHex(pos):

            digits = "0123456789abcdef"

            if pos < 16:
                return digits[num % 16]

            return self.toHex(pos // 16) + self.toHex(pos % 16)

        if num >= 0:
            return positiveHex(num)
        else:
            return positiveHex(2 ** 32 + num)



