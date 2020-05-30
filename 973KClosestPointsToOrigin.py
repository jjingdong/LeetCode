'''
973. K Closest Points to Origin
Medium

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
 
Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 
Note:
	1.	1 <= K <= points.length <= 10000
	2.	-10000 < points[i][0] < 10000
	3.	-10000 < points[i][1] < 10000
'''


class Solution:

    # Time O(NlogK) Space O(N), runtime = 660 ms
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, lambda p: p[0] * p[0] + p[1] * p[1])


'''
    # Time O(NlogN), Space O(N), runtime = 636 ms
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda p: p[0] * p[0] + p[1] * p[1])
        return points[:K]
'''

'''   
    # Time O(NlogK) Space O(N), runtime = 716 ms
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        d_dict = collections.Counter()
        for [p0, p1] in points:
            d_dict[(p0, p1)] = p0 * p0 + p1 * p1

        return heapq.nsmallest(K, d_dict, key = d_dict.get)
'''