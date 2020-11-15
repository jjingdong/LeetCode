'''
938. Range Sum of BST
Easy

Given the root node of a binary search tree, return the sum of values of all
nodes with a value in the range [low, high].



Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23


Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #         root = [10,5,15,3,7,null,18], low = 7, high = 15
    #         total = 10+15+7 = 32
    #
    #         root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    #         total = 6+7+10 = 23

    # Time O(N) Space O(N)
    # runtime = 196 ms
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def traverse(node):
            nonlocal total

            if low <= node.val <= high:
                total += node.val
            if node.left and node.val > low:
                traverse(node.left)
            if node.right and node.val < high:
                traverse(node.right)

        if not root: return 0
        total = 0
        traverse(root)
        return total


'''
    # Time O(N) Space O(N)
    # runtime = 216 ms
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def traverse(node):
            nonlocal total

            if low <= node.val <= high:
                total += node.val
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
            elif node.val < low:
                if node.right:
                    traverse(node.right)
            elif node.val > high:
                if node.left:
                    traverse(node.left)


        if not root: return 0
        total = 0
        traverse(root)
        return total
'''

