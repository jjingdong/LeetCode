'''
75. Sort Colors
Medium

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:
	•	A rather straight forward solution is a two-pass algorithm using counting sort. First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
	•	Could you come up with a one-pass algorithm using only constant space?

'''


class Solution:

    # Solution I: Dutch National Flag Problem
    #          p0             p2
    #          |              |
    #    0, 0 [2, 0, 2, 1, 1, 0] 2, 2
    #          |
    #          i

    # Time O(N) Space O(1), runtime = 20 ms
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        # p0 is the rightmost boundary of 0s, p2 is the leftmost boundary of 2s
        p0, p2 = 0, len(nums) - 1
        index = 0
        while index <= p2:
            cur = nums[index]
            if cur == 0:
                swap(index, p0)
                index += 1
                p0 += 1
            elif cur == 1:
                index += 1
            else:
                swap(index, p2)
                p2 -= 1

