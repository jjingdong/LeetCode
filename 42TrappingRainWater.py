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

