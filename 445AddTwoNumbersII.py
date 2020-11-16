'''
445. Add Two Numbers II
Medium

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Solution I: reverse linked list
    #         3 -> 4 -> 2 -> 7
    #         4 -> 6 -> 5
    #
    #         7 -> 10
    #         7 -> 0 -> 8 -> 7
    #         7 -> 8 -> 0 -> 7
    #
    # Solution II:
    #         (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    #
    #         7 -> 2 -> 4 -> 3        length = 4
    #              5 -> 6 -> 4        length = 3
    #
    #         add them in reverse order:
    #         ? -> 7
    #         ? -> 7 -> 7
    #         ? -> 10 -> 7 -> 7
    #         7 -> 10 -> 7 -> 7
    #
    #         reverse
    #         ? -> 7
    #         ? -> 0 -> 7
    #         ? 8 -> 0 -> 7
    #         7 -> 8 -> 0 -> 7

    # Time O() Space O()
    # runtime =
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: