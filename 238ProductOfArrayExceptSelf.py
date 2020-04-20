# 238. Product of Array Except Self
# Medium
#
# Given an array nums of n integers where n > 1,
# return an array output such that output[i] is equal
# to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity?
# (The output array does not count as extra space for
# the purpose of space complexity analysis.)

class Solution:

    # [4, 5, 1, 8, 2]
    # Left multiply results:
    # [1, 4, 20, 20, 160]
    # right multiply results:
    # [80, 16, 16, 2, 1]
    # multiply all the left and right:
    # [80, 64, 320, 40, 160]

    # Time O(N)
    # Space O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        results = left = [1] * length

        left = [1] * length
        right = [1] * length

        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(length):
            results[i] = left[i] * right[i]

        return results

    # Time O(N)
    # Space O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        results = left = [1] * length

        for i in range(1, length):
            results[i] = results[i - 1] * nums[i - 1]

        right = 1
        for i in range(length - 2, -1, -1):
            right = right * nums[i + 1]
            results[i] = results[i] * right

        return results