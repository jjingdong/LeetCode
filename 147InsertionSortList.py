'''
147. Insertion Sort List
Medium

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    #         re   node
    #          |    |
    #         -1    5->3->4->0
    #
    #     (1) -1    5    3->4->0
    #                    |
    #                    next_n
    #     (2) -1->5      3->4->0
    #                    |
    #                    node
    #     (1) -1->5   3  4->0
    #                    |
    #                    next_n
    #     (2) -1->3->5   4->0
    #                    |
    #                    node
    #     (1) -1->3->5   4  0
    #                       |
    #                       next_n
    #     (2) -1->3->4->5   0
    #                       |
    #                       node
    #     (1) -1->3->4->5   0
    #                       |
    #                       next_n
    #     (2) -1->0->3->4->5

    # Time O(N^2) Space O(1)
    # runtime = 1500, 50%
    def insertionSortList(self, head: ListNode) -> ListNode:

        def insert(re, cur_node):

            pre = ListNode(None)
            node = re
            pre.next = re

            new_re = pre
            while node:

                if node.val >= cur_node.val:
                    break

                pre = node
                node = node.next

            pre.next = cur_node
            cur_node.next = node

            return new_re.next

        if not head: return head

        re = head
        node = head.next
        re.next = None
        while node:
            next_n = node.next
            re = insert(re, node)
            node = next_n

        return re


'''
    #Time O(N^2) Space O(1)
    #runtime = 1500, 50%
    def insertionSortList(self, head: ListNode) -> ListNode:

        def insert(re, cur_node):

#             1 -> 2 -> 3 -> 5 -> 6 -> 7     4
#             |                              |
#             re                            cur_node
#                       |    |
#                       pre node

            pre = ListNode(None)
            node = re
            pre.next = re

            new_re = pre
            found = False
            while node:

                if node.val >= cur_node.val:
                    pre.next = cur_node
                    cur_node.next = node
                    found = True
                    break

                pre = node
                node = node.next

            if not found:
                if pre.val < cur_node.val:
                    pre.next = cur_node
                    return re
                elif re.val < cur_node.val:
                    re.next = cur_node
                    return re

            return new_re.next


        if not head: return head

        re = head
        node = head.next
        re.next = None
        while node:

            next_n = node.next
            node.next = None
            re = insert(re, node)
            node = next_n

        return re
'''
