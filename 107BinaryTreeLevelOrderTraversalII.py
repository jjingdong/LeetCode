'''
107. Binary Tree Level Order Traversal II
Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
For example: Given binary tree [3,9,20,null,null,15,7], 
    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as: 
[
  [15,7],
  [9,20],
  [3]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Time O(N) Space O(N)
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root: return []

        results = []
        queue = collections.deque([(root, 0)])
        prelevel = 0
        lst = []
        while queue:

            node, level = queue.popleft()
            if prelevel < level:
                results.append(lst)
                prelevel = level
                lst = [node.val]
            else:
                lst.append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        results.append(lst)

        return results[::-1]


