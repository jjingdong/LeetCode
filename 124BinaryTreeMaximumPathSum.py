'''
124. Binary Tree Maximum Path Sum
Hard

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Step I: calculate max_gain(cur_node)
    #   -10
    #   / \
    #  9  20
    #    /  \
    #   15   7
    # max_gain(9) = 9, max_gain(15) = 15, max_gain(7) = 7
    # max_gain(20) = 35 = max(15, 7) + 20
    #
    # Step II: max_sum
    #

    # Time O() Space O()
    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(cur_node):
            nonlocal max_sum

            if cur_node is None: return 0

            left_gain = max(maxGain(cur_node.left), 0)
            right_gain = max(maxGain(cur_node.right), 0)
            price_new_path = cur_node.val + left_gain + right_gain

            max_sum = max(max_sum, price_new_path)

            return max(left_gain, right_gain) + cur_node.val

        max_sum = float('-inf')
        maxGain(root)
        return max_sum


'''
        def max_gain(cur_node):

            if cur_node is None: return 0

            return max(max(max_gain(cur_node.left), 0), 
                    max(max_gain(cur_node.right), 0) + cur_node.val


        max_sum = float('-inf')
        return max_gain(root)
'''




