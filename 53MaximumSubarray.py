# 53. Maximum Subarray
# Easy
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution
# using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Time O(N)
        # Space O(N)
        curMaxSum = nums[:]
        globalMaxSum = nums[:]
        startIndex, endIndex = 0, 0
        maxValue = nums[0]

        for i in range(1, len(nums)):

            if nums[i] > curMaxSum[i - 1] + nums[i]:
                startIndex = i

            curMaxSum[i] = max(nums[i], curMaxSum[i - 1] + nums[i])
            if curMaxSum[i] > maxValue:
                maxValue = curMaxSum[i]
                endIndex = i

            globalMaxSum[i] = max(globalMaxSum[i - 1], curMaxSum[i])

            # print(curMaxSum)
            # print(globalMaxSum)
            # print("maxValue = " + str(maxValue))
            # print("start = " + str(startIndex))
            # print("end = " + str(endIndex))

        return globalMaxSum[len(nums) - 1]

    # Better solution will be
    # Time O(N)
    # Space O(1)

