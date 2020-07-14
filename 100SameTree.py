'''
100. Same Tree
Easy

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Time O(N) Space O(N), runtime = 52 ms
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p or not q: return p == q
        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


'''   
    # Time O(N) Space O(N), runtime = 36 ms
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p or not q: return p == q

        queue_p = collections.deque([p])
        queue_q = collections.deque([q])
        while queue_p and queue_q:

            p = queue_p.popleft()
            q = queue_q.popleft()
            if q.val != p.val: return False
            if p.left and q.left:
                queue_p.append(p.left)
                queue_q.append(q.left)
            elif q.left or p.left: return False


            if p.right and q.right:
                queue_p.append(p.right)
                queue_q.append(q.right)
            elif p.right or q.right: return False

        if queue_p or queue_q: return False

        return True
'''