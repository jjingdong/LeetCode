'''
404. Sum of Left Leaves
Easy

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively.
Return 24.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Time O(N) Space O(N), runtime = 48 ms
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root: return 0

        count = 0
        queue = collections.deque([(root, 'lr')])
        while queue:

            cur, lr = queue.popleft()

            if lr == 'l' and not cur.left and not cur.right:
                count += cur.val

            if cur.left:
                queue.append((cur.left, 'l'))
            if cur.right:
                queue.append((cur.right, 'r'))

        return count
