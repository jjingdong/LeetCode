'''
11. Container With Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
 

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
 
Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''


class Solution:

    #                               [1,8,6,2,5,4,8,3,7]
    #                     /                                     \
    #           [1,8,6,2,5,4,8,3]                     [8,6,2,5,4,8,3,7]
    #           /                   \                   /               \
    # [1,8,6,2,5,4,8] [8,6,2,5,4,8,3,7]     [8,6,2,5,4,8,3] [6,2,5,4,8,3,7]
    #
    #       [1,8,6,2,5,4,8,3,7]
    #   1   [0,1,1,1,1,1,1,1,1]
    #   8   [1,0,6,2,5,4,0,3,7]
    #   6   [1,6,0,2,5,4,6,3,6]
    #   2
    #   5
    #   4
    #   8
    #   3
    #   7
    #
    #   [1,8,6,2,5,4,8,3,7]
    #

    # Time O(N) Space O(1)
    def maxArea(self, height: List[int]) -> int:

        if not height: return 0

        max_value = 0
        i, j = 0, len(height) - 1
        value = 0
        while i < j:
            if height[i] > height[j]:
                value = height[j] * (j - i)
                j -= 1
            else:
                value = height[i] * (j - i)
                i += 1

            max_value = max(max_value, value)

        return max_value


'''    
    # Time O(N^2) Space O(N^2) ----- Time Limit Exceeded
    def maxArea(self, height: List[int]) -> int:

        if not height: return 0

        size = len(height)
        dp = [[0 for _ in range(size)] for _ in range(size)]  
        max_value = 0
        for i in range(size):
            for j in range(size):
                if i > j:
                    dp[i][j] = min(height[i],height[j]) * abs(i-j)
                    max_value = max(max_value, dp[i][j])

        return max_value
'''