'''
252. Meeting Rooms
Easy

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: [[7,10],[2,4]]
# Output: true
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''
class Solution:

    # Time: O(NlogN)
    # Space: O(1)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if intervals is None: return False
        if intervals == []: return True
        if len(intervals) == 1: return True

        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        finish = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            if start < finish:
                return False

            finish = intervals[i][1]

        return True




