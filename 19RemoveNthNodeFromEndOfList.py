'''
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and
return its head.

Follow up: Could you do this in one pass?



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Recursion
    # Time O(N) Space O(N)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        #         1 -> 2 -> 3 -> 4 -> 5 -> None

        #                       cur
        #                        |
        #                 pre_n   ---->  next_n

        #         n = 3
        #         1
        #         /
        #         2    count = 4, if count = n+1, pre_n is here. pre_n.next = next_n
        #         /
        #         3    count = 3
        #         /
        #         4    count = 2 , if count = n -1, next_n is here
        #         /
        #         5    count = 1

        # Eg.2
        #         1   count = 1

        def helper(node):
            nonlocal count, pre_n, next_n

            if node is None:
                return

            helper(node.next)
            count += 1
            if count == n - 1:
                next_n = node
            elif count == n + 1:
                pre_n = node

        count = 0
        dummy_node = ListNode()
        dummy_node.next = head
        pre_n = dummy_node
        next_n = None
        helper(head)
        pre_n.next = next_n
        return dummy_node.next

    # Iteration
    # Time O() Space O()
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        #         n = 2

        #         1 ->    2 ->    3 ->    4 ->    5
        #                         pre_n   cur    next_n
        #         s
        #         f
        #         count=1
        #                 ------------------------------
        #         s
        #                         f
        #                         ----------------------
        #                         s
        #                                         f

        f = head
        s = head
        for _ in range(n):
            f = f.next
        if f is None:
            return head.next

        while f.next is not None:
            f = f.next
            s = s.next

        s.next = s.next.next
        return head
