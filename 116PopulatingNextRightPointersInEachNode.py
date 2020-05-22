'''

116. Populating Next Right Pointers in Each Node
Medium

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
 
Follow up:
	•	You may only use constant extra space.
	•	Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 
Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 
Constraints:
	•	The number of nodes in the given tree is less than 4096.
	•	-1000 <= node.val <= 1000

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:

    # Solution I: BFS + level
    #
    # Solution II: BFS + queue level pop & append
    #
    # Solution III: Use only pointer, not queue: node.right.next = node.next.left

    # Time O(N) Space O(1), using only .next pointer, runtime = 96 ms
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left

                head = head.next
            leftmost = leftmost.left

        return root


'''
    # Time O(N) Space O(N), using BFS + queue level pop & append, runtime = 168 ms
    def connect(self, root: 'Node') -> 'Node':

        if not root: return root

        queue = collections.deque([root])
        while queue:

            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)

        return root
'''

'''
    # Time O(N) Space O(N), using BFS + level, runtime 120 ms
    def connect(self, root: 'Node') -> 'Node':

        if not root: return root

        queue = collections.deque([(root, 0)])
        pre_level = -1
        last_node = None
        while queue:
            node, level = queue.popleft()
            node.next = None
            if level > pre_level:
                pre_level = level
            else:
                if node.next is None and last_node.next is None:
                    last_node.next = node
            if node.left:
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
            last_node = node

        return root
'''



