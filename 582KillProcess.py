'''
582. Kill Process
Medium

Given n processes, each process has a unique PID (process id) and its PPID (parent
process id).

Each process only has one parent process, but may have one or more children processes.
 This is just like a tree structure. Only one process has PPID that is 0, which means
 this process has no parent process. All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes, where the first list
 contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a
list of PIDs of processes that will be killed in the end. You should assume that when
a process is killed, all its children processes will be killed. No order is required
for the final answer.

Example 1:
Input:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation:
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
Note:
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.
'''


class Solution:

    #         pid =  [1, 3, 10, 5]
    #         ppid = [3, 0, 5, 3]
    #         kill = 5

    #             3
    #           /   \
    #         1     5
    #               \
    #                 10

    # dict + BFS
    # Time O(N) Space O(N)
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        if not pid or not ppid or kill is None: return None
        if len(pid) != len(ppid): return None

        id_dict = collections.defaultdict(list)
        size = len(pid)
        for i in range(size):
            id_dict[ppid[i]].append(pid[i])

        result = [kill]
        queue = collections.deque([])
        queue.append(kill)
        while queue:
            cur = queue.popleft()
            if cur in id_dict:
                children = id_dict[cur]
                result.extend(children)
                queue.extend(children)

        return result

