'''
25. Reverse Nodes in k-Group
Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]


Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz


Follow-up: Can you solve the problem in O(1) extra memory space?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

    #         def reverse_first_k(head,k):
    #             node = head
    #             pre = None
    #             while k>0:
    #                 next_node = node.next
    #                 node.next = pre
    #                 pre = node
    #                 node = next_node
    #                 k -= 1
    #             return pre

    #         final_head = None
    #         counter = 0
    #         tail = None
    #         node = head
    #         while node:

    #             node = node.next
    #             counter += 1
    #             # print(f'counter = {counter} k = {k}')

    #             if 0 == counter % k:

    #                 # reverse the group
    #                 rev_head = reverse_first_k(head,k)
    #                 # print(rev_head)
    #                 # 3,2,1
    #                 #rev_head = 3
    #                 #head = 1
    #                 #tail = None

    #                 if final_head is None:
    #                     final_head = rev_head

    #                 if tail:
    #                     tail.next = rev_head

    #                 tail = head
    #                 head = node

    #         if tail:
    #             tail.next = head
    #         if final_head is None:
    #             return head
    #         return final_head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse_first_k(head, k):
            node = head
            pre = None
            while k > 0:
                next_node = node.next
                node.next = pre
                pre = node
                node = next_node
                k -= 1
            return pre

        node = head
        counter = 0
        while node:

            node = node.next
            counter += 1

            if 0 == counter % k:
                # reverse the group
                rev_head = reverse_first_k(head, k)
                # print(rev_head)

                head.next = self.reverseKGroup(node, k)

                return rev_head

        return head