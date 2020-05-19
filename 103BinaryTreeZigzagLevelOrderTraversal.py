'''
103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example: Given binary tree [3,9,20,null,null,15,7], 
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as: 
[
  [3],
  [20,9],
  [15,7]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution I: BFS
    #
    # Solution II: DFS

    # Time O(N) Space O(H), using DFS
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        def traverse(node, level):
            if not node: return

            if level >= len(results):
                results.append([node.val])
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level] = [node.val] + results[level]

            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        if not root: return []
        results = []
        traverse(root, 0)
        return results


'''
    # Time O(N) Space O(N), using BFS
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root: return []

        results = []

        queue = collections.deque([])
        queue.append((root, 0))
        preLevel = -1
        while queue:
            node, level = queue.popleft()
            if level > preLevel:
                results.append([node.val])
                preLevel = level
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level] = [node.val] + results[level]

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return results
'''

