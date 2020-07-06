'''
461. Hamming Distance
Easy

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note: 0 ≤ x, y < 231.
Example:
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''


class Solution:

    # Time O(1) Space O(1), time = 40 ms
    def hammingDistance(self, x: int, y: int) -> int:

        if x == None or y == None: return 0

        value = x ^ y
        count = 0
        while value != 0:
            count += 1
            value = value & (value - 1)

        return count


'''
    # Time O(1) Space O(1), time = 64 ms
    def hammingDistance(self, x: int, y: int) -> int:

        if x == None or y == None: return 0

        value = x^y
        count = 0
        while value != 0:
            if value & 1 == 1:
                count += 1
            value = value >> 1

        return count
'''

'''
    # Time O(1) Space O(1), time = 56 ms
    def hammingDistance(self, x: int, y: int) -> int:

        if x == None or y == None: return 0
        return bin(x^y).count('1')
'''

'''
    # Time O(1) Space O(1), time = 32 ms
    def hammingDistance(self, x: int, y: int) -> int:

        if x == None or y == None: return 0

        value = x^y
        count = 0
        while value != 0:
            if value % 2 == 1:
                count += 1
            value = value >> 1

        return count
'''

'''
    # Time O(1) Space O(1), time = 52 ms
    def hammingDistance(self, x: int, y: int) -> int:

        if x == None or y == None: return 0

        value = x^y
        count = 0
        while value != 0:
            value, rest = divmod(value,2)
            if rest == 1:
                count += 1

        return count
'''

'''
    # Time O(1) Space O(1), time = 68 ms
    def hammingDistance(self, x: int, y: int) -> int:

#         XOR = ^
#         either a or b, but not both

#         x = 1 = 0 0 0 1 = bin(x)[2:]
#         y = 4 = 0 1 0 0 = bin(x)[2:]
#         x ^ y = 0 1 0 1 --------> count no. of 1's

        if x == None or y == None: return 0

        value = bin(x^y)[2:]
        count = 0
        for v in value:
            if v == '1':
                count += 1

        return count
'''
