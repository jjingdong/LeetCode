'''
1552. Magnetic Force Between Two Balls
Medium

163

23

Add to List

Share
In universe Earth C-137, Rick discovered a special form of magnetic force
between two balls if they are put in his new invented basket. Rick has n
empty baskets, the ith basket is at position[i], Morty has m balls and needs
to distribute the balls into the baskets such that the minimum magnetic
force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions
x and y is |x - y|.

Given the integer array position and the integer m. Return the required
force.



Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the
magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is
3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.


Constraints:

n == position.length
2 <= n <= 10^5
1 <= position[i] <= 10^9
All integers in position are distinct.
2 <= m <= position.length
'''


class Solution:

    #         1 2 3 4 5 6 7
    #         | | | |     |
    #         b     b     b
    #         forces: 3, 3, 6
    #         results = 3

    #         1 2 3 4 5 ...... 100000000  m = 2
    #         | | | | |            |
    #         b                    b
    #         result = 100000000 - 1

    #         1 2 3 4 5 ...... 100    m = 3
    #         | | | | |         |
    #         b                 b
    #               mid =  50
    # distance = 0 1 2 3 4 99
    #
    #                mid = 25
    # distance = 0 1 2 3 4 99
    #                mid = 11
    # distance = 0 1 2 3 4 99
    #                mid = 5
    # distance = 0 1 2 3 4 99
    #                mid = 4
    # distance = 0 1 2 3 4 99

    #         1 2 3 4 5 ...... 100    m = 4
    #         | | | | |         |
    #         b                 b
    #               mid =  50
    # distance = 0 1 2 3 4 99
    #
    #                mid = 25
    # distance = 0 1 2 3 4 99
    #                mid = 12
    # distance = 0 1 2 3 4 99
    #                mid = 6
    # distance = 0 1 2 3 4 99
    #                mid = 3
    # distance = 1 2 3 1 96
    # mid = 1
    # mid = 2

    # Time O(N) Space O(1), runtime = 1644 ms
    def maxDistance(self, position: List[int], m: int) -> int:

        def find_distance(mid_pos):

            count = 1
            pre = position[0]
            for i in range(1, len(position)):
                distance = position[i] - pre
                if distance >= mid_pos:
                    count += 1
                    pre = position[i]
            return count

        position = sorted(position)
        lo = 0
        hi = position[-1]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if find_distance(mid) >= m:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi

