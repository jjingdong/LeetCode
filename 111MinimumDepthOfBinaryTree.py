'''
111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # return the smallest path from left and right, except left is None or right is None

    # Time O(N) Space O(H)
    def minDepth(self, root: TreeNode) -> int:

        if not root: return 0

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if l == 0:
            return r + 1
        elif r == 0:
            return l + 1
        else:
            return min(l, r) + 1