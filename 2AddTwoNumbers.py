'''
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Note. Can make it to Space O(1) if save results in l1

    # Time O(N) Space O(N)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = l3 = ListNode(None)
        carry = 0
        while l1 or l2 or carry:

            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, value = divmod((sum + carry), 10)
            l3.next = ListNode(value)
            l3 = l3.next

        return head.next

