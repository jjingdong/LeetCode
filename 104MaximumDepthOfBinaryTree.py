# 104. Maximum Depth of Binary Tree
# Easy
#
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.
# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Solution I
    # Time O(N)
    # Space O(N)
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # Solutjion II
    # Time O(N) Space O(N)
    def maxDepth(self, root: TreeNode) -> int:

        def helper(node, d):
            nonlocal max_depth

            if not node: return

            max_depth = max(max_depth, d)

            helper(node.left, d + 1)
            helper(node.right, d + 1)

        max_depth = 0
        helper(root, 1)
        return max_depth
