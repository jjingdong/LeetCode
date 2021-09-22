'''
84. Largest Rectangle in Histogram
Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''


class Solution:

    # Time O(N^2)
    #     def largestRectangleArea(self, heights: List[int]) -> int:
    #         area = 0
    #         size = len(heights)
    #         for i in range(size):
    #             min_H = float('inf')
    #             for j in range(i, size):
    #                 min_H = min(min_H, heights[j])
    #                 W = j - i + 1
    #                 area = max(area, min_H * W)

    #         return area

    # Time O(N) Space O(N)
    def largestRectangleArea(self, row):

        row.insert(0, 0)
        row.append(0)
        print(f'row = {row}')
        stack = []
        stack.append(0)

        area = 0
        for i in range(0, len(row)):
            if row[i] > row[stack[-1]]:
                stack.append(i)
            else:
                while row[stack[-1]] > row[i]:
                    H = row[stack[-1]]
                    stack.pop()
                    W = i - stack[-1] - 1
                    area = max(area, H * W)

                stack.append(i)

        return area