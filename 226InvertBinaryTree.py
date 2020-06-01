# https://leetcode.com/problems/invert-binary-tree/
#
# 226. Invert Binary Tree
# Easy
#
# 2396
#
# 38
#
# Add to List
#
# Share
# Invert a binary tree.
# Example:
# Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia: This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Time O(N) Space O(N)
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


'''
    # Time O(N) Space O(N)
    def invertTree(self, root: TreeNode) -> TreeNode:

        if root is None: return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
'''

