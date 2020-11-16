'''
1026. Maximum Difference Between Node and Ancestor
Medium

Given the root of a binary tree, find the maximum value V for which there exist
different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any
child of A is an ancestor of B.



Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3


Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Time O(N) Space O(N)
    # runtime = 40 ms
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def traverse(node, max_ancestor, min_ancestor):
            nonlocal result

            if not node:
                return

            result = max(result, abs(max_ancestor - node.val), abs(min_ancestor - node.val))

            max_ancestor = max(max_ancestor, node.val)
            min_ancestor = min(min_ancestor, node.val)
            traverse(node.left, max_ancestor, min_ancestor)
            traverse(node.right, max_ancestor, min_ancestor)

        if not root: return 0
        result = 0
        traverse(root, root.val, root.val)
        return result


'''
    # Time O(N) Space O(N)
    # runtime = 2524 ms
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def traverse(node, ancestors):
            nonlocal result

            if not node:
                return

            for a in ancestors:
                result = max(result, abs(a-node.val))

            traverse(node.left, ancestors + [node.val])
            traverse(node.right, ancestors + [node.val])



        if not root: return 0
        result = 0
        traverse(root, [])
        return result
'''