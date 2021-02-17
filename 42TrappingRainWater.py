'''
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks
Marcos for contributing this image!

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

    # Use l, r pointers
    # Time O(N) Space O(1)
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        size = len(height)
        l = 0
        r = size - 1
        total = 0
        left_max = 0
        right_max = 0
        while l < r:

            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    total += left_max - height[l]
                l += 1

            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    total += right_max - height[r]
                r -= 1

        return total



    # Time O(N) Space O(N)
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        size = len(height)
        left = [0] * size
        right = [0] * size
        total = 0
        left[0] = height[0]
        right[size - 1] = height[size - 1]

        for i in range(1, size):
            left[i] = max(left[i - 1], height[i])

        for j in range(size - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])

        for i in range(size):
            total += max(0, min(left[i], right[i]) - height[i])

        return total



    # Brute Force
    # Time O(N^2) Space O(1)
    def trap(self, height: List[int]) -> int:

        total, left_max, right_max = 0, 0, 0
        for i in range(len(height)):

            left_max = 0 if i == 0 else max(height[:i])
            right_max = 0 if i == len(height) - 1 else max(height[i+1:])
            total += max(0, min(left_max, right_max) - height[i])

        return total

