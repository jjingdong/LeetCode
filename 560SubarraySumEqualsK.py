'''
560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total
 number of continuous subarrays whose sum equals to k.
Example 1: 
Input:nums = [1,1,1], k = 2
Output: 2

Note: 
	1.	The length of the array is in range [1, 20,000].
	2.	The range of numbers in the array is [-1000, 1000] and the range
	of the integer k is [-1e7, 1e7].
'''


class Solution:

    # Solution I: Cumulated Sum --- Time Limit exceeded
    # sum[i:j] = accumulated_sum[j] - accumulated_sum[i-1]
    #
    # Solution II: HashMap

    # Time O(N) Space O(N), runtime = 140 ms
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum_count_dict = {0: 1}
        s, count = 0, 0
        for n in nums:
            s += n
            if s - k in sum_count_dict:
                count += sum_count_dict[s - k]
            if s in sum_count_dict:
                sum_count_dict[s] += 1
            else:
                sum_count_dict[s] = 1
        return count


'''
    # Time O(N^2) Space O(N), TLE
    def subarraySum(self, nums: List[int], k: int) -> int:

        result = 0
        value = 0
        sums = nums[:]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]

        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == 0:
                    count = sums[j]
                else:
                    count = sums[j] - sums[i-1]
                if count == k:
                    result += 1

        return result
'''

'''
    # Time O(N^2) Space O(1), TLE
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

