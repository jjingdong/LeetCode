'''
1008. Construct Binary Search Tree from Preorder Traversal
Medium

Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.
Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 
Constraints:
	•	1 <= preorder.length <= 100
	•	1 <= preorder[i] <= 10^8
	•	The values of preorder are distinct.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # 8 5 1 7 10 12
    #   L      R
    # L = first value smaller than the root
    # R = first value larger than the root
    #
    # Solution I: construct BST from preorder and inorder traversal
    # Time O(NlogN) Space O(N)
    #
    # Solution I: recursion
    #
    # Solution II: iteration
    #
    # Note the solution is hard to understand, I need to review it again

    # Time O(N) Space O(N)
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def traverse(lower=float('-inf'), upper=float('inf')):
            nonlocal i

            if i == size: return None

            value = preorder[i]
            if value < lower or value > upper:
                return None

            i += 1
            root = TreeNode(value)
            root.left = traverse(lower, value)
            root.right = traverse(value, upper)
            return root

        if preorder is None: return None
        i = 0
        size = len(preorder)
        return traverse()







