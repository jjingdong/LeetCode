'''
141. Linked List Cycle
Easy

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos
 which represents the position (0-indexed) in the linked list where
 the tail connects to. If pos == -1, then there is no cycle in the
 linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects
to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects
to the first node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    #         3 -> 2 -> 0 -> 4 ->
    #         ||
    #         fast and slow pointer
    #
    #           1

    # Time O(N) Space O(1), runtime = 44 ms
    def hasCycle(self, head: ListNode) -> bool:

        if not head: return False

        s = head
        f = head.next
        while f and f.next:

            if s == f:
                return True

            s = s.next
            f = f.next.next

        return False
