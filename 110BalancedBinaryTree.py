'''
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node
 differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #     3               node
    #    / \
    #   9  20            if abs(left subnode's height   -     right subnode's height) > 1: return False
    #     /  \            ^^^ recursive case
    #    15   7
    #
    #                     helper(node)         Time 2^height  Space 2^height
    #                     base case:
    #
    #                             if node is None:   return 0
    #
    #                             node has no children: return 1
    #
    #                     recursive
    #                             return max(leftnode's height + rightnode's height)

    #       1
    #      / \
    #     2   2
    #    / \
    #   3   3
    #  / \
    # 4   4

    # Time O(NlogN) Space O(N), runtime =
    def isBalanced(self, root: TreeNode) -> bool:

        def helper(node):
            nonlocal result

            if not node: return 0

            if not node.left and not node.right:
                return 1

            if result == False:
                return -1

            left_height = helper(node.left) + 1
            right_height = helper(node.right) + 1
            if abs(left_height - right_height) > 1:
                result = False
                return -1

            return max(left_height, right_height)

        result = True
        helper(root)
        return result



