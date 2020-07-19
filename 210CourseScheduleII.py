'''
210. Course Schedule II
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
Example 1:
Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:
	1.	The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
	2.	You may assume that there are no duplicate edges in the input prerequisites.
'''


class Solution:

    #            pre
    #         [0,1]
    #
    #         [[1,0],[2,0],[3,1],[3,2]]
    #         0 -> 1 -> 3
    #           -> 2 -> 3
    #
    #         Topological Sort
    #         pre_dict = {0: [1,2], 1 : [3], 2 : 3}
    #         course_dict = {1 : [0], 2: [0], 3 : [1,2]}

    # Time O(V+E) Space O(V+E), runtime = 104ms
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        pre_dict = collections.defaultdict(list)
        course_dict = collections.defaultdict(list)
        for [course, pre] in prerequisites:
            pre_dict[pre].append(course)
            course_dict[course].append(pre)

        todo = collections.deque([])
        results = []
        for i in range(numCourses):
            if i not in course_dict:
                todo.append(i)

        while todo:
            c1 = todo.popleft()
            results.append(c1)

            if c1 in pre_dict:
                for c2 in pre_dict[c1]:
                    course_dict[c2].remove(c1)
                    if course_dict[c2] == []:
                        todo.append(c2)

        if len(results) < len(course_dict):
            return []

        return results
