'''
435. Non-overlapping Intervals
Medium

Given a collection of intervals, find the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are
non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals
non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're
already non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't
overlap each other.

'''


class Solution:

    #         1   2
    #         1       3
    #             2   3
    #                 3   4

    #         1   2   3   4
    #         -----
    #         --------    ---> remove
    #             -----
    #                 -----

    #         1   2   3   4
    #         ---------
    #             ----           --> remove
    #             ---------    --> remove
    #                 -----

    # Time O(NlogN) Space O(1), runtime = 68 ms
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals: return 0

        intervals = sorted(intervals, key=lambda x: x[0])

        count = 0
        pre_e = intervals[0][0]
        for [s, e] in intervals:

            if s < pre_e:
                count += 1
                pre_e = min(pre_e, e)
            else:
                pre_e = e

        return count
