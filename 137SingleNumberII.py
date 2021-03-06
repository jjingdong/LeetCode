'''
137. Single Number II
Medium

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,3,2]
Output: 3
Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
'''


class Solution:

    # 1. dict time O(N) space O(N)
    # 2. sort time O(NlogN) space O(1)
    # 3. a+a+a+b+b+b+c+c = 3a+3b+2c, use set. Time O(N) Space O(N)
    # 4. bitwise a XOR a = 0, 0 XOR a = a

    # Time O(N) Space O(1)
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = 0
        seen_twice = 0
        for num in nums:
            seen_once = seen_once ^ num & ~seen_twice
            seen_twice = seen_twice ^ num & ~seen_once
            print(f'num = {num} seen_once = {seen_once} seen_twice = {seen_twice}')

        return seen_once

    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2