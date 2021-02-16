'''
144. Binary Tree Preorder Traversal
Medium

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [1,2]
Example 5:


Input: root = [1,null,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # recursion
    # Time O(N) Space O(N)
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root: return None

        def dfs(node):
            if not node: return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root)
        return result

    # Iteration
    # Time O(N) Space O(N)
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None: return

        result = []
        stack = [root]
        while stack:

            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

        # Morris Preorder Tree Traversal
        # Time O(N) Space O(1)
        def preorderTraversal(self, root: TreeNode) -> List[int]:

            if not root: return None

            result = []
            cur = root
            while cur:

                if cur.left:
                    pre = cur.left

                    while pre.right is not None and pre.right != cur:
                        pre = pre.right

                    if pre.right is None:
                        result.append(cur.val)
                        pre.right = cur
                        cur = cur.left
                    else:
                        pre.right = None
                        cur = cur.right
                else:
                    result.append(cur.val)
                    cur = cur.right

            return result



