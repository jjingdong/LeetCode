'''
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Time O(M+N) Space O(1)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        prehead = ListNode(None)
        node = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 if l1 else l2

        return prehead.next