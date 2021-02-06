'''
199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #            1            <---
    #          /   \
    #         2     3         <---
    #          \     \
    #           5     4       <---

    #     output = [1,3,4]

    #            1            <---
    #          /   \
    #         2     3         <---
    #       /
    #      5                  <---

    #     output = [1, 3, 5]

    #     BFS
    #     [1]
    #     [2, 3]
    #     [5]

    #     DFS
    #     [1]
    #     [2, 3]
    #     [5]

    # Time O(N) Space O(N)
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root: return None

        result = []
        queue = collections.deque([(root, 0)])
        pre_level = -1
        while queue:

            node, level = queue.popleft()
            if level != pre_level:
                result.append(node.val)
            else:
                result[level] = node.val

            pre_level = level

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result

