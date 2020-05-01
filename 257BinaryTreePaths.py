'''
257. Binary Tree Paths
Easy

Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.
Example:
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution I: recursive
    # Using a stack call
    #
    # Solution II: iterative
    # Using a stack

    # Time O(N) Space O(N)
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def traverse(node, path):
            if node is not None:
                path += str(node.val)

                if node.left is None and node.right is None:
                    paths.append(path)
                else:
                    path += '->'
                    traverse(node.left, path)
                    traverse(node.right, path)

        if root is None: return None
        paths = []
        traverse(root, '')
        return paths
