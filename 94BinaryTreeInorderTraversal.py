'''
94. Binary Tree Inorder Traversal
Medium

2790

120

Add to List

Share
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution I: Recursion
    # Solution II: Iteration
    # Solutjion III: Morri


    # Time O(N) Space O(N), using iteration
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root: return []

        in_order = []
        stack = collections.deque([])
        node = root
        while node or stack:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            in_order.append(node.val)
            node = node.right

        return in_order



    # Time O(N) Space O(N), using recursion
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root: return []

        def traverse(node): 
            if node is None: return

            traverse(node.left)
            in_order.append(node.val)
            traverse(node.right)

        in_order = []
        traverse(root)
        return in_order


    # Time O(N) Space O(N)
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root: return None
        result = []
        cur = root
        while cur:
            if not cur.left:
                result.append(cur.val)
                cur = cur.right
            else:
                predecessor = cur.left

                while predecessor.right != None and predecessor.right != cur:
                    predecessor = predecessor.right
                if predecessor.right == None:
                    predecessor.right = cur
                    cur = cur.left
                else:
                    predecessor.right = None
                    result.append(cur.val)
                    cur = cur.right

        return result
