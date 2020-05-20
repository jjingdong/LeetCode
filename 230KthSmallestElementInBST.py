'''
230. Kth Smallest Element in a BST
Medium

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up: What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution: DFS inorder = BST
    # I: Recursion
    # II: Iteration

    # Time O(N) Space O(N)
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        if not root: return []

        count = 0
        stack = collections.deque([])
        node = root
        while node or stack:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right

        return -1


'''
    # Time O(N) Space O(N), using recursion
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def traverse(node):
            if node is None: return

            traverse(node.left)
            results.append(node.val)
            traverse(node.right)

        results = []
        traverse(root)
        return results[k-1]
'''


