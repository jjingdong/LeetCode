'''
234. Palindrome Linked List
Easy

Given a singly linked list, determine if it is a palindrome.
Example 1:
Input: 1->2
Output: false
Example 2:
Input: 1->2->2->1
Output: true
Follow up: Could you do it in O(n) time and O(1) space?

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 1->2->2->1
    #    |  |
    #    i  j
    #       |     |
    #       i     j
    #
    # 1->2->3->2->1
    #    |  |
    #    i  j
    #       |     |
    #       i     j
    #          |     |
    #          i     j

    # Time O(n) Space O(1)
    def isPalindrome(self, head: ListNode) -> bool:

        def reverse(node):
            pre = None
            node = node_i
            while node:
                next_node = node.next
                node.next = pre
                pre = node
                node = next_node
            return pre

        if not head: return True

        node = head
        node_i = node
        node_j = node
        while node_j.next and node_j.next.next:
            node_i = node_i.next
            node_j = node_j.next.next

        # reverse
        node_2 = reverse(node_i)

        # compare node and and node_2
        while node and node_2:
            if node.val != node_2.val:
                return False
            node = node.next
            node_2 = node_2.next

        return True