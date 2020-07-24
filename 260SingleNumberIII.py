'''
260. Single Number III
Medium

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:
	1.	The order of the result is not important. So in the above example, [5, 3] is also correct.
	2.	Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

'''


class Solution:


# a XOR 0 = a
# XOR if one, but not both
# a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# a XOR a = 0
# a XOR b XOR a XOR c = 0 XOR b XOR c = b XOR c
# x & (-x) to isolate the rightmost 1-bit.
# x & (-x) keep the rightmost 1-bit and to set all the other bits to 0
# Brain Kernighan's algorithm a & (a-1), turn off the rightmost 1-bit


'''
    # Time O(N) Space O(1), runtime = 60 ms
    def singleNumber(self, nums: List[int]) -> List[int]:

        if not nums: return []

        a_xor_b = 0
        for num in nums:
            a_xor_b ^= num

        rightmost_1_bit = a_xor_b & (- a_xor_b)

        a = 0
        for num in nums:
            if num & rightmost_1_bit:
                a ^= num
        return [a, a_xor_b ^ a]
'''

'''
    # Time O(N) Space O(N), runtime = 56 ms
    def singleNumber(self, nums: List[int]) -> List[int]:

        num_dict = collections.Counter(nums)

        return [k for k,v in num_dict.items() if v == 1]

'''

