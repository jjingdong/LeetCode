'''
 270. Closest Binary Search Tree Value
Easy

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #     4
    #    / \
    #   2   5
    #  / \
    # 1   3

    # 3.2 -> 4
    # 3.7 -> 5

    # Time O(H) Space O(1), runtime = 36 ms
    def closestValue(self, root: TreeNode, target: float) -> int:

        if not root: return None

        close_node = root
        node = root
        while node:

            if target == node.val:
                return node.val
            elif target < node.val:
                if abs(node.val - target) < abs(close_node.val - target):
                    close_node = node
                node = node.left
            else:
                if abs(node.val - target) < abs(close_node.val - target):
                    close_node = node
                node = node.right

        return close_node.val
