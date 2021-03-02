'''
206. Reverse Linked List
Easy

Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Recursion
    # Time O(N) Space O(N), runtime = 44 ms
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node):
            if not node or not node.next: return node

            p = reverse(node.next)
            node.next.next = node
            node.next = None
            return p

        return reverse(head)

    # Recursion
    # Time O(N) Space O(N), runtime = 44 ms
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        if not node or not node.next: return node

        p = self.reverseList(node.next)
        node.next.next = node
        node.next = None

        return p


    # iterative
    # Time O(N) Space O(1), runtime = 32 ms
    def reverseList(self, head: ListNode) -> ListNode:

        node = head
        pre = None
        while node:
            next_node = node.next
            node.next = pre
            pre = node
            node = next_node
        return pre


