'''
101. Symmetric Tree
Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
 
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
 
Follow up: Solve it both recursively and iteratively.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution I: recursion
    #
    # Solution II: iteration, BFS
    #

    # Time O(N) Space O(1), using recursion
    def isSymmetric(self, root: TreeNode) -> bool:

        def traverse(l, r):

            if l is None and r is None: return True
            if l is None or r is None: return False

            if l.val != r.val: return False
            return traverse(l.left, r.right) and traverse(l.right, r.left)

        if root is None: return True
        return traverse(root, root)

