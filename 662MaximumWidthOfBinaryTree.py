'''
662. Maximum Width of Binary Tree
Medium

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
Example 1:
Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:
Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:
Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:
Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #      0
    #    /   \
    #   0     1
    #  / \     \
    # 0   1     3

    # Time O(N) Space O(N), runtime = 32 ms
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        if not root: return 0

        max_count, count_start, count_end = 0, 0, 0
        pre_level = -1

        queue = collections.deque([(root, count_start, 0)])
        while queue:

            node, num, level = queue.popleft()
            if pre_level == level:
                count_end = num
            else:
                max_count = max(max_count, count_end - count_start + 1)
                count_start = num
                pre_level = level

            if node.left:
                queue.append((node.left, num * 2, level + 1))
            if node.right:
                queue.append((node.right, num * 2 + 1, level + 1))

        max_count = max(max_count, count_end - count_start + 1)
        return max_count


