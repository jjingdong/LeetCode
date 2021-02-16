'''
94. Binary Tree Inorder Traversal
Medium

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

    # Recursion
    # Time O(N) Space O(H)
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def dfs(node):
            if not node: return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        result = []
        dfs(root)
        return result

    # Morris Tree Traversal
    # Time O(N) Space O(1)
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root: return None

        result = []
        cur = root
        while cur:

            if cur.left:
                pre = cur.left

                while pre.right is not None and pre.right != cur:
                    pre = pre.right

                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    result.append(cur.val)
                    cur = cur.right
            else:
                result.append(cur.val)
                cur = cur.right

        return result

    # Iteration
    # Time O(N) Space O(N)
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root: return []

        in_order = []
        stack = []
        node = root
        while node or stack:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            in_order.append(node.val)
            node = node.right

        return in_order
