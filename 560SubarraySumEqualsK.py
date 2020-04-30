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

    # Solution I:
    # Time O(N^2) Space O(N)
    # nums[i:j] = sum[j+1] - sum[i]
    #
    # Solution II:
    #
    # Not done? Can I use sliding window????

    # Time O(N) Space O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:

        if nums is None: return None
        if nums == []: return 0

        i, sum, count = 0, 0, 0

        for j in range(len(nums)):
            print('----------------------')
            print('step 0')
            print('i = ' + str(i) + ' j = ' + str(j) + ' sum = ' + str(sum))

            sum += nums[j]
            print('step 0')
            print('i = ' + str(i) + ' j = ' + str(j) + ' sum = ' + str(sum))

            if sum == k:
                count += 1

                sum = sum - nums[i] - nums[j]
                i += 1
                print('step 1')
                print('i = ' + str(i) + ' j = ' + str(j) + ' sum = ' + str(sum))

            while sum > k:
                sum = sum - nums[i]
                i += 1
                print('step 2')
                print('i = ' + str(i) + ' j = ' + str(j) + ' sum = ' + str(sum))

        return count



