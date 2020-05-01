'''
112. Path Sum
Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution I:
    # Recursion with stack to track the value
    #
    # Solution II:
    # Iterative with a stack

    # Time O(N) Space O(N)
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def traverse(cur_node, local_sum):

            if cur_node is None: return None

            local_sum += cur_node.val

            if cur_node.left is None and cur_node.right is None:
                if local_sum == sum:
                    return True

            return traverse(cur_node.left, local_sum) or traverse(cur_node.right, local_sum)

        if root is None: return None
        return traverse(root, 0)



