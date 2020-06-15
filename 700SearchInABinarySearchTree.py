'''
700. Search in a Binary Search Tree
Easy

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.
For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:
      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.
Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
Accepted

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution I: Recursion
    #
    # Solution II: Iteration

    # Time O(H) Space O(1), runtime = 72 ms
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root: return None

        while root and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left

        if not root: return None
        return root


'''
    # Time O(H) Space O(H), runtime = 76 ms
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root: return None

        def traverse(node):

            if not node: return None

            if node.val == val:
                return node
            elif node.val < val:
                return traverse(node.right)
            else:
                return traverse(node.left)

        return traverse(root)
'''

