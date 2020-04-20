'''
876. Middle of the Linked List
Easy

Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
 
Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Note:
	•	The number of nodes in the given list will be between 1 and 100.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Time O(N) Space O(1)
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None: return None

        slowNode = head
        fastNode = head
        while fastNode is not None and fastNode.next is not None:
            slowNode = slowNode.next
            fastNode = fastNode.next.next

        return slowNode


'''   
    # Time O(N) Space O(1)
    def middleNode(self, head: ListNode) -> ListNode:

        if head is None: return None

        size = 0
        curNode = head
        while curNode is not None:
            size += 1
            curNode = curNode.next

        mid = 0
        if size % 2 == 0:
            mid = size / 2 + 1
        else:
            mid = size // 2 + 1

        curNode = head
        while mid > 1:
            mid -= 1
            curNode = curNode.next

        return curNode
'''
