'''
1229. Meeting Scheduler
Medium

Given the availability time slots arrays slots1 and slots2 of two people and
a meeting duration duration, return the earliest time slot that works for
both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an
empty array.

The format of a time slot is an array of two elements [start, end] representing
an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect
with each other. That is, for any two time slots [start1, end1] and [start2, end2]
of the same person, either start1 > end2 or start2 > end1.



Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []


Constraints:

1 <= slots1.length, slots2.length <= 104
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 109
1 <= duration <= 106
'''


class Solution:

    #         slots1 = [[10,50],[60,120],[140,210]],
    #         slots2 = [[0,15],[60,70]],
    #         duration = 8
    #         Output: [60,68]

    #         0 10 15 50 60 70 120
    #         |  |  |  |  |  |  |
    #         -------     ----
    #            -------  -------

    #         [[0,15], [10,50],[60,70],[60,120],[140,210]]

    #         0 10 15 50 60 70 120
    #         |  |  |  |  |  |  |
    #         -------
    #            -------
    #                     ----
    #                     -------

    #         [[0,15], [10,50],[60,70],[60,120],[140,210]]
    #           |
    #                           s  e    ss  ee

    #         if ss < e: overlap   [ss, e]
    #         if ss > e: no overlap
    #
    #       common slot: [max(s,ss), min(e,ee)]

    # Time O(MlogM + NlogN) Space O(max(M,N))
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1 = sorted(slots1, key=lambda x: x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])

        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):

            s, e = slots1[i]
            ss, ee = slots2[j]
            l = max(s, ss)
            r = min(e, ee)
            if r - l >= duration:
                return [l, l + duration]

            if e < ee:
                i += 1
            else:
                j += 1

        return []

    # Time O(MlogM + NlogN) Space O(1)
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):

            s, e = slots1[i]
            ss, ee = slots2[j]
            l = max(s, ss)
            r = min(e, ee)
            if r - l >= duration:
                return [l, l + duration]

            if e < ee:
                i += 1
            else:
                j += 1

        return []

    # Time O((M+N)log(M+N)) Space O(M+N)
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slot = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        slot.sort(key=lambda x: (x[0], x[1]))

        heapq.heapify(slot)

        while len(slot) > 1:
            s, e = heapq.heappop(slot)
            ss, ee = slot[0]
            if e - ss >= duration:
                return [ss, ss + duration]

        return []

