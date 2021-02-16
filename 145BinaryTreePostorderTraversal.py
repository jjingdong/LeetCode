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
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        def dfs(node):
            if not node: return

            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        result = []
        dfs(root)
        return result


    # Iteration
    # Time O(N) Space O(N)
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

        return result[::-1]

'''