'''
342. Power of Four
Easy

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''


class Solution:


# # Time O(1) Space O(1), runtime = 64 ms
#     def isPowerOfFour(self, num: int) -> bool:

#         if not num or num < 1: return False

#         #         1               1
#         #         4             100
#         #         16          10000
#         #         64        1000000

#         b = bin(num)[2:]
#         return len(b)%2 and b.count('1') == 1


'''
    # Time O(1) Space O(1), runtime = 48 ms
    def isPowerOfFour(self, num: int) -> bool:

#         1               1
#         4             100
#         16          10000
#         64        1000000
#                   1010101

#         num & (1010101) == 0

        if not num or num < 1: return False

        return num & (num-1) == 0 and num & 0b10101010101010101010101010101010 == 0
'''

'''   
    # Time O(1) Space O(1), runtime = 44 ms
    def isPowerOfFour(self, num: int) -> bool:

        if not num or num < 1: return False

        return num & (num-1) == 0 and num % 3 == 1  
'''

'''
    # Time O(1) Space O(1), runtime = 48 ms
    def isPowerOfFour(self, num: int) -> bool:

#         1               1
#         4             100
#         16          10000
#         64        1000000
#                   1010101

#         num & (1010101) == 0

        if not num or num < 1: return False

        return num & (num-1) == 0 and num & 0xaaaaaaaa == 0
'''

'''
    # Time O(1) Space O(1), 28 ms
    def isPowerOfFour(self, num: int) -> bool:

    # 4^0 = 1
    # 4^1 = 4
    # 4^2 = 16
    # 4^3 = 64
    # 4^4 = 256
    # log4(Num) --> an integer

        if not num or num < 1: return False
        return math.log(num, 4).is_integer()
'''

'''       
    def isPowerOfTwo(self, n: int) -> bool:

        if not n or n < 1: return False
        if n == 1: return True

        return n & (n-1) == 0
'''

'''
    def isPowerOfTwo(self, n: int) -> bool:

        if not n or n < 1: return False
        if n == 1: return True

        return n == n & (-n)
'''