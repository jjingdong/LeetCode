'''
143. Reorder List
Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # index   0    1    2    3    4    5    6    7
    #         1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
    #                             i                    j
    #
    #         1 -> 2 -> 3 -> 4
    #                             5 -> 6 -> 7 -> 8
    #                             8 -> 7 -> 6 -> 5
    #
    #         1    8    2    7    3    6    4    5
    #
    #         reverse
    #         1 -> 2 -> 3
    #         pre_n node next_n
    #
    #         next_n.next = node
    #         node.next = pre_n
    #
    #         join
    #         1 -> 2 -> 3 -> 4
    #     node_1  node_1_next
    #                               8 -> 7 -> 6 -> 5
    #                            node_2 node_2_next
    #        node_1.next = node_2
    #        node_2.next = node_1_next

    # Time O(N) Space O(1), runtime = 92ms
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(node):

            pre_n = None
            while node:
                next_n = node.next
                node.next = pre_n

                pre_n = node
                node = next_n

            return pre_n

        def combine(node_1, node_2):

            while node_2.next:
                node_1_next = node_1.next
                node_2_next = node_2.next

                node_1.next = node_2
                node_2.next = node_1_next

                node_1 = node_1_next
                node_2 = node_2_next

        if not head: return

        # find the mid node
        s_node, f_node = head, head
        while f_node and f_node.next:
            s_node = s_node.next
            f_node = f_node.next.next

        # reverse the 2nd half
        node_2 = reverse(s_node)

        # join head with node_2
        combine(head, node_2)
