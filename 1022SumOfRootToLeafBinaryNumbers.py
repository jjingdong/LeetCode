'''
1022. Sum of Root To Leaf Binary Numbers
Easy

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents
a binary number starting with the most significant bit.  For example, if the path
is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the
 root to that leaf.

Return the sum of these numbers.



Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #         dfs
    #         get value from the path    -> use binary shift
    #         sum the value

    # Time O(N) Space O(H), runtime = 36 ms
    def sumRootToLeaf(self, root: TreeNode) -> int:

        def dfs(node, num):
            nonlocal count

            if not node:
                return

            if not node.left and not node.right:
                count += (num << 1) + node.val
                return

            value = num << 1
            dfs(node.left, value + node.val)
            dfs(node.right, value + node.val)

        if not root: return None

        count = 0
        dfs(root, 0)
        return count

