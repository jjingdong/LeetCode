# 95. Unique Binary Search Trees II
# Medium
#
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Time: O(nGn)
    # Space: O(nGn)
    def generateTrees(self, n: int) -> List[TreeNode]:

        if n is None: return []
        if n < 1: return []

        def buildTree(start, end):

            allTrees = []

            if start > end:
                return [None]

            for i in range(start, end + 1):

                leftTrees = buildTree(start, i - 1)
                rightTrees = buildTree(i + 1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        allTrees.append(root)

            return allTrees

        return buildTree(1, n)