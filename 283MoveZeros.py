# 283. Move Zeroes
# Easy
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the ' \
#                                                    'relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
# 	1.	You must do this in-place without making a copy of the array.
# 	2.	Minimize the total number of operations.

class Solution:

    # [0, 1, 0, 3, 12]
    #  i. j    -> swap
    # [1, 0, 0, 3, 12]
    #     i     j. -> swap
    # [1, 3, 0, 0, 12]
    #        i.     j.  -> swap
    # [1, 3, 12, 0, 0]
    #            i. j.

    # Time: O(N) Space O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if nums is None: return None
        if nums == []: return []
        if len(nums) == 1: return nums

        i = 0
        j = i + 1
        size = len(nums)
        while i < size and j < size:
            # print(str('i = ') + str(i))
            # print(str('j = ') + str(j))
            if nums[i] != 0:
                i += 1
                j = i + 1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j = i + 1
            elif nums[i] == 0 and nums[j] == 0:
                j += 1

    '''
    # [0, 1, 0, 3, 12]
    #  i. j           -> put j value to i position
    # [1, 0, 0, 3, 12]
    #     i     j     -> put j value to i position
    # [1, 3, 0, 0, 12]
    #        i      j -> put j value to i position
    # [1, 3, 12, 0, 0]
    #            i  
    #Time O(N) Space O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != 0:
                i += 1
                j = i + 1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
                j = i + 1
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
    '''