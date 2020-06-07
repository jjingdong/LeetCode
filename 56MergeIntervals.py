'''
56. Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.
Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''


class Solution:

    # Time O(NlogN) Space O(N), runtime = 76 ms
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals: return intervals

        intervals = sorted(intervals, key=lambda x: x[0])

        i, j = 0, 0
        results = []
        pre_i, pre_j = intervals[0][0], intervals[0][1]
        for [cur_i, cur_j] in intervals:
            if pre_j < cur_i:
                results.append([pre_i, pre_j])
                pre_i = cur_i
                pre_j = cur_j
            else:
                pre_j = max(cur_j, pre_j)

        results.append([pre_i, pre_j])
        return results

