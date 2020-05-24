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

    # Time O(N^2) Space O(1), runtime = 40 ms
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        if not preorder: return None

        root = TreeNode(preorder[0])
        stack = collections.deque([root])

        size = len(preorder)
        for i in range(1, size):
            node = stack[-1]
            child = TreeNode(preorder[i])

            while stack and stack[-1].val < child.val:
                node = stack.pop()

            if node.val < child.val:
                node.right = child
            else:
                node.left = child

            stack.append(child)

        return root


'''
    # Time O(N) Space O(N), using recursion, runtime = 36 ms
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def traverse(lower=float('-inf'), upper=float('inf')):
            nonlocal i

            if i == len(preorder): return

            value = preorder[i]
            if value < lower or value > upper: return

            i += 1
            root = TreeNode(value)
            root.left = traverse(lower, value)
            root.right = traverse(value, upper)
            return root


        if not preorder: return None
        i = 0
        return traverse()
'''

