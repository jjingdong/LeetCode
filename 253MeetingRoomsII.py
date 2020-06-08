'''
253. Meeting Rooms II
Medium

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:
Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''


class Solution:

    # Solution I:  Time Limit Exceeded
    #         [[0, 30],[5, 10],[15, 20]]

    #         0 5 10 15 20 30
    #         [0,5][5,10][10,15][15,20][20,30]
    #  [0,30]   1     1     1      1      1
    #  [5,10]         1
    # [15,20]                      1
    #
    # Solution II: Heap
    #
    # Solution III: Chronological Ordering

    # Time O(NlogN) Space O(N), runtime = 100 ms
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals: return 0

        start, end = [], []
        for [a, b] in intervals:
            start.append(a)
            end.append(b)
        start = sorted(start)
        end = sorted(end)

        start_i, end_i = 0, 0
        count = 0
        while start_i < len(intervals):
            if start[start_i] < end[end_i]:
                start_i += 1
                count += 1
            else:
                start_i += 1
                end_i += 1

        return count


'''
    # Time O(NlogN) Space O(N), runtime = 96 ms
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals: return 0

        results = []
        intervals = sorted(intervals, key = lambda x: x[0])

        heapq.heappush(results, intervals[0][1])
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            top = results[0]
            if start >= top:
                heapq.heappop(results)
                heapq.heappush(results, end)
            else:
                heapq.heappush(results, end)

        return len(results)
'''

'''
    # Time O(N^2) Space O(2N), time limit exceeded
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals: return 0

        nums = set([])
        ranges = []
        max_count = 0
        for [a, b] in intervals:
            nums.add(a)
            nums.add(b)
        nums = sorted(nums)

        pre = 0
        for n in nums:
            ranges.append([pre, n])
            pre = n

        counts = [0] * len(ranges)
        for [lo,hi] in intervals:
            for i in range(len(ranges)):
                [r1,r2] = ranges[i]
                if r1 >=lo and r2 <= hi:
                    counts[i] += 1
                    max_count = max(max_count, counts[i])

        return max_count
'''

