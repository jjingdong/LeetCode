'''
560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
Example 1: 
Input:nums = [1,1,1], k = 2
Output: 2

Note: 
	1.	The length of the array is in range [1, 20,000].
	2.	The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''


class Solution:


# Solution I: Brute Force --- Time limit exceeded
#
# Solution II: HashMap ---> Didn't implement


'''
    # Time O(N^2) Space O(1), using Brute Force
    def subarraySum(self, nums: List[int], k: int) -> int:

        if nums is None: return None

        result = 0
        for start in range(len(nums)):
            count = 0
            i = start
            while i <= len(nums) - 1:
                count += nums[i]
                if count == k:
                    result += 1
                i += 1

        return result
'''






