'''
42. Trapping Rain Water
Hard

6260

110

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution:

    # minimum of maximum height of bars on both the sides minus its own height
    # ans = min(left_max, right_max) - height[i]
    # left_max = max(left_max, height[j])
    # right_max = max(right_max, height[j])
    # ans = max(0, min(left_max, right_max) - height[i])
    #
    # Solution I: Brute Force
    #
    # Solution II: Using cache
    #
    # Solution III: Using 2 pointers
    # Note. didn't implement this

    # Time O(N) Space O(N), using Cache
    def trap(self, height: List[int]) -> int:

        size = len(height)
        left = [0] * size
        right = [0] * size
        total = 0

        for i in range(1, size):
            right[i] = max(right[i - 1], height[i])

        for j in range(size - 2, -1, -1):
            left[j] = max(left[j + 1], height[j])

        for i in range(size):
            total += max(0, min(left[i], right[i]) - height[i])

        return total


'''
    # Time O(N^2) Space O(1), Using Brute Force
    def trap(self, height: List[int]) -> int:

        total, left_max, right_max = 0, 0, 0
        for i in range(len(height)):

            left_max = 0 if i == 0 else max(height[:i])
            right_max = 0 if i == len(height) - 1 else max(height[i+1:])
            total += max(0, min(left_max, right_max) - height[i])

        return total
'''
