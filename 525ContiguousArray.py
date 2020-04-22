'''
525. Contiguous Array
Medium

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
Example 1: 
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2: 
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
'''


class Solution:

    # Brute Force:
    #                 00001011100
    #              /               \
    #      0000101110             0001011100
    #     /         \           /         \
    # 000010111  000101110  000101110  001011100
    #
    # Solution II:
    #      [0,0,0,0,1,0,1,1,1,0,0]
    # 0 = -1
    # 1 = 1
    #         [ 0,  0,  0,  0,  1,  0,  1,  1,  1,  0,  0]
    # index =   0   1   2.  3.  4.  5.  6.  7.  8.  9. 10
    # count = [-1, -2, -3, -4, -3, -4, -3, -2, -1, -2, -3] -------> calculate on the fly
    # HashMap = {-1: , -2: , -3: , -4: } ---> just save the min value
    #    min max
    # -1: 0, 8             len = 8 ------> calculate on the fly
    # -2: 1, 7, 9          len = 8
    # -3: 2, 4, 6, 10      len = 8
    # -4: 3, 5             len = 2

    # Time O(N) Space O(N)
    def findMaxLength(self, nums: List[int]) -> int:

        count = 0
        countMap = {}
        maxLen = 0
        countMap[0] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                count += -1
            else:
                count += 1

            if count in countMap:
                maxLen = max(maxLen, i - countMap[count])
            else:
                countMap[count] = i

        return maxLen




