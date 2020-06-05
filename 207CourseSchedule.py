'''
207. Course Schedule
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
 
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 
Constraints:
	•	The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
	•	You may assume that there are no duplicate edges in the input prerequisites.
	•	1 <= numCourses <= 10^5

'''


class Solution:

    # Graph
    #
    # Solution I: DFS
    #
    # Solution II: Topological Sort

    # Time O(E+V) Space O(E+V), runtime = 212 ms
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites: return True

        pre_course_dict = collections.defaultdict(list)
        cc_dict = collections.defaultdict(list)
        for c, p in prerequisites:
            pre_course_dict[p].append(c)
            cc_dict[c].append(p)

        result = []
        in_progress = collections.deque([])
        # find the node donnot have pre requests
        vs = []
        for v in pre_course_dict.values():
            vs += v
        for k in pre_course_dict.keys():
            if k not in vs:
                in_progress.append(k)

        while in_progress:
            pre = in_progress.popleft()
            result.append(pre)
            for course in pre_course_dict[pre]:
                cc_dict[course].remove(pre)
                if not cc_dict[course]:
                    in_progress.append(course)

        return len(result) == len(pre_course_dict)


'''
    # Time O() Space O()
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        c_dict = collections.defaultdict(list)
        for c, p in prerequisites:
            c_dict[p].append(c)

        # print(c_dict)


        visited = set()
        def traverse(current, path):
            nonlocal result

            # print(path)
            if current in visited:
                return False
            if current in path:
                return False
            if not result:
                return

            visited.add(current)
            path.append(current)

            for edge in c_dict[current]:
                if traverse(edge, path) == False:
                    return False

            path.pop()
            visited.remove(current)

            return result

        result = True
        for i in range(numCourses):
            # print(traverse(i, []))
            if traverse(i, []) == False:
                return False

        return True
'''
