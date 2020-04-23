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

    # Coding is not done, need to debug

    # Time O(N) Space O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:

        if nums is None: return None
        if nums == []: return 0

        i = 0
        j = 0
        sum = 0
        count = 0
        while i <= j and j < len(nums):

            sum += nums[j]
            print('------------------')
            print(str(i) + " " + str(j))
            print(sum)
            if sum == k:
                count += 1
                if i == j:
                    i += 1
                    j += 1
                    sum = 0
                elif i < j:
                    i += 1
                    sum = sum - nums[i] - nums[j]
            elif sum < k:
                j += 1
            else:
                if i == j:
                    i += 1
                    j += 1
                    sum = 0
                elif i < j:
                    i += 1
                    sum = sum - nums[i] - nums[j]

        return count

