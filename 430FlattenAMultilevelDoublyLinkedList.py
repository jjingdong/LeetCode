'''
430. Flatten a Multilevel Doubly Linked List
Medium

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
 
Example 1:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:
Input: head = []
Output: []
 
How multilevel linked list is represented in test case:
We use the multilevel linked list from Example 1 above:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 
Constraints:
	•	Number of Nodes will not exceed 1000.
	•	1 <= Node.val <= 10^5
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:

    # Solution I: Recursion
    # Solution II: Iteration

    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    #             -> 7 -> 8 -> 9 -> 10
    #                       -> 11 -> 12

    # Time O(N) Space O(N), runtime = 56 ms
    def flatten(self, head: 'Node') -> 'Node':

        def dfs(node, pre_node):

            if not node: return pre_node

            node.prev = pre_node
            pre_node.next = node

            temp_next = node.next
            temp = dfs(node.child, node)
            node.child = None

            return dfs(temp_next, temp)

        if not head: return None
        result_head = pre_node = Node()
        dfs(head, pre_node)
        result_head.next.prev = None
        return result_head.next


'''
        # Time O(N) Space O(N), runtime = 44ms
        def flatten(self, head: 'Node') -> 'Node':

            if not head: return head

            result_head = pre_node = Node()

            stack = []
            stack.append(head)

            while stack:
                curr = stack.pop()

                pre_node.next = curr
                curr.prev = pre_node

                if curr.next:
                    stack.append(curr.next)

                if curr.child:
                    stack.append(curr.child)
                    curr.child = None

                pre_node = curr

            result_head.next.prev = None
            return result_head.next
'''